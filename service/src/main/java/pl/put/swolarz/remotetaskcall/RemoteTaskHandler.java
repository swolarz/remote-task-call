package pl.put.swolarz.remotetaskcall;

import com.google.protobuf.ByteString;
import pl.put.swolarz.remotetaskcall.generated.*;

import java.io.IOException;


class RemoteTaskHandler {

    private final TaskResponseStreamDispatcher responseDispatcher;

    private RemoteTaskProcess taskProcess;
    private boolean firstRequest;


    public RemoteTaskHandler(TaskResponseStreamDispatcher responseDispatcher) {
        this.responseDispatcher = responseDispatcher;

        this.firstRequest = true;
        this.taskProcess = null;
    }

    public void onNext(TaskRequest value) {
        onNextTaskRequest(value);
        firstRequest = false;
    }

    public void onCompleted() {
        try {
            taskProcess.finishInput();
        }
        catch (IOException e) {
            // No action apart from logging the error
            // The error should possibly happen on the process side
            System.err.printf("Warning: task process input close failure: %s%n", e.getMessage());
        }
    }

    private void onNextTaskRequest(TaskRequest value) {
        if (value.hasInput()) {
            if (firstRequest) {
                responseDispatcher.pushError(new IllegalArgumentException("Task command not present"));
                terminate();
            }

            ByteString bytesString = value.getInput().getData();
            byte[] bytes = bytesString.toByteArray();

            handleInput(bytes);
        }
        else if (value.hasCall()) {
            if (!firstRequest) {
                responseDispatcher.pushError(new IllegalArgumentException("Illegal repetition of task command"));
                terminate();
            }

            String taskCommand = value.getCall().getCommand();
            launchTaskProcess(taskCommand);
        }
    }

    private void handleInput(byte[] inputBytes) {
        try {
            taskProcess.acceptInput(inputBytes);
        }
        catch (IOException e) {
            System.err.printf("Error: failed to pipe input to process: %s%n", e.getMessage());
            responseDispatcher.pushError(new RuntimeException("Failed to pass input to process"));

            terminate();
        }
    }

    private void launchTaskProcess(String taskCommand) {
        taskProcess = RemoteTaskProcess.builder()
                .command(taskCommand)
                .onOutputStream(this::passOutputStream)
                .onErrorStream(this::passErrorStream)
                .onExit(this::handleTaskExit)
                .build();

        try {
            taskProcess.start();
        }
        catch (IOException e) {
            System.err.printf("Warning: failed to start task process: %s%n", e.getMessage());
            responseDispatcher.pushError(new RuntimeException(String.format("Failed to start process with command: %s", taskCommand)));

            terminate();
        }
    }

    private void handleTaskExit(int status) {
        ExitStatus exitStatus = ExitStatus.newBuilder().setCode(status).build();
        TaskResult result = TaskResult.newBuilder().setStatus(exitStatus).build();

        responseDispatcher.pushResponse(result);
        responseDispatcher.notifyCompleted();

        terminate();
    }

    private void passOutputStream(byte[] out) {
        ByteString outBytes = ByteString.copyFrom(out);
        StdOutput stdOutput = StdOutput.newBuilder().setData(outBytes).build();
        TaskResult result = TaskResult.newBuilder().setStd(stdOutput).build();

        responseDispatcher.pushResponse(result);
    }

    private void passErrorStream(byte[] err) {
        ByteString errBytes = ByteString.copyFrom(err);
        ErrOutput errOutput = ErrOutput.newBuilder().setData(errBytes).build();
        TaskResult result = TaskResult.newBuilder().setErr(errOutput).build();

        responseDispatcher.pushResponse(result);
    }

    public void terminate() {
        if (taskProcess != null)
            taskProcess.terminate();

        // TODO shutdown client heartbeat

        responseDispatcher.stop();
    }
}

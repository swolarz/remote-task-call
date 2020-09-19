package pl.put.swolarz.remotetaskcall;

import io.grpc.stub.StreamObserver;
import pl.put.swolarz.remotetaskcall.generated.TaskExecutionServiceGrpc;
import pl.put.swolarz.remotetaskcall.generated.TaskRequest;
import pl.put.swolarz.remotetaskcall.generated.TaskResult;

import java.util.concurrent.atomic.AtomicBoolean;


class RemoteTaskService extends TaskExecutionServiceGrpc.TaskExecutionServiceImplBase {

    public RemoteTaskService() {
    }

    @Override
    public StreamObserver<TaskRequest> launchTask(StreamObserver<TaskResult> responseObserver) {
        TaskResponseStreamDispatcher responseDispatcher = new TaskResponseStreamDispatcher(responseObserver);
        AtomicBoolean firstRequest = new AtomicBoolean(true);

        // TODO initialize heartbeat and graceful shutdown handler
        // Heartbeat may not be needed

        return new StreamObserver<>() {
            @Override
            public void onNext(TaskRequest value) {
                onNextTaskRequest(value, responseDispatcher, firstRequest.get());
                firstRequest.set(false);
            }

            @Override
            public void onError(Throwable t) {
                onClientError(t);
            }

            @Override
            public void onCompleted() {
                onClientCompleted();
            }
        };
    }

    private void onNextTaskRequest(TaskRequest value, TaskResponseStreamDispatcher responseDispatcher, boolean firstRequest) {
        if (value.hasInput()) {
            if (firstRequest) {
                // TODO move error notification to dispatcher
                responseDispatcher.pushError(new IllegalArgumentException("Task command not present"));
            }

            // TODO pass received part of input stream to the process
        }
        else if (value.hasCall()) {
            // TODO initialize and start process and heartbeat threads
            String taskCommand = value.getCall().getCommand();

            // TODO add callbacks for handling output streams
            RemoteTaskProcess taskProcess = RemoteTaskProcess.builder()
                    .command(taskCommand)
                    .build();

            taskProcess.start();
        }
    }

    private void onClientError(Throwable t) {
        // TODO log error and stop process
    }

    private void onClientCompleted() {
        // TODO send EOF to processes input stream if necessary
    }
}

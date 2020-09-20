package pl.put.swolarz.remotetaskcall;

import lombok.Builder;
import lombok.NonNull;

import java.io.*;
import java.util.Arrays;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.function.Consumer;


class RemoteTaskProcess {

    private final String command;
    private final AtomicBoolean started;

    private Process process;

    private OutputStream inputStream;
    private InputStream outputStream;
    private InputStream errorStream;

    private CompletableFuture<Void> outputFuture;
    private CompletableFuture<Void> errorFuture;
    private CompletableFuture<Void> exitFuture;

    private final Consumer<byte[]> onOutputStream;
    private final Consumer<byte[]> onErrorStream;
    private final Consumer<Integer> onExit;


    @Builder
    private RemoteTaskProcess(@NonNull String command,
                              Consumer<byte[]> onOutputStream,
                              Consumer<byte[]> onErrorStream,
                              Consumer<Integer> onExit) {

        this.command = command;
        this.started = new AtomicBoolean(false);

        this.onOutputStream = onOutputStream;
        this.onErrorStream = onErrorStream;
        this.onExit = onExit;
    }

    public void start() throws IOException {
        process = new ProcessBuilder()
                .command("bash", "-c", command)
                .directory(new File("/tmp"))
                .redirectInput(ProcessBuilder.Redirect.PIPE)
                .redirectOutput(ProcessBuilder.Redirect.PIPE)
                .redirectError(ProcessBuilder.Redirect.PIPE)
                .start();

        inputStream = process.getOutputStream();
        outputStream = process.getInputStream();
        errorStream = process.getErrorStream();

        outputFuture = CompletableFuture.runAsync(() -> readStream(outputStream, onOutputStream, "stdout"));
        errorFuture = CompletableFuture.runAsync(() -> readStream(errorStream, onErrorStream, "stderr"));

        CompletableFuture.allOf(outputFuture, errorFuture).thenRunAsync(this::resolveExitStatus);

        started.set(true);
    }

    private void resolveExitStatus() {
        try {
            int status = process.waitFor();
            onExit.accept(status);
        }
        catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void readStream(InputStream stream, Consumer<byte[]> consumer, String name) {
        try (BufferedInputStream bufferedOutput = new BufferedInputStream(stream)) {
            byte[] buffer = new byte[4096];
            int bytesRead = 0;

            while ((bytesRead = bufferedOutput.read(buffer)) != -1) {
                byte[] output = Arrays.copyOf(buffer, bytesRead);
                consumer.accept(output);
            }
        }
        catch (IOException e) {
            System.err.printf("Warning: unexpected read failure for %s: %s%n", name, e.getMessage());
        }
    }

    public void acceptInput(byte[] inputChunk) throws IOException {
        inputStream.write(inputChunk);
    }

    public void finishInput() throws IOException {
        inputStream.close();
    }

    public void terminate() {
        outputFuture.cancel(true);
        errorFuture.cancel(true);
        exitFuture.cancel(true);

        process.destroy();
    }
}

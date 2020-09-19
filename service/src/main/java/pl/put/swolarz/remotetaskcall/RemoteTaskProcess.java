package pl.put.swolarz.remotetaskcall;

import lombok.Builder;
import lombok.NonNull;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.concurrent.atomic.AtomicBoolean;


class RemoteTaskProcess {

    private final String command;
    private final AtomicBoolean started;

    private InputStream inputStream;
    private OutputStream outputStream;


    @Builder
    private RemoteTaskProcess(@NonNull String command) {
        this.command = command;
        this.started = new AtomicBoolean(false);

        this.inputStream = null;
        this.outputStream = null;
    }

    public void start() {
        // TODO initialise process
        started.set(true);
    }

    public InputStream getInputStream() {
        if (!started.get())
            throw new IllegalStateException("Process not started yet");

        return inputStream;
    }

    public OutputStream getOutputStream() {
        if (!started.get())
            throw new IllegalStateException("Process not started yet");

        return outputStream;
    }
}

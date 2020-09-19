package pl.put.swolarz.remotetaskcall;

import io.grpc.stub.StreamObserver;
import pl.put.swolarz.remotetaskcall.generated.TaskResult;

class TaskResponseStreamDispatcher {

    private final StreamObserver<TaskResult> responseObserver;
    private boolean finalized;

    public TaskResponseStreamDispatcher(StreamObserver<TaskResult> responseObserver) {
        this.responseObserver = responseObserver;
        this.finalized = false;
    }

    public synchronized void pushResponse() {
        if (finalized)
            return;

        // TODO implement
    }

    public synchronized void notifyCompleted() {
        if (finalized)
            return;

        // TODO implement
    }

    public synchronized void pushError(Throwable error) {
        if (finalized)
            return;

        responseObserver.onError(error);
        finalized = true;
    }

    public synchronized void stop() {
        finalized = true;
    }
}

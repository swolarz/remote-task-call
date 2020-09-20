package pl.put.swolarz.remotetaskcall;

import io.grpc.stub.StreamObserver;
import pl.put.swolarz.remotetaskcall.generated.*;


class RemoteTaskService extends TaskExecutionServiceGrpc.TaskExecutionServiceImplBase {

    @Override
    public StreamObserver<TaskRequest> launchTask(StreamObserver<TaskResult> responseObserver) {
        final TaskResponseStreamDispatcher responseDispatcher = new TaskResponseStreamDispatcher(responseObserver);
        final RemoteTaskHandler taskHandler = new RemoteTaskHandler(responseDispatcher);

        // TODO initialize heartbeat and graceful shutdown handler

        return new StreamObserver<>() {
            @Override
            public void onNext(TaskRequest value) {
                taskHandler.onNext(value);
            }

            @Override
            public void onError(Throwable t) {
                System.out.printf("Warning: client side error: %s%n", t.getMessage());
                taskHandler.terminate();
            }

            @Override
            public void onCompleted() {
                taskHandler.onCompleted();
            }
        };
    }
}

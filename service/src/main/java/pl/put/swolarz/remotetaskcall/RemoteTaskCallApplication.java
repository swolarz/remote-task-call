package pl.put.swolarz.remotetaskcall;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;
import java.util.concurrent.TimeUnit;


public class RemoteTaskCallApplication {

	private static Server server;

	public static void main(String[] args) {
		int port = 9090;
		if (args.length > 0) {
			try {
				port = Integer.parseInt(args[0]);
			}
			catch (NumberFormatException e) {
				System.err.printf("Error: invalid port: %s%n", e.getMessage());
				System.exit(2);
			}
		}

		RemoteTaskService service = new RemoteTaskService();
		server = ServerBuilder.forPort(port)
				.addService(service)
				.build();

		try {
			server.start();
		}
		catch (IOException e) {
			System.err.printf("Error: failed to setup rpc server: %s%n", e.getMessage());
			System.exit(1);
		}

		Runtime.getRuntime().addShutdownHook(new Thread(() -> {
			System.err.print("Shutting down... ");
			try {
				server.awaitTermination(5, TimeUnit.SECONDS);
			}
			catch (InterruptedException e) {
				System.err.print("warning: rpc server interrupted... ");
			}

			System.err.println("Done.");
		}));

		try {
			server.awaitTermination();
		}
		catch (InterruptedException e) {
			System.err.printf("Error: main thread interrupted: %s%n", e.getMessage());
			System.exit(1);
		}
	}
}

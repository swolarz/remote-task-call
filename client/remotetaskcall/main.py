import argparse
import sys

import grpc

import taskcall_pb2
import taskcall_pb2_grpc


def main(args):
    service_endpoint = '{}:{}'.format(args.host, args.port)
    channel = grpc.insecure_channel(service_endpoint)

    stub = taskcall_pb2_grpc.TaskExecutionServiceStub(channel)

    def request_iterator():
        yield taskcall_pb2.TaskRequest(command=taskcall_pb2.TaskCall(command=args.command))

        chunk_size = 8192
        for bytes_line in iter(sys.stdin.buffer.readline, b''):
            for pt in range(0, len(bytes_line), chunk_size):
                chunk = bytes_line[pt:pt + chunk_size]
                yield taskcall_pb2.TaskRequest(input=taskcall_pb2.TaskInput(data=chunk))

    request_iter = request_iterator()
    for response in stub.LaunchTask(request_iter):
        if response.WhichOneof('OutputType') == 'std':
            std = response.std.data
            sys.stdout.buffer.write(std)
            sys.stdout.flush()

        elif response.WhichOneof('OutputType') == 'err':
            err = response.err.data
            sys.stderr.buffer.write(err)
            sys.stderr.flush()

        elif response.WhichOneof('OutputType') == 'status':
            code = response.status.code
            exit(code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for Remote Task Service')

    parser.add_argument('-p', '--port', type=int, default=9090)
    parser.add_argument('-h', '--host', type=str, default='localhost')
    parser.add_argument('-c', '--command', type=str, required=True)

    args = parser.parse_args()

    main(args)

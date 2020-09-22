import sys
import select
import signal

import argparse

import grpc

import taskcall_pb2
import taskcall_pb2_grpc


def main(args):
    service_endpoint = '{}:{}'.format(args.host, args.port)
    channel = grpc.insecure_channel(service_endpoint)

    try:
        grpc.channel_ready_future(channel).result(timeout=3)
    except grpc.FutureTimeoutError:
        print('Service not available...')
        return

    stub = taskcall_pb2_grpc.TaskExecutionServiceStub(channel)

    def request_iterator():
        yield taskcall_pb2.TaskRequest(call=taskcall_pb2.TaskCall(command=args.command))

        chunk_size = 8192

        select.select([sys.stdin.buffer], [], [])
        for bytes_line in iter(sys.stdin.buffer.readline, b''):
            for pt in range(0, len(bytes_line), chunk_size):
                chunk = bytes_line[pt:pt + chunk_size]
                yield taskcall_pb2.TaskRequest(input=taskcall_pb2.TaskInput(data=chunk))

            select.select([sys.stdin.buffer], [], [])

    request_iter = request_iterator()
    task_stream = stub.LaunchTask(request_iter)

    signal.signal(signal.SIGINT, lambda sig, frame: task_stream.cancel())

    try:
        for response in task_stream:
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
                print('# Process exited with code: {}'.format(code))
                break
    except grpc._channel._MultiThreadedRendezvous as e:
        # A hack for clean terminal output on exit
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for Remote Task Service')

    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=9090)
    parser.add_argument('-c', '--command', type=str, required=True)

    args = parser.parse_args()

    main(args)


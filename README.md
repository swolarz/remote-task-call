# Remote Task Call Service

## Overview

Service for launching command line processes on the server machine.
The standard output and error streams are redirected to the client.
The client redirects standard input to the process on the server side.
When the process finishes, the client is informed about exit status of the finished process.

## Running application

#### Running service

```
./gradlew run
```

By default, port **9090** is used. To specify port run:

```
./gradlew run --args='<PORT>'
```

#### Running client

To run client via makefile python grpc packages must be installed:

```
make install
```
This installs virtualenv, creates new virtual environment for python and then installs necessary packages.

As an example command we will use `python3 -i` (the `-i` flag is necessary to run python in the interactive mode).

```
CLIENT_COMMAND='python -i' make start
```

Client will try to connect gRPC server at localhost:9090.
To run with different connection settings run:

```
SERVICE_HOST=<HOST> SERVICE_PORT=<PORT> CLIENT_COMMAND='python3 -i' make start
```

Or run via docker (no virtualenv installation needed):

```
docker image build -t rtc_client .
docker container run --network=host -e CLIENT_COMMAND='python3 -i' -it rtc_client
```

The `SERVICE_HOST` and `SERVICE_PORT` variables can be passed via docker command as well:

```
docker container run --network=host -e SERVICE_HOST=<HOST> -e SERVICE_PORT=<PORT> -e CLIENT_COMMAND='python3 -i' -it rtc_client
```

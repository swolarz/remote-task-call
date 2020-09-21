
PROJECT_ROOT := $(shell pwd)
SRC_ROOT := $(PROJECT_ROOT)/remotetaskcall
PROTO_ROOT := $(SRC_ROOT)/proto
GEN_ROOT := $(SRC_ROOT)/generated

PROTO_SOURCES := $(shell find $(PROTO_ROOT) -type f -name "*.proto")

export PYTHONPATH := $(PYTHONPATH):$(SRC_ROOT):$(GEN_ROOT)


.PHONY: all protocol install clean

all: protocol

protocol: $(PROTO_SOURCES)
	mkdir -p $(GEN_ROOT)
	python -m grpc_tools.protoc -I $(PROTO_ROOT) --python_out=$(GEN_ROOT) --grpc_python_out=$(GEN_ROOT) $(PROTO_SOURCES)

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	virtualenv --python=python3 venv
	source venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install grpcio grpcio-tools

clean:
	rm -r $(GEN_ROOT)


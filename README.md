# README

## Setup

In order to run this you will need to run 

```pip install -r requirements.txt```

for requirements installation

Then you will need to have at least one instance of a [geoservice](https://github.com/juanpisani/geoService) or [authservice](https://github.com/franz-sotoleal/auth-service) running.

This is important because otherwise though the server will start nothing will work.

### Troubleshooting

You may need to recompile the protobufs by running ```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. geoService.proto --experimental_allow_proto3_optional```

## config.yaml

### geoservices

A list of string with the host and port for the instances of geoservices

### authservices

A list of string with the host and port for the instances of geoservices

### max_retries

How much a call to a path will be done, alternating concrete service

## Run

In order to run it with the IDE or execute ```python main.py```.

To run it from the IDE it should be enough to just to right click on the file you want to run and use ```Run```

## HELP! NOTHING IS WORKING

Ping ropa1998
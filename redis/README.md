# Documentation for `gcr.io/distroless/redis`

## Image Contents

This image contains a redis-server

Specifically, the image contains everything in the [base image](../base/README.md), plus:

* redis-server and jemalloc

## Usage

The entrypoint of this image is set to "redis-server", so this image expects users to supply a path to a config file in the CMD.

See the Redis [Hello World](../examples/redis/) directory for an example.

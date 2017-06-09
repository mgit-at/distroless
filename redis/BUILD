package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@runtimes_common//structure_tests:tests.bzl", "structure_test")

docker_build(
    name = "redis",
    base = "//init:init-base",
    cmd = [
        "/usr/bin/redis-server",
        "/redis.conf",
    ],
    debs = [
        "@redis_server//file",
        "@libjemalloc//file",
    ],
    files = [
        "redis.conf",
    ],
    ports = ["6379"],
    symlinks = {
        "/var/lib/redis": "/srv",
    },
    volumes = [
        "/srv",
    ],
)

structure_test(
    name = "redis_test",
    config = "testdata/redis.yaml",
    image = ":redis",
)

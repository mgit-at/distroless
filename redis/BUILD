package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@runtimes_common//structure_tests:tests.bzl", "structure_test")

docker_build(
    name = "redis",
    base = "//base:base",
    debs = [
        "@redis_server//file",
        "@libjemalloc//file",
    ],
    entrypoint = [
        "/usr/bin/redis-server",
    ],
)

structure_test(
    name = "redis_test",
    config = "testdata/redis.yaml",
    image = ":redis",
)

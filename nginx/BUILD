package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@runtimes_common//structure_tests:tests.bzl", "structure_test")
load("@debian_jessie_amd64//debs:deb_packages.bzl", "debian_jessie_amd64")
load("@debian_jessie_backports_amd64//debs:deb_packages.bzl", "debian_jessie_backports_amd64")

docker_build(
    name = "nginx",
    base = "//init:init-base",
    cmd = [
        "/usr/sbin/nginx",
        "-g",
        "daemon off; worker_processes 4;",
    ],
    debs = [
        debian_jessie_amd64["libpcre3"],
        debian_jessie_amd64["zlib1g"],
        debian_jessie_backports_amd64["libssl1.0.0"],
        debian_jessie_backports_amd64["nginx-common"],
        debian_jessie_backports_amd64["nginx-extras"],
    ],
    files = [
        "nginx.conf",
    ],
    ports = ["6379"],
    # does not work together with nginx-common
    #symlinks = {
    #    "/var/lib/nginx": "/srv",
    #},
    volumes = [
        "/srv",
    ],
)

structure_test(
    name = "nginx_test",
    config = "testdata/nginx.yaml",
    image = ":nginx",
)

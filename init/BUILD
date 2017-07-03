package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@runtimes_common//structure_tests:tests.bzl", "structure_test")
load("@io_bazel_rules_docker//docker/contrib:passwd.bzl", "passwd_file")

# we are not running as root
passwd_file(
    name = "init_passwd",
    gid = 1000,
    info = "user",
    uid = 1000,
    username = "user",
)

# rename tini-static-muslc-amd64 to tini
genrule(
    name = "tini_tar",
    srcs = ["@tini//file"],
    outs = ["tini.tar"],
    cmd = "cp $(<) tini; tar cf $@ tini",
)

docker_build(
    name = "init-base",
    base = "//base:base",
    entrypoint = [
        "/tini",
        "--",
    ],
    tars = [
        ":tini.tar",
        ":init_passwd.passwd.tar",
    ],
    # enable this base for debugging
    #base = "//busybox:debug",
    user = "user",
)

structure_test(
    name = "init_test",
    config = "testdata/init.yaml",
    image = ":init-base",
)

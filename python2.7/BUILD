package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@runtimes_common//structure_tests:tests.bzl", "structure_test")
load("@package_bundle//file:packages.bzl", "packages")

docker_build(
    name = "python27",
    # Based on //cc:cc so that C extensions work properly.
    base = "//cc:cc",
    debs = [
        packages["zlib1g"],
        packages["python2.7-minimal"],
        packages["libpython2.7-minimal"],
        packages["libpython2.7-stdlib"],
    ],
    entrypoint = [
        "/usr/bin/python2.7",
    ],
    symlinks = {
        "/usr/bin/python": "/usr/bin/python2.7",
    },
)

structure_test(
    name = "python27_test",
    config = "testdata/python27.yaml",
    image = ":python27",
)

load("@debian_jessie_amd64//debs:deb_packages.bzl", "debian_jessie_amd64")

docker_build(
    name = "deb_packages_python27",
    # Based on //cc:deb_packages_cc so that C extensions work properly.
    base = "//cc:deb_packages_cc",
    debs = [
        debian_jessie_amd64["zlib1g"],
        debian_jessie_amd64["python2.7-minimal"],
        debian_jessie_amd64["libpython2.7-minimal"],
        debian_jessie_amd64["libpython2.7-stdlib"],
    ],
    entrypoint = [
        "/usr/bin/python2.7",
    ],
    symlinks = {
        "/usr/bin/python": "/usr/bin/python2.7",
    },
)

structure_test(
    name = "deb_packages_python27_test",
    config = "testdata/python27.yaml",
    image = ":deb_packages_python27",
)

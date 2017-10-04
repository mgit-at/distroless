package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@package_bundle//file:packages.bzl", "packages")

# An intermediate image for Java and other "mostly statically" compiled languages
docker_build(
    name = "cc",
    base = "//base:base",
    debs = [
        packages["libgcc1"],
        packages["libstdc++6"],
    ],
)

load("@debian_jessie_amd64//debs:deb_packages.bzl", "debian_jessie_amd64")

docker_build(
    name = "deb_packages_cc",
    base = "//base:deb_packages_base",
    debs = [
        debian_jessie_amd64["libgcc1"],
        debian_jessie_amd64["libstdc++6"],
    ],
)

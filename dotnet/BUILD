package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//docker:docker.bzl", "docker_build")
load("@package_bundle//file:packages.bzl", "packages")

docker_build(
    name = "dotnet",
    base = "//cc:cc",
    debs = [
        packages["libcurl3"],
        packages["libgssapi-krb5-2"],
        packages["libicu52"],
        packages["liblttng-ust0"],
        packages["libunwind8"],
        packages["libuuid1"],
        packages["liblzma5"],
    ],
    entrypoint = [
        #"/opt/dotnet/dotnet",
    ],
    symlinks = {
        "/usr/bin/dotnet": "/opt/dotnet/dotnet",
    },
    tars = ["@dotnet//:tar"],
)

load("@debian_jessie_amd64//debs:deb_packages.bzl", "debian_jessie_amd64")

docker_build(
    name = "deb_packages_dotnet",
    base = "//cc:deb_packages_cc",
    debs = [
        debian_jessie_amd64["libcurl3"],
        debian_jessie_amd64["libgssapi-krb5-2"],
        debian_jessie_amd64["libicu52"],
        debian_jessie_amd64["liblttng-ust0"],
        debian_jessie_amd64["libunwind8"],
        debian_jessie_amd64["libuuid1"],
        debian_jessie_amd64["liblzma5"],
    ],
    entrypoint = [
        #"/opt/dotnet/dotnet",
    ],
    symlinks = {
        "/usr/bin/dotnet": "/opt/dotnet/dotnet",
    },
    tars = ["@dotnet//:tar"],
)

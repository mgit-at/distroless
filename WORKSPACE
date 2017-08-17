workspace(name = "distroless")

git_repository(
    name = "io_bazel_rules_go",
    remote = "https://github.com/bazelbuild/rules_go.git",
    tag = "0.4.4",
)

load("@io_bazel_rules_go//go:def.bzl", "go_repositories")

go_repositories()

# To build the par file for the helper program in deb_helper
git_repository(
    name = "subpar",
    remote = "https://github.com/google/subpar",
    tag = "1.0.0",
)

# An example of actually using the new rules of this project
load(
    "//deb_helper:deb_helper.bzl",
    "deb_loader",
    "deb_packages",
)

# Initialize the deb_loader which downloads the deb files in deb_packages rules
deb_loader()

# For every source of deb packages create a deb_packages rule
# The name does not have to be like the one here, but it helps to know what is used in BUILD files
deb_packages(
    name = "debian_jessie_amd64",
    architecture = "amd64",
    distro = "jessie",
    distro_type = "debian",
    mirrors = [
        "http://deb.debian.org",
        #"http://my.private.mirror",
    ],
    packages = {
        "ca-certificates": "pool/main/c/ca-certificates/ca-certificates_20141019+deb8u3_all.deb",
        "libc6": "pool/main/g/glibc/libc6_2.19-18+deb8u10_amd64.deb",
        "libjemalloc1": "pool/main/j/jemalloc/libjemalloc1_3.6.0-3_amd64.deb",
        "libssl1.0.0": "pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb",
        "netbase": "pool/main/n/netbase/netbase_5.3_all.deb",
        "openssl": "pool/main/o/openssl/openssl_1.0.1t-1+deb8u6_amd64.deb",
    },
    packages_sha256 = {
        "ca-certificates": "bd799f47f5ae3260b6402b1fe19fe2c37f2f4125afcd19327bf69a9cf436aeff",
        "libc6": "0a95ee1c5bff7f73c1279b2b78f32d40da9025a76f93cb67c03f2867a7133e61",
        "libjemalloc1": "caeeb8b60bee0b732de25b6091dae30d58f1cebcf7467900525d5d266d4360ba",
        "libssl1.0.0": "0fc777d9242fd93851eb49c4aafd22505048b7797c0178f20c909ff918320619",
        "netbase": "3979bdd40c5666ef9bf71a5391ba01ad38e264f2ec96d289993f2a0805616dd3",
        "openssl": "41613658b4e93ffaa7de25060a4a1ab2f8dfa1ee15ed90aeac850a9bf5a134bb",
    },
    # TODO:
    #tags = [
    #    "manual",
    #]
)

deb_packages(
    name = "debian_jessie_backports_amd64",
    architecture = "amd64",
    distro = "jessie-backports",
    distro_type = "debian",
    mirrors = [
        "http://deb.debian.org",
        #"http://my.private.mirror",
    ],
    packages = {"redis-server": "pool/main/r/redis/redis-server_3.2.8-2~bpo8+1_amd64.deb"},
    packages_sha256 = {"redis-server": "660fb0b07fad591fe6b44f547c0314b91f2fa1515375c51d7cf8be01072e1206"},
    # TODO:
    #tags = [
    #    "manual",
    #]
)

# In the BUILD file where you want to use this source, add a line like this (always @<rule_name>//debs:deb_packages.bzl):
#
# load("@debian_jessie_amd64//debs:deb_packages.bzl", "debian_jessie_amd64")
#
# and in the docker_build rule refer to packages like this:
#
# docker_build(
#     debs = [
#         debian_jessie_amd64["foo"],
#         [...]

# For the glibc base image.
http_file(
    name = "glibc",
    sha256 = "bdf12aa461f2960251292c9dbfa2702d65105555b12cb36c6ac9bf8bea10b382",
    url = "http://deb.debian.org/debian/pool/main/g/glibc/libc6_2.19-18+deb8u9_amd64.deb",
)

http_file(
    name = "ca_certificates",
    sha256 = "bd799f47f5ae3260b6402b1fe19fe2c37f2f4125afcd19327bf69a9cf436aeff",
    url = "http://deb.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_20141019+deb8u3_all.deb",
)

http_file(
    name = "openssl",
    sha256 = "41613658b4e93ffaa7de25060a4a1ab2f8dfa1ee15ed90aeac850a9bf5a134bb",
    url = "http://deb.debian.org/debian/pool/main/o/openssl/openssl_1.0.1t-1+deb8u6_amd64.deb",
)

http_file(
    name = "libssl",
    sha256 = "9c8637febf6a32c300bebd1eaa8d78f3845dd6d87d8c5e56345e5fc5f3041034",
    url = "http://deb.debian.org/debian/pool/main/o/openssl/libssl1.1-udeb_1.1.0f-3_amd64.udeb",
)

# For Java
http_file(
    name = "zlib",
    sha256 = "b75102f61ace79c14ea6f06fdd9509825ee2af694c6aa503253df4e6659d6772",
    url = "http://deb.debian.org/debian/pool/main/z/zlib/zlib1g_1.2.8.dfsg-2+b1_amd64.deb",
)

http_file(
    name = "openjdk_jre8",
    sha256 = "11c592e237549d74bda30875979c2a937588667d10307c7c14047b8d03f5718a",
    url = "http://deb.debian.org/debian/pool/main/o/openjdk-8/openjdk-8-jre-headless_8u131-b11-1~bpo8+1_amd64.deb",
)

http_file(
    name = "libstdcpp6",
    sha256 = "f1509bbabd78e89c861de16931aec5988e1215649688fd4f8dfe1af875a7fbef",
    url = "http://deb.debian.org/debian/pool/main/g/gcc-4.9/libstdc++6_4.9.2-10_amd64.deb",
)

http_file(
    name = "libgcc1",
    sha256 = "a1402290165e8d91b396a33d79580a4501041e92bdb62ef23929a0c207cd9af9",
    url = "http://deb.debian.org/debian/pool/main/g/gcc-4.9/libgcc1_4.9.2-10_amd64.deb",
)

# For Jetty
new_http_archive(
    name = "jetty",
    build_file = "BUILD.jetty",
    sha256 = "ca93c7f88e842fcb1e7bd551c071b3302b7be1faf9cad3ce415af19c77d6cb74",
    strip_prefix = "jetty-distribution-9.4.4.v20170414/",
    type = "tgz",
    url = "http://central.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.4.v20170414/jetty-distribution-9.4.4.v20170414.tar.gz",
)

# For Python
http_file(
    name = "libpython27",
    sha256 = "916e2c541aa954239cb8da45d1d7e4ecec232b24d3af8982e76bf43d3e1758f3",
    url = "http://deb.debian.org/debian/pool/main/p/python2.7/libpython2.7-minimal_2.7.9-2+deb8u1_amd64.deb",
)

http_file(
    name = "python27",
    sha256 = "c89199f908d5a508d8d404efc0e1aef3d9db59ea23bd4532df9e59941643fcfb",
    url = "http://deb.debian.org/debian/pool/main/p/python2.7/python2.7-minimal_2.7.9-2+deb8u1_amd64.deb",
)

http_file(
    name = "libpython27_stdlib",
    sha256 = "d997ef9edbccea4f1902a443a31c26c5c62cc5e2c9a679b3ace19909c8dc9f31",
    url = "http://deb.debian.org/debian/pool/main/p/python2.7/libpython2.7-stdlib_2.7.13-2_amd64.deb",
)

# Node
new_http_archive(
    name = "nodejs",
    build_file = "BUILD.nodejs",
    sha256 = "c6a60f823a4df31f1ed3a4044d250e322f2f2794d97798d47c6ee4af9376f927",
    strip_prefix = "node-v6.10.3-linux-x64/",
    type = "tgz",
    url = "https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.gz",
)

# For the debug image
http_file(
    name = "busybox",
    executable = True,
    sha256 = "8d7a4ac8629db62457447673fd5e3ae857bdf5c4bda46f6c2abc53b3315f4bf5",
    url = "https://busybox.net/downloads/binaries/1.21.1/busybox-x86_64",
)


# init
http_file(
    name = "tini",
    executable = True,
    sha256 = "1c9974f0be89de306811fcea2f675e8f0d43349b963913f81cfae571c558a59e",
    url = "https://github.com/krallin/tini/releases/download/v0.15.0/tini-static-muslc-amd64",
)

# Docker rules.
git_repository(
    name = "io_bazel_rules_docker",
    commit = "5ce5f4c1bf1ee6458d24c4178a2707111723d5af",
    remote = "https://github.com/bazelbuild/rules_docker.git",
)

load(
    "@io_bazel_rules_docker//docker:docker.bzl",
    "docker_repositories",
)

docker_repositories()

git_repository(
    name = "runtimes_common",
    commit = "3d73b4fecbd18de77588ab5eef712d50f34f601e",
    remote = "https://github.com/GoogleCloudPlatform/runtimes-common.git",
)

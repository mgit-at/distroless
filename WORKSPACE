workspace(name = "distroless")

git_repository(
    name = "io_bazel_rules_go",
    remote = "https://github.com/bazelbuild/rules_go.git",
    tag = "0.5.5",
)

load("@io_bazel_rules_go//go:def.bzl", "go_repositories", "go_repository")

go_repositories()

# Go dependencies of the update_workspace helper tool

# "golang.org/x/crypto/openpgp"
go_repository(
    name = "org_golang_x_crypto",
    commit = "847319b7fc94cab682988f93da778204da164588",
    importpath = "golang.org/x/crypto",
)

# "github.com/knqyf263/go-deb-version"
go_repository(
    name = "com_github_knqyf263_go_deb_version",
    commit = "9865fe14d09b1c729188ac810466dde90f897ee3",
    importpath = "github.com/knqyf263/go-deb-version",
)

# "github.com/stapelberg/godebiancontrol"
go_repository(
    name = "com_github_stapelberg_godebiancontrol",
    commit = "4376b22fb2c4dfda546c972f686310af907819b2",
    importpath = "github.com/stapelberg/godebiancontrol",
)

# To build the par file for the helper program in deb_loader
git_repository(
    name = "subpar",
    remote = "https://github.com/google/subpar",
    tag = "1.0.0",
)

# use the deb_loader ruleset
load(
    "//deb_loader:deb_loader.bzl",
    "deb_packages",
    "deb_repositories",
)

deb_repositories()

# The Debian jessie archive signing key
# Source: https://ftp-master.debian.org/keys.html
# Full fingerprint: 126C 0D24 BD8A 2942 CC7D F8AC 7638 D044 2B90 D010
http_file(
    name = "jessie_archive_key",
    # It is highly recommended to use the sha256 hash of the key file to make sure it is untampered
    sha256 = "e42141a829b9fde8392ea2c0e329321bb29e5c0453b0b48e33c9f88bdc4873c5",
    urls = ["https://ftp-master.debian.org/keys/archive-key-8.asc"],
)

load(
    "//package_manager:package_manager.bzl",
    "package_manager_repositories",
    "dpkg_src",
    "dpkg_list",
)

package_manager_repositories()

dpkg_src(
    name = "debian_jessie",
    arch = "amd64",
    distro = "jessie",
    sha256 = "142cceae78a1343e66a0d27f1b142c406243d7940f626972c2c39ef71499ce61",
    snapshot = "20170821T035341Z",
    url = "http://snapshot.debian.org/archive",
)

dpkg_src(
    name = "debian_jessie_backports",
    arch = "amd64",
    distro = "jessie-backports",
    sha256 = "eba769f0a0bcaffbb82a8b61d4a9c8a0a3299d5111a68daeaf7e50cc0f76e0ab",
    snapshot = "20170821T035341Z",
    url = "http://snapshot.debian.org/archive",
)

dpkg_list(
    name = "package_bundle",
    packages = [
        "libc6",
        "ca-certificates",
        "openssl",
        "libssl1.0.0",
        "netbase",
        "tzdata",

        #java
        "zlib1g",
        "libgcc1",
        "libstdc++6",
        "openjdk-8-jre-headless",

        #python
        "libpython2.7-minimal",
        "python2.7-minimal",
        "libpython2.7-stdlib",

        #dotnet
        "libcurl3",
        "libgssapi-krb5-2",
        "libicu52",
        "liblttng-ust0",
        "libunwind8",
        "libuuid1",
        "liblzma5",
    ],
    sources = [
        "@debian_jessie//file:Packages.json",
        "@debian_jessie_backports//file:Packages.json",
    ],
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

# Node
new_http_archive(
    name = "nodejs",
    build_file = "BUILD.nodejs",
    sha256 = "c6a60f823a4df31f1ed3a4044d250e322f2f2794d97798d47c6ee4af9376f927",
    strip_prefix = "node-v6.10.3-linux-x64/",
    type = "tgz",
    url = "https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.gz",
)

# dotnet
new_http_archive(
    name = "dotnet",
    build_file = "BUILD.dotnet",
    sha256 = "69ecad24bce4f2132e0db616b49e2c35487d13e3c379dabc3ec860662467b714",
    type = "tgz",
    url = "https://download.microsoft.com/download/5/F/0/5F0362BD-7D0A-4A9D-9BF9-022C6B15B04D/dotnet-runtime-2.0.0-linux-x64.tar.gz",
)

# For the debug image
http_file(
    name = "busybox",
    executable = True,
    sha256 = "b51b9328eb4e60748912e1c1867954a5cf7e9d5294781cae59ce225ed110523c",
    url = "https://busybox.net/downloads/binaries/1.27.1-i686/busybox",
)

# Docker rules.
git_repository(
    name = "io_bazel_rules_docker",
    commit = "cdd259b3ba67fd4ef814c88070a2ebc7bec28dc5",
    remote = "https://github.com/bazelbuild/rules_docker.git",
)

load(
    "@io_bazel_rules_docker//docker:docker.bzl",
    "docker_repositories",
    "docker_pull",
)

# Used to generate java ca certs.
docker_pull(
    name = "debian8",
    # From tag: 2017-09-11-115552
    digest = "sha256:6d381d0bf292e31291136cff03b3209eb40ef6342fb790483fa1b9d3af84ae46",
    registry = "gcr.io",
    repository = "google-appengine/debian8",
)

docker_repositories()

# Have the py_image dependencies for testing.
load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

# Have the java_image dependencies for testing.
load(
    "@io_bazel_rules_docker//java:image.bzl",
    _java_image_repos = "repositories",
)

_java_image_repos()

# Have the go_image dependencies for testing.
load(
    "@io_bazel_rules_docker//go:image.bzl",
    _go_image_repos = "repositories",
)

_go_image_repos()

git_repository(
    name = "runtimes_common",
    remote = "https://github.com/GoogleCloudPlatform/runtimes-common.git",
    tag = "v0.1.0",
)

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

# use the deb_packages ruleset
load("//deb_packages:deb_packages.bzl", "deb_packages")

# The Debian jessie archive signing key
# Source: https://ftp-master.debian.org/keys.html
# Full fingerprint: 126C 0D24 BD8A 2942 CC7D F8AC 7638 D044 2B90 D010
http_file(
    name = "jessie_archive_key",
    # It is highly recommended to use the sha256 hash of the key file to make sure it is untampered
    sha256 = "e42141a829b9fde8392ea2c0e329321bb29e5c0453b0b48e33c9f88bdc4873c5",
    urls = ["https://ftp-master.debian.org/keys/archive-key-8.asc"],
)

deb_packages(
    name = "debian_jessie_amd64",
    arch = "amd64",
    distro = "jessie",
    distro_type = "debian",
    mirrors = [
        "http://deb.debian.org/debian",
    ],
    packages = {
        "ca-certificates": "pool/main/c/ca-certificates/ca-certificates_20141019+deb8u3_all.deb",
        "libc6": "pool/main/g/glibc/libc6_2.19-18+deb8u10_amd64.deb",
        "libcurl3": "pool/main/c/curl/libcurl3_7.38.0-4+deb8u5_amd64.deb",
        "libgcc1": "pool/main/g/gcc-4.9/libgcc1_4.9.2-10_amd64.deb",
        "libgssapi-krb5-2": "pool/main/k/krb5/libgssapi-krb5-2_1.12.1+dfsg-19+deb8u2_amd64.deb",
        "libicu52": "pool/main/i/icu/libicu52_52.1-8+deb8u5_amd64.deb",
        "libjemalloc1": "pool/main/j/jemalloc/libjemalloc1_3.6.0-3_amd64.deb",
        "liblttng-ust0": "pool/main/u/ust/liblttng-ust0_2.5.0-1_amd64.deb",
        "liblzma5": "pool/main/x/xz-utils/liblzma5_5.1.1alpha+20120614-2+b3_amd64.deb",
        "libpython2.7-minimal": "pool/main/p/python2.7/libpython2.7-minimal_2.7.9-2+deb8u1_amd64.deb",
        "libpython2.7-stdlib": "pool/main/p/python2.7/libpython2.7-stdlib_2.7.9-2+deb8u1_amd64.deb",
        "libssl1.0.0": "pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb",
        "libstdc++6": "pool/main/g/gcc-4.9/libstdc++6_4.9.2-10_amd64.deb",
        "libunwind8": "pool/main/libu/libunwind/libunwind8_1.1-3.2_amd64.deb",
        "libuuid1": "pool/main/u/util-linux/libuuid1_2.25.2-6_amd64.deb",
        "netbase": "pool/main/n/netbase/netbase_5.3_all.deb",
        "openssl": "pool/main/o/openssl/openssl_1.0.1t-1+deb8u6_amd64.deb",
        "python2.7-minimal": "pool/main/p/python2.7/python2.7-minimal_2.7.9-2+deb8u1_amd64.deb",
        "tzdata": "pool/main/t/tzdata/tzdata_2017b-0+deb8u1_all.deb",
        "zlib1g": "pool/main/z/zlib/zlib1g_1.2.8.dfsg-2+b1_amd64.deb",
    },
    packages_sha256 = {
        "ca-certificates": "bd799f47f5ae3260b6402b1fe19fe2c37f2f4125afcd19327bf69a9cf436aeff",
        "libc6": "0a95ee1c5bff7f73c1279b2b78f32d40da9025a76f93cb67c03f2867a7133e61",
        "libcurl3": "5604a7ab988a30c82ab5cc9498bbf17f58719bdfc891ee65267be7019a5ca842",
        "libgcc1": "a1402290165e8d91b396a33d79580a4501041e92bdb62ef23929a0c207cd9af9",
        "libgssapi-krb5-2": "06e83f850bb4271de223623f1f44cc2956390a289d0e94a150ba4fbb97ac8b4a",
        "libicu52": "8882b51b67973d23719f078dec907a81fe3ec6675954dfa6b6784d0547cc66db",
        "libjemalloc1": "caeeb8b60bee0b732de25b6091dae30d58f1cebcf7467900525d5d266d4360ba",
        "liblttng-ust0": "f9f5d7d6c70fca493c8e194a4f945c64a1fbcdc47c75a5008224f91d80456d6c",
        "liblzma5": "a60661f537292862f9bfa4c421df5af126da5032def818a0bf38c49b68656328",
        "libpython2.7-minimal": "916e2c541aa954239cb8da45d1d7e4ecec232b24d3af8982e76bf43d3e1758f3",
        "libpython2.7-stdlib": "cf1c9dfc12d6cfd42bb14bfb46ee3cec0f6ebc720a1419f017396739953b12c5",
        "libssl1.0.0": "0fc777d9242fd93851eb49c4aafd22505048b7797c0178f20c909ff918320619",
        "libstdc++6": "f1509bbabd78e89c861de16931aec5988e1215649688fd4f8dfe1af875a7fbef",
        "libunwind8": "1ea086c1544aa3e04067af1b6d2d065562480a8a5959fbf707557481136eb680",
        "libuuid1": "ab7821a322a6c137eb7b36297eba11a5d2a3d3c27e480a238ff4538898570fb9",
        "netbase": "3979bdd40c5666ef9bf71a5391ba01ad38e264f2ec96d289993f2a0805616dd3",
        "openssl": "41613658b4e93ffaa7de25060a4a1ab2f8dfa1ee15ed90aeac850a9bf5a134bb",
        "python2.7-minimal": "c89199f908d5a508d8d404efc0e1aef3d9db59ea23bd4532df9e59941643fcfb",
        "tzdata": "4d754d06cf94b3991f333d076461efe7f8e905462be9663b4b616fd75233c09d",
        "zlib1g": "b75102f61ace79c14ea6f06fdd9509825ee2af694c6aa503253df4e6659d6772",
    },
    pgp_key = "jessie_archive_key",
)

deb_packages(
    name = "debian_jessie_backports_amd64",
    arch = "amd64",
    distro = "jessie-backports",
    distro_type = "debian",
    mirrors = [
        "http://deb.debian.org/debian",
    ],
    packages = {
        "openjdk-8-jre-headless": "pool/main/o/openjdk-8/openjdk-8-jre-headless_8u131-b11-1~bpo8+1_amd64.deb",
        "redis-server": "pool/main/r/redis/redis-server_3.2.8-2~bpo8+1_amd64.deb",
    },
    packages_sha256 = {
        "openjdk-8-jre-headless": "11c592e237549d74bda30875979c2a937588667d10307c7c14047b8d03f5718a",
        "redis-server": "660fb0b07fad591fe6b44f547c0314b91f2fa1515375c51d7cf8be01072e1206",
    },
    pgp_key = "jessie_archive_key",
)

deb_packages(
    name = "packages",
    arch = "",
    distro = "",
    distro_type = "",
    mirrors = [],
    packages = {},
    packages_sha256 = {},
    pgp_key = "",
    # Tag this dummy rule with "manual_update" so the update script ignores it.
    # This is done because it looks for docker_build rules and thinks the "packages" part is the name of a deb_packages rule.
    # It is instead the hardcoded name of the dpkg_list rule output.
    tags = ["manual_update"],
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

# For the init image
http_file(
    name = "tini",
    executable = True,
    sha256 = "2f17cf294c64c78f36c1c9339590a95ce6e672c6a2dbdcc3c417017248acc682",
    urls = ["https://github.com/krallin/tini/releases/download/v0.16.1/tini-static-muslc-amd64"],
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

load("@io_bazel_rules_go//go:def.bzl", "go_binary", "go_library", "go_test")

go_library(
    name = "go_default_library",
    srcs = [
        "update_workspace.go",
    ],
    importpath = "github.com/GoogleCloudPlatform/distroless/tools/update_workspace",
    deps = [
        "@com_github_knqyf263_go_deb_version//:go_default_library",
        "@com_github_stapelberg_godebiancontrol//:go_default_library",
        "@org_golang_x_crypto//openpgp:go_default_library",
    ],
)

go_binary(
    name = "update_workspace",
    srcs = ["update_workspace.go"],
    importpath = "github.com/GoogleCloudPlatform/distroless/tools/update_workspace",
    visibility = ["//visibility:public"],
    deps = [
        ":go_default_library",
        "@com_github_knqyf263_go_deb_version//:go_default_library",
        "@com_github_stapelberg_godebiancontrol//:go_default_library",
        "@org_golang_x_crypto//openpgp:go_default_library",
    ],
)

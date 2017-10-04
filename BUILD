package(default_visibility = ["//visibility:public"])

# Go boilerplate
load("@io_bazel_rules_go//go:def.bzl", "go_prefix", "gazelle")

gazelle(
    name = "gazelle",
    prefix = "github.com/GoogleCloudPlatform/distroless",
)

go_prefix("github.com/GoogleCloudPlatform/distroless")

# update_workspace boilerplate
load("@distroless//tools:update_workspace.bzl", "update_workspace")

update_workspace(
    name = "update_workspace",
    pgp_keys = ["@jessie_archive_key//file"],
)

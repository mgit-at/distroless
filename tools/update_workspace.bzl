# Copyright 2017 mgIT GmbH All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

_script_content = """
BASE=$(pwd)
WORKSPACE=$(dirname $(readlink WORKSPACE))
cd "$WORKSPACE"
$BASE/{update_workspace} {args} $@
"""

def _update_workspace_script_impl(ctx):
  args = ctx.attr.args
  script_content = _script_content.format(update_workspace=ctx.file._update_workspace.short_path, args=" ".join(args))
  script_file = ctx.new_file(ctx.label.name+".bash")
  ctx.file_action(output=script_file, executable=True, content=script_content)
  return struct(
    files = depset([script_file]),
    runfiles = ctx.runfiles([ctx.file._update_workspace])
  )

_update_workspace_script = rule(
    _update_workspace_script_impl,
    attrs = {
        "args": attr.string_list(),
        "pgp_keys": attr.label_list(),
        "_update_workspace": attr.label(
            default = Label("@distroless//tools/update_workspace:update_workspace"),
            allow_single_file = True,
            executable = True,
            cfg = "host",
        ),
    },
)

def update_workspace(name, pgp_keys, **kwargs):
  script_name = name+"_script"
  _update_workspace_script(
      name = script_name,
      tags = ["manual"],
      **kwargs
  )
  native.sh_binary(
      name = name,
      srcs = [script_name],
      data = ["//:WORKSPACE"] + pgp_keys,
      tags = ["manual"],
  )

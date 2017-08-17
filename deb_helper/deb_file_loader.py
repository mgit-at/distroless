# Copyright 2017 Google Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Sample:
# """
# deb_packages(
#     name = "debian_jessie_amd64",
#     distro_type = "debian",
#     distro = "jessie",
#     architecture = "amd64",
#     packages = {
#         "libstdc++6": "pool/main/g/gcc-4.9/libstdc++6_4.9.2-10_amd64.deb",
#         "foo": "path",
#     },
#     packages_sha256 = {
#         "libstdc++6": "123456abcdef...",
#         "foo": "hash",
#     }
#     mirrors = [
#         "http://deb.debian.org",
#         "http://my.private.mirror",
#     ],
# )
# """

import argparse
import base64
import hashlib
import json
import urllib
import urlparse

parser = argparse.ArgumentParser(
    description="Downloads and validates deb packages from package sources"
)

parser.add_argument("--rule_name", action='store',
                    help='The name of the rule in the WORKSPACE file')
parser.add_argument("--distro_type", action='store',
                    help='The distribution type to use (e.g. "debian")')
parser.add_argument("--distro", action='store',
                    help='The actual distribution name (e.g. "jessie")')
parser.add_argument("--architecture", action='store',
                    help='The package architecture to use')
parser.add_argument("--packages_dict", action='store', type=json.loads,
                    help='A JSON-encoded dictionary of packages to use with the path to them as value')
parser.add_argument("--packages_sha256_dict", action='store', type=json.loads,
                    help='A JSON-encoded dictionary of packages to use with the corresponding SHA256 hash as value')
parser.add_argument("--mirrors_list", action='store', type=json.loads,
                    help='A JSON-encoded list of mirrors to use')

def download_deb(mirrorlist, deb_path, distro_type):
    success = False
    for mirror in mirrorlist:
        if distro_type == "debian":
            url = urlparse.urljoin(mirror, "/debian/")
        elif distro_type == "ubuntu":
            url = urlparse.urljoin(mirror, "/ubuntu/")
        url = urlparse.urljoin(url, deb_path)
        # get the part after the last slash
        pkgname = url.rsplit('/', 1)[-1]
        filename = base64.urlsafe_b64encode(pkgname) + ".deb"
        try:
            urllib.urlretrieve(url, "debs/" + filename)
            success = True
            break
        except:
            print "Could not load file {} from mirror {} with url {}".format(pkgname, mirror, url)
            continue
    if success:
        return filename
    else:
        raise Exception("Could not load file {} from any supplied mirror".format(pkgname))


def verify_deb(filename, sha256_hash, package_name):
    sha256 = hashlib.sha256()
    with open("debs/" + filename, 'rb') as f:
        for block in iter(lambda: f.read(65536), b''):
            sha256.update(block)
    actual_hash = sha256.hexdigest()
    if not actual_hash.lower() == sha256_hash.lower():
        raise Exception("Hashes of downloaded file {} do not match. Got {}, expected {}".format(package_name, actual_hash, sha256_hash))


def main(args):
    """ A tool for downloading deb packages """
    debian = False
    ubuntu = False
    if args.distro_type.lower() == "debian":
        debian = True
    elif args.distro_type.lower() == "ubuntu":
        ubuntu = True
    else:
        raise NotImplementedError("Only debian and ubuntu are supported in distro_type at the moment")

    package_to_rule_dict = {}
    for package in args.packages_dict:
        if package not in args.packages_sha256_dict:
            raise Exception("Package {} was not found in packages_sha256.".format(package))
        # download deb
        if debian:
            filename = download_deb(args.mirrors_list, args.packages_dict[package], "debian")
        elif ubuntu:
            filename = download_deb(args.mirrors_list, args.packages_dict[package], "ubuntu")
        verify_deb(filename, args.packages_sha256_dict[package], package)
        # add to package_to_rule_dict
        package_to_rule_dict[package] = "@" + args.rule_name + "//debs:" + filename

    with open("debs/deb_packages.bzl", "w") as packagefile:
        packagefile.write(args.rule_name + " = " + json.dumps(package_to_rule_dict))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

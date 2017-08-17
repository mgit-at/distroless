#!/usr/bin/env python

# TBD:
# python update_workspace.py add <packagename>/<packagename=version> <rulename>

# DONE:
# python update_workspace.py --update|-u all|<rulename>
# For now, only prints to stdout and doesn't change WORKSPACE files
# Also some paths are still hardcoded (e.g. the directory for temp files called "foo" in curdir)

import argparse
import gzip
import hashlib
import json
import os
import subprocess
import urllib
import urlparse

# python-apt
import apt_pkg

parser = argparse.ArgumentParser(
    description="Adds and updates deb_packages rules in WORKSPACE files"
)

parser.add_argument("-u", "--update", action='store',
                    help='Name of the deb_packages rule that should be updated. If the name is "all", all rules will be updated.')


def get_packages_file(arch, distro_type, distro, mirrors_list):
    release_done = False
    for mirror in mirrors_list:
        # download
        # TODO: use tempfile module
        release_url = urlparse.urljoin(mirror, "/" + distro_type + "/dists/" + distro + "/Release")
        release_gpg_url = urlparse.urljoin(mirror, "/" + distro_type + "/dists/" + distro + "/Release.gpg")
        try:
            urllib.urlretrieve(release_url, "foo/Release")
        except:
            print "Could not load Release file from mirror {} with url {}".format(mirror, release_url)
            continue
        try:
            urllib.urlretrieve(release_gpg_url, "foo/Release.gpg")
            release_done = True
            break
        except:
            print "Could not load Release.gpg file from mirror {} with url {}".format(mirror, release_gpg_url)
            continue
    if not release_done:
        raise Exception("Could not download Release files from any of the supplied mirrors")
    # TODO:
    # Verify integrity of Release file with gpg
    with apt_pkg.TagFile('foo/Release') as tagfile:
        for section in tagfile:
            components = section["Components"].split()
            for component in components:
                sha256 = section["SHA256"].split()
                for index, entry in enumerate(sha256):
                    if entry.endswith(component + "/binary-" + arch + "/Packages.gz"):
                        package_path = sha256[index]
                        package_sha256 = sha256[index - 2]
                package_done = False
                for mirror in mirrors_list:
                    package_url = urlparse.urljoin(mirror, "/" + distro_type + "/dists/" + distro + "/" + package_path)
                    try:
                        urllib.urlretrieve(package_url, "foo/Packages.gz.tmp")
                        package_done = True
                        break
                    except:
                        print "Could not load Release.gpg file from mirror {} with url {}".format(mirror, release_gpg_url)
                        continue
                if not package_done:
                    raise Exception("Could not download Packages file from any of the supplied mirrors")
                # verify sha256 of Packages.gz
                sha256 = hashlib.sha256()
                with open("foo/Packages.gz.tmp", 'rb') as f:
                    for block in iter(lambda: f.read(65536), b''):
                        sha256.update(block)
                actual_hash = sha256.hexdigest()
                if not actual_hash.lower() == package_sha256.lower():
                    raise Exception("Hashes of downloaded Packages.gz file do not match. Got {}, expected {}".format(actual_hash, package_sha256))
                # Append Package files together
                with gzip.open("foo/Packages.gz.tmp", "rb") as packagesfile:
                    with open("foo/Packages.all", "ab") as allfile:
                        allfile.write(packagesfile.read())


def get_distro_type(rule_name, workspace_contents):
    # run buildozer:
    # buildozer 'print distro_type' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "print distro_type", "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    result = str(stdout).strip().lower()
    return result


def get_distro(rule_name, workspace_contents):
    # run buildozer:
    # buildozer 'print distro' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "print distro", "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    result = str(stdout).strip().lower()
    return result


def get_architecture(rule_name, workspace_contents):
    # run buildozer:
    # buildozer 'print architecture' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "print architecture", "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    result = str(stdout).strip().lower()
    return result


def get_mirrors(rule_name, workspace_contents):
    # run buildozer:
    # buildozer 'print mirrors' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "print mirrors", "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    # Ignore [] characters in output
    result = str(stdout)[1:-2].split()
    return result


def get_all_packages(rule_name, workspace_contents):
    # run buildozer:
    # buildozer 'print packages' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "print packages", "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    # the results currently include curly braces and quotes
    # package names are the ones ending in a colon
    # TODO:
    # this should become easier once buildozer can handle dicts
    # Alternatively treat this as json and use a json parser?
    # Good enough for now.
    result = [entry[1:-2] for entry in str(stdout).split() if entry.endswith(":")]
    if len(result) == 1:
        # single packages have a " character prepended
        result[0] = result[0][1:]
    return result


def get_all_rule_names(workspace_contents):
    # run buildozer:
    # buildozer 'print name' -:%deb_packages <WORKSPACE
    process = subprocess.Popen(["buildozer", "print name", "-:%deb_packages"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    result = str(stdout).split()
    # TODO: Make it possible to ignore some of these e.g. with a tag
    return result


def write_distro_to_rule(distro, rule_name, workspace_contents):
    # run buildozer
    # buildozer 'set distro DISTRONAME_GOES_HERE' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", 'set distro "{}"'.format(distro), "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    return stdout


def write_packages_to_rule(dictionary, rule_name, workspace_contents):
    # run buildozer
    # buildozer 'set packages {"foo":"bar","foo2":"baz"}' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "set packages {}".format(json.dumps(dictionary, separators=(",",":"), sort_keys=True)), "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    return stdout


def write_packages_sha256_to_rule(dictionary, rule_name, workspace_contents):
    # run buildozer
    # buildozer 'set packages_sha256 {"foo":"bar","foo2":"baz"}' -:RULENAME_GOES_HERE <WORKSPACE
    process = subprocess.Popen(["buildozer", "set packages_sha256 {}".format(json.dumps(dictionary, separators=(",",":"), sort_keys=True)), "-:{}".format(rule_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout = process.communicate(input=workspace_contents)[0]
    return stdout


def main(args):
    apt_pkg.init_system()
    with open("WORKSPACE", "r") as workspacefile:
        workspace_contents = workspacefile.read()
    if args.update == "all":
        rule_names = get_all_rule_names(workspace_contents)
    else:
        rule_names = [args.update]

    for rule in rule_names:
        package_names = get_all_packages(rule, workspace_contents)
        package_names_dict = {}
        for package_name in package_names:
            if "=" in package_name:
                name, version = package_name.split("=")
                package_names_dict[name] = version
            else:
                package_names_dict[package_name] = "latest"
        distro_type = get_distro_type(rule, workspace_contents)
        distro = get_distro(rule, workspace_contents)
        arch = get_architecture(rule, workspace_contents)
        mirrors_list = get_mirrors(rule, workspace_contents)
        get_packages_file(arch, distro_type, distro, mirrors_list)
        packages = {}
        packages_sha256 = {}
        package_dict = {}
        with apt_pkg.TagFile('foo/Packages.all') as packagesfile:
            for section in packagesfile:
                if section["Package"] in package_dict:
                    package_dict[section["Package"]].append(section)
                else:
                    package_dict[section["Package"]] = [section]
        for package in package_dict:
            if package in package_names_dict:
                version_list = []
                for version in package_dict[package]:
                    version_list.append(version["Version"])
                version_to_use = None
                if package_names_dict[package] == "latest":
                    latest_version = version_list[0]
                    for entry in version_list:
                        compare_version = entry
                        res = apt_pkg.version_compare(latest_version, compare_version)
                        if res < 0:
                            latest_version = compare_version
                    version_to_use = latest_version
                else:
                    version_to_use = package_names_dict[package]
                for version in package_dict[package]:
                    if apt_pkg.version_compare(version["Version"], version_to_use) == 0:
                        packages[package] = version["Filename"]
                        packages_sha256[package] = version["SHA256"]
        os.remove("foo/Packages.all")
        workspace_contents = write_packages_to_rule(packages, rule, workspace_contents)
        workspace_contents = write_packages_sha256_to_rule(packages_sha256, rule, workspace_contents)
        # Workaround, since buildozer seems to run buildifier over its input , but not its output if "-buildifier" is not set.
        # This formats the outputs nicely
        workspace_contents = write_distro_to_rule(distro, rule, workspace_contents)

    # Maybe just keep it like this, so it is easier to do a diff with the current WORKSPACE file and redirect the output as needed?
    print workspace_contents

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

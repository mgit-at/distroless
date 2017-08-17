load(":debs.bzl", "deb_packages")

def deb_loader():
  # py_binary can't be used here, so use an "external" artifact storage for now
  native.http_file(
      name = "deb_file_loader",
      url = ("http://localhost/deb_file_loader.par"),
      executable = True,
      sha256 = "5fb59242f2c6c9043fbed67f062b0120a9047ddb3fd2eff56df8b014d162b3a5",
  )

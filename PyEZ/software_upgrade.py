#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

PACKAGE = "/var/tmp/junos-openconfig-x86-32-0.0.0.9.tgz"

def progress_callback(dev, report):
  print(report)
  
if __name__ == '__main__':
  dev = Device(host="172.25.11.1", user="lab", password="lab123")
  dev.open()
  sw = SW(dev)
  ok = sw.install(package=PACKAGE, no_copy=True, validate=False,
                  progress=progress_callback)
  dev.close()
  # Note: sw.install() does not perform a reboot, use sw.reboot() if needed

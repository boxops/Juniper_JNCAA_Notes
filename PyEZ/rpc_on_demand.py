#!/usr/bin/python

from jnpr.junos import Device

if __name__ == '__main__':
  dev = Device(host='172.25.11.1', user='lab', passwd='lab123')
  dev.open()
  route_lxml_element = dev.rpc.get_route_information(table="inet.0")
  list_of_routes = route_lxml_element.findall('.//rt')
  for route in list_of_routes:
    print("Route: {} Protocol: {}".format(route.findtext('rt-destination').strip(), 
                                          route.findtext('rt-entry/protocol-name').strip()))
  dev.close()

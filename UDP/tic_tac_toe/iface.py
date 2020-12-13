#!/usr/bin/env python3
"""
from scapy.all import get_if_list, get_if_hwaddr

def get_if():
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break
    if not iface:
        print ("Cannot find eth0 interface")
        exit(1)
    return iface
"""
"""
import netifaces as ni
#print(ni.interfaces())
for i in ni.interfaces():
    print(i)
    if "eth0" in i:
        iface = i
        break
"""
import netifaces as ni
def get_ipv4_eth0(hostname):
    ipv4 = None
    string = None
    iface = hostname + "-eth0"
    for i in ni.interfaces():
        if (iface) in i :
            ipv4 = ni.ifaddresses(iface)[2][0]['addr']
            string = iface
            break
        elif "lo" in i :
            ipv4 = ni.ifaddresses('lo')[2][0]['addr']
            string = "lo"
    if not ipv4 :
        print ("Cannot find + " + iface + " or lo interface")
        exit(1)
    return ipv4 , string

ipv4 , string = get_ipv4_eth0("h1")
print (string , ipv4)

#ni.ifaddresses('eth0')
#print(ni.ifaddresses.__doc__)
"""
Obtain information about the specified network interface.

Returns a dict whose keys are equal to the address family constants,
e.g. netifaces.AF_INET, and whose values are a list of addresses in
that family that are attached to the network interface.
"""
# for the IPv4 address of eth0
#ni.ifaddresses('eth0')[2][0]['addr']
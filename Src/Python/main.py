import json
import urllib.request
import ipaddress
import pprint

URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'


def GetAwsIpList():
    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as res:
        ip_ranges = json.load(res)
    return ip_ranges


def SelectionIpType(ip_ranges):
    result = []
    for prefix in ip_ranges["prefixes"]:
        if prefix["ip_prefix"] is not None:
            result.append(prefix)
    return result


def CheckIpRange(ip_ranges, search_ip):
    for prefix in ip_ranges:
        if ipaddress.IPv4Address(search_ip) in ipaddress.IPv4Network(prefix["ip_prefix"]):
            pprint.pprint(prefix)
            break
    else:
        print("Not Match")


if __name__ == "__main__":
    search_ip = "15.230.105.56"
    ip_ranges = GetAwsIpList()
    # print(SelectionIpType(ip_ranges))
    CheckIpRange(SelectionIpType(ip_ranges), search_ip)

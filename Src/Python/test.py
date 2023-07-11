import ipaddress
import pprint
aws_ip_list = {
    "syncToken": "1689105189",
    "createDate": "2023-07-11-19-53-09",
    "prefixes": [
        {
            "ip_prefix": "13.34.37.64/27",
            "region": "ap-southeast-4",
            "service": "AMAZON",
            "network_border_group": "ap-southeast-4"
        },
        {
            "ip_prefix": "13.34.65.64/27",
            "region": "il-central-1",
            "service": "AMAZON",
            "network_border_group": "il-central-1"
        },
        {
            "ip_prefix": "15.230.221.0/24",
            "region": "us-east-1",
            "service": "AMAZON",
            "network_border_group": "us-east-1"
        }
    ]
}


def convert(ip_list):
    """
    docstring
    """
    pass


if __name__ == "__main__":
    search_ip = "13.34.65.89"
    for prefix in aws_ip_list["prefixes"]:
        if ipaddress.IPv4Address(search_ip) in ipaddress.IPv4Network(prefix["ip_prefix"]):
            pprint.pprint(prefix)
            break
    print("END")

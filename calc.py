import sys
import ipaddress

ip_file = sys.argv[1]


class Calculator:
    """Calculate takes a file with ip and classify them"""

    def __init__(self, filename) -> None:
        self.filename = filename

    def classify_ip(self):
        with open(self.filename, encoding="utf-8") as ip:
            for lines in ip:
                ip_address = ipaddress.ip_address(lines.removesuffix("\n"))

                if ip_address.is_private:
                    print(f"{ip_address} is a private address")
                elif ip_address.is_global:
                    print(f"{ip_address} is a public address")
                elif ip_address.is_loopback:
                    print(f"{ip_address} is a loopback address")
                elif ip_address.is_reserved:
                    print(f"{ip_address} is a reserved address")
                else:
                    print("check your ip address")


ips = Calculator("ips.txt")
ips.classify_ip()

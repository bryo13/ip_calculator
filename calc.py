import sys
import re

ip_file = sys.argv[1]


class Calculator:
    """Calculate takes a file with ip and classify them"""

    def __init__(self, filename) -> None:
        self.filename = filename

    def private_or_public_ip(self,ip):
        private_regex = re.compile(
            r"^(10|172\.16|192\.168)\.([0-9]{1,3}\.){2}([0-9]{1,3})$"
        )
        public_regex = re.compile(
            r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$"
        )
        loopnack_regex = re.compile(r"^(127)\.([0-9]{1,3}\.){2}([0-9]{1,3})$")

        if private_regex.match(ip):
            print(f"{ip} - private ip")
            return "private"
        elif public_regex.match(ip):
            print(f"{ip} - public ip")
            return "public"
        elif loopnack_regex.match(ip):
            print(f"{ip} - loopback ip")
            return "loopback"
        else:
            print("check your ip address!")
            return "error"

    def read_ips(self):
        with open(self.filename, encoding="utf-8") as ip:
            for lines in ip:
                self.private_or_public_ip(lines)


ips = Calculator("ips.txt")
ips.read_ips()

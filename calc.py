import sys

ip_file = sys.argv[1]

class Calculator:
    def __init__(self,filename) -> None:
        self.filename = filename

    def read_ips(self):
        with open(self.filename,encoding="utf-8") as ip:
            for lines in ip:
                print(lines)


ips = Calculator(ip_file)
ips.read_ips()
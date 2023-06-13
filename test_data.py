import random
import threading


class TestData:
    def __init__(self) -> None:
        pass

    def generate_ips(self) -> str:
        first_octate = random.randint(1, 223)
        second_octate = random.randint(1, 255)
        third_octate = random.randint(1, 255)
        fourth_octate = random.randint(1, 255)
        return f"{first_octate}.{second_octate}.{third_octate}.{fourth_octate}"

    def write_file(self, filename) -> None:
        lines = 1
        with open(filename, "a") as f:
            while lines <= 13:
                ip_ranges = self.generate_ips()
                f.write(f"{ip_ranges}\n")
                lines += 1


if __name__ == "__main__":
    td = TestData()
    thread = threading.Thread(target=td.write_file, args=("ips.txt",))
    thread.start()
    thread.join()
    print(f"file - ips.txt created and populated")

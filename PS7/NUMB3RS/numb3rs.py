import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        a, b, c, d = ip.strip().split(".")
        if int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()

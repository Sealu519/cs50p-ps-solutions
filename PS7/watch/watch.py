import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(
            r"^<iframe(.+)? src=\"(https?://)?(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"(?:.+)?></iframe>$", s):
        return f"https://youtu.be/{match.group(4)}"
    return None


if __name__ == "__main__":
    main()

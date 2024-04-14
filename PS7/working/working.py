import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s):
        h1, m1, ap1, h2, m2, ap2 = match.groups()
        if m1 is None and m2 is None:
            m1, m2 = 0, 0
        elif m1 is None and m2 is not None:
            m1 = 0
        elif m1 is not None and m2 is None:
            m2 = 0
        h1, m1, h2, m2 = map(int, [h1, m1, h2, m2])

        if ap1 == 'AM' and h1 == 12:
            h1 = 0
        elif ap1 == 'PM' and h1 != 12:
            h1 += 12

        if ap2 == 'AM' and h2 == 12:
            h2 = 0
        elif ap2 == 'PM' and h2 != 12:
            h2 += 12

        if 0 <= h1 <= 23 and 0 <= h2 <= 23 and 0 <= int(m1) <= 59 and 0 <= int(m2) <= 59:
            return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()

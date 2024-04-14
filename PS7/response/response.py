import re
import validators


def main():
    print(valid(input("What's your email address? ")))


def valid(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


main()
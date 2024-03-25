# In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted
# with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100.
# The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer
# accepts.
#
# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with
# “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(x):
    if x[0].lower() != 'h':
        return 100
    elif x.startswith('hello'):
        return 0
    else:
        return 20


if __name__ == "__main__":
    main()
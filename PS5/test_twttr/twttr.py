# Just setting up my twttr
#
# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user
# for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted
# in uppercase or lowercase.

# tweet = input("Input: ").strip()
# print("Output: ", end="")
# for i in tweet:
#     if i.lower() in ["a", "e", "i", "o", "u"]:
#         print("", end="")
#     else:
#         print(i, end="")

def main():
    tweet = input("Input: ").strip()
    print(f"Output: {shorten(tweet)}", end="")


def shorten(tweet):
    non_vowel = []
    for i in tweet:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            non_vowel.append("")
        else:
            non_vowel.append(i)
    return "".join(non_vowel)


if __name__ == "__main__":
    main()

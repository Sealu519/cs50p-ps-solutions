# # Vanity Plates
# #
# # In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
# # with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
# #
# # “All vanity plates must start with at least two letters.” “… vanity plates may contain a maximum of 6 characters (
# # letters or numbers) and a minimum of 2 characters.” “Numbers cannot be used in the middle of a plate; they must
# # come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The
# # first number used cannot be a ‘0’.” “No periods, spaces, or punctuation marks are allowed.” In plates.py,
# # implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
# # or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program
# # per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s
# # will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per
# # requirement).
#
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_start_valid(s) and is_length_valid(s) and is_order_valid(s) and is_content_valid(s):
        return True
    else:
        return False


def is_start_valid(s):
    if s[:2].isalpha():
        return True
    else:
        return False


def is_length_valid(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def is_order_valid(s):
    numbers = range(0, 10)
    non_zero = range(1, 10)
    num_counter = 0
    zero_counter = 0
    for i in s:
        if i.isdigit():
            if i == '0':
                zero_counter = zero_counter + 1
                num_counter = num_counter + 1
            else:
                num_counter = num_counter + 1

    if s.isalpha():
        return True
    elif s[-1].isalpha():
        return False
    elif num_counter == 1:
        if int(s[-1]) in non_zero:
            return True
        else:
            return False
    elif num_counter == 2:
        if s[-2].isdigit() and int(s[-2]) in non_zero:
            return True
        else:
            return False
    elif num_counter == 3:
        if s[-3:-1].isdigit() and int(s[-2]) in numbers and int(s[-3]) in non_zero:
            return True
        else:
            return False


def is_content_valid(s):
    flag = True
    invalid_symbol = [" ", ",", ".", "!", "?"]
    for i in s:
        if i in invalid_symbol:
            flag = flag and False
        else:
            flag = flag and True
    return flag


main()

# Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)


def last_two_char_str(str):
    if len(str) > 2:
        return str[-2:] * 4
    else:
        return "invail input"


str = input("Enter a string: ")
print(last_two_char_str(str))

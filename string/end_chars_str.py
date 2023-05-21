# program to get a string made of the first 2 and last 2 characters of a given string


def end_char_str(str):
    str = input("Enter a string: ")
    if len(str) < 2:
        return ""
    else:
        return str[:2] + str[-2:]


print(end_char_str(str))

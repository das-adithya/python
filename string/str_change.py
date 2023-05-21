# Python program to change a given string to a newly string where the first and last chars have been exchanged


def str_change(str):
    str = input("Enter a string: ")
    if len(str) <= 1:
        return str
    else:
        return str[-1:] + str[1:-1] + str[0]


print(str_change(str))

# program to calculate the length of a string


def str_len(str):
    str = input("Enter a string: ")
    len = 0
    for i in str:
        len += 1
    return len


print(str_len(str))

#program to remove characters that have odd index values in a given string

def remove_odd_index(str):
    str=input("Enter a string: ")
    return str[::2]
print(remove_odd_index(str))
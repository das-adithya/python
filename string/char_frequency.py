# program to count the number of characters (character frequency) in a string.


def char_count(str):
    str = input("Enter a string: ")
    freq = {}
    keys = freq.keys()
    for i in str:
        if i in keys:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


print(char_count(str))

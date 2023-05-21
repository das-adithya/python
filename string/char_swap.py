# program to get a single string from two given strings, separated by a space and swap the first two characters of each string


def char_swap(str1, str2):
     
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2
str1 = input("Enter 1st str: ")
str2 = input("Enter 2nd str: ")
print(char_swap(str1,str2))
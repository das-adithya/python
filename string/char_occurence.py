#program to get a string from a given string where all occurrences of its first char
#have been changed to '$', except the first char itself


def char_occurence(str):
    str=input("Enter a string: ")
    char=str[0]
    new_str=char+str[1:].replace(char,'$')
    return new_str
    
print(char_occurence(str))    

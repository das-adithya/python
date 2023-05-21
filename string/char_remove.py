#program to remove the nth index character from a nonempty string


def char_remove(str,index):
    if len(str)>index>=0:
        return str[:index]+str[index+1:]
    else:
        return str
str=input("Enter a string: ")
index=int(input("Enter char index to remove: "))
print(char_remove(str,index))

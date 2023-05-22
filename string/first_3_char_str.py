#Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string

def three_char_str(str):
    return str[:3] if len(str)>3 else str

str=input("Enter a string:")
print("result:",(three_char_str(str))) 
    
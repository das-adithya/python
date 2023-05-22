# function to insert a string in the middle of a string


def insert_middle_string(orginal_str, str_to_insert):
   
    return orginal_str[:2]+' '+str_to_insert+' '+orginal_str[2:]

orginal_str = input("Enter a string: ")
str_to_insert = input("Enter string to be inserted int the middle: ")

print(insert_middle_string(orginal_str,str_to_insert))

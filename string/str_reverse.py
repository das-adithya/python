#function to reverse a string if its length is a multiple of 4

def reverse_str(str):
    if len(str)%4==0:
        return str[::-1] 
    else:
        return str
print(reverse_str("abcdwxyz"))
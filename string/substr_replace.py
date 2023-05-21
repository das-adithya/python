# program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'


def substr_replace(str):
    str = input("Enter a str: ")
    not_index = str.find("not")
    poor_index = str.find("poor")
    if not_index > 0 and poor_index > 0 and not_index < poor_index:
        replaced_str = str[:not_index] + "good"
        return replaced_str
    else:
        return str


print(substr_replace(str))

# Python function to create an HTML string with tags around the word(s)


def html_str(tag, word):
    html_string = f"<{tag}>{word}<{tag}/>"
    return html_string


tag = input("Enter a tag: ")
word = input("Enter a word: ")

print(html_str(tag, word))

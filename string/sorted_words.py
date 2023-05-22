# program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically)


def sorted_words(items):
    words = items.split(",")
    sorted_items = sorted(set(words))
    return sorted_items


items = input("Input comma separated sequence of words: ")

print(",".join(sorted_words((items))))

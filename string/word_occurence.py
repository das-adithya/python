# program to count the occurrences of each word in a given sentence


def word_occurence(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


sentence = input("Enter a sentence: ")

print(word_occurence(sentence))

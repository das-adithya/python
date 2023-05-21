# Python function that takes a list of words and return the longest word and the length of the longest one
def longest_word(list):
    long_word=""
    long_lenth=0
    
    for word in list:
        if len(word)>long_lenth:
         long_word=word
         long_lenth=len(word)        
    return long_word,long_lenth
list=['apple','orange','grape','adithyadas','athuldas']
result=(longest_word(list))
print("longest word = ",result[0])
print("length of the word = ",result[1])
            
#python function that takes a list of words and returns the length of the longest one.
def longest_word(word_list):
    len_word = []
    for i in word_list:
        len_word.append((len(i),i))
    len_word.sort()
    return len_word[-1][0], len_word[-1][1]
output = longest_word(["Insight","Workshop","Bootcamps"])
print("The longest word is: ", output[1])
print("The length of this word is: ", output[0])

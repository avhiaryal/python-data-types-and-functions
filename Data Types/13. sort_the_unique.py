#python program that accepts a comma separated sequence of words as input and prints
#the unique words in sorted form (alphanumerically)

word_sequence = input ("Enter the sequence of words separated by comma : ")
separated_words = [word for word in word_sequence.split(",")]
print(",".join(sorted(list(set(separated_words))))) 

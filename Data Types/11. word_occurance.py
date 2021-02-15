#python program to count the occurrences of each word in a given sentence.
def occ_words(str):
    count = dict()
    words = str.split()
    
    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
        
    return count

print (occ_words('I am taking the python-django training in the Insight Workshop Bootcamp'))


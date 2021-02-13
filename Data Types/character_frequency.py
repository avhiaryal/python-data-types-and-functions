# this program count the number of characters (character frequency) in a string
sample_string ="google.com"

frequency = {}

for i in sample_string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print ("frequency of all characters in string "+sample_string+" is :\n" + str(frequency))

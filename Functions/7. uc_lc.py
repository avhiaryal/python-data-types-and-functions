#python function to accepts a string and calculate the number of 
#uppercase and lowercase letters
def string(st):
    count={"upper_case":0, "lower_case":0}
    for i in st:
        if i.isupper():
            count["upper_case"]+=1
        elif i.islower():
            count["lower_case"]+=1
        else:
            pass    
    
    print("The given string is : ", st)
    print("Number of upper case letters: ", count["upper_case"])
    print("Number of lower case letters: ", count["lower_case"])
string('The quick Brow Fox')
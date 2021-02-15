# python program to check whether a given key already exists in a dictionary

dict1 = {1:10, 2:20, 3:30, 4:40, 5:50}
def key(x):
    if x in dict1:
        print('Key already exist in dictionary')
    else:
        print('Key is not present in the dictionary')

key(4)
key(6)

#python program to get a single string from two
#given strings, separated by a space and swap the
#first two characters of each string.

def swap(a,b):
    a_update = b[:2] + a[2:]
    b_update = a[:2] + b[2:]
    
    return a_update + ' ' + b_update
print(swap('abc','xyz'))

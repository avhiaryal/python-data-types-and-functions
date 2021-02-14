#python function to check whether a number is in a given range

def is_in_range(num):
    if num in range(11,32):
        print(" The number %s is in the range "%str(num))
    else:
        print(" The number %s is out of the range "%str(num),)
        
is_in_range(33)
is_in_range(29)
    
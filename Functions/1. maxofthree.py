#python function to find the max of three numbers
# using max function
# a = 15
# b = 5
# c = 10
# print(max(a,b,c))

def maximum(a,b,c):
    if (a>=b) and (a>=c):
        max = a
    elif (b>=a) and (b>=c):
        max = b
    else:
        max = c
    return max

a=15
b=5
c=10
print(maximum(a,b,c))
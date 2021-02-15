# python program to generate and print a dictionary that contain a number
# (between 1 and n) in the form (x,x*x)

num = int(input("Enter a number : "))
dict1 = dict()

for a in range(1, num+1):
    dict1[a]=a*a

print(dict1)
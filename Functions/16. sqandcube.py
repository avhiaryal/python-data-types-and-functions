# python program to square and cube every number in a given list of integer using lambda

list1 = [1,2,3,4,5,6,7,8,9]
print("List of integers: ",list1)
square = list(map(lambda x:x**2, list1))
cube = list(map(lambda x:x**3, list1))
print("the square of numbers in the list is: ", square)
print("the cube of numbers in the list is: ", cube)


# python program to filter a list of integers using lambda

list1 = [1,2,3,4,5,6,7,8,9]
print("List of integers: ", list1)
#filtering to get odd numbers
print("Extracting odd numbers from the list: ")
odd_numbers = list(filter(lambda x:x%2 !=0, list1))
print(odd_numbers)

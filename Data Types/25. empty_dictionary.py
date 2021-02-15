# python program to check whether all dictionaries in a list are empty or not.
list1 = [{},{},{}]
list2 = [{1,2},{},{}]

print(all(not d for d in list1))
print(all(not d for d in list2))

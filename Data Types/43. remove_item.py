# python program to remove an item from a tuple

tuple1 = 'i','n','s','i','g','h','t'
print (tuple1)

#since tuple are immutable, we cannot remove elements from it
#using different method
list1= list(tuple1)
list1.remove('g')
tuple1 = tuple(list1)
print(tuple1)



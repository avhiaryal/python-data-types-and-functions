# python program to find the intesection of two given arrays using lambda

array1 = [1,2,3,7,8,9]
array2 = [2,3,4,6,7,8]
print("Arrays before intersections : ", array1,array2)
intersection = list(filter(lambda x:x in array1, array2))
print ("The intersection of these arrays is: ", intersection)

#python program to multiply all the items in a dictionary.


dict1 = {'a':6,'b':12,'c':18}
count = 1
for key in dict1:
    count = count * dict1[key]

print(count)
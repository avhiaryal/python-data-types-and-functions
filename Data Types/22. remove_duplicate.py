# python program to remove duplicated from a list.
given_list = [1,2,3,2,1,4,5,6,4,7,8,5,8,9,1]

duplicates = set()
unique = []
for x in given_list:
    if x not in duplicates:
        unique.append(x)
        duplicates.add(x)
        
print(duplicates)

def largest_num(list):
    maximum = list[0]
    for x in list:
        if x > maximum:
            maximum = x
    return maximum
print(largest_num([1,2,3,6,12,5]))
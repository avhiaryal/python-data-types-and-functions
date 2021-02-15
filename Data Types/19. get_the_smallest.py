def smallest_num(list):
    minimum = list[0]
    for x in list:
        if x < minimum:
            minimum = x
    return minimum
print(smallest_num([-5,2,3,6,12,5]))
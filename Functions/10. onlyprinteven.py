#python program to print the even numbers from the given list
def num_list(list):
    numbers = []
    for num in list:
        if num % 2 == 0:
            numbers.append(num)
    return numbers
print(num_list([1,2,3,4,5,6,7,8,9]))

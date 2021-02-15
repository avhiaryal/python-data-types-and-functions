# python program to create fibonacci series upto n using lambda
from functools import reduce

num=int(input("Enter the amount of number in series: "))

fibonacci = lambda a: reduce(lambda x, _: x+[x[-1]+x[-2]], range (a-2), [0,1])

print("Fibonacci series upto "+str(num),fibonacci(num))


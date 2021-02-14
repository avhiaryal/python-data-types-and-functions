#python program to remove the nth index character from a nonempty string.
def rmchar(str,n):
    start = str[:n]
    end = str[n+1:]
    return start + end
print(rmchar('Insight',1))
print(rmchar('Insight',4))

# python program to get a list, sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples.

def list(n):
     return n[-1]

def list_sort(tuples):
    return sorted(tuples, key=list)

print (list_sort([(2,5),(1,2),(4,4),(2,3),(2,1)]))


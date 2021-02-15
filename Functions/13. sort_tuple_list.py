age = [('ram', 20),('hari',25),('arjun',18),('deepak',23),('avhi',24)]
print("Age of students :", age)
age.sort(key=lambda x:x[1])
print("Age in sorted format :", age)

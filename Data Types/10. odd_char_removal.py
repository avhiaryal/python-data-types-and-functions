#python program to remove the characters which have odd index values of a given string.
def string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

print(string('insight'))
print(string('workshop'))
print(string('bootcamp'))
#python program to get a string from a given string where all
#occurances of its first char have been changed to '$', except the first char itself.

def change_occ(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]
    
    return str
print (change_occ('restart'))
# python program to find if a given string starts with a given character using lambda

check = input("Enter the string to check : ")
if_start = lambda x: True if x.startswith('I') else False
print(if_start(check))



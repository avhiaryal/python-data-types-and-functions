# python program to check whether a given string is number or not using lambda

check_num = lambda a: a.replace('.','',1).isdigit()
print(check_num('abcd'))

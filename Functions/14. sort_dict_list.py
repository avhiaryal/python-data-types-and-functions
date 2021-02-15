# python program to sort a list of dictionaries using lambda
student_description = [{'name':'avhi', 'age':23, 'education':'4. bachelor'},
                       {'name':'rahul', 'age':15, 'education':'2. slc'},
                       {'name':'sabin', 'age':17, 'education':'3. +2'},
                       {'name':'deepak', 'age':27, 'education':'5. masters'},
                       {'name':'rohit', 'age':9, 'education':'1.primary'}]
print('Decription of Students :',student_description )
sort = sorted(student_description, key=lambda x:x['education'])
print("Sorting based on education: ", sort)

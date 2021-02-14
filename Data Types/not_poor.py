# pyhton program to find the first appearance of the substring 'not'
# and'poor' from the given string, if 'not' follows 'poor', replace the
# whole 'not'...'poor' substring with 'good'

def string(str):
    sbt_not = str.find('not')
    sbt_poor = str.find('poor')
    
    if sbt_poor > sbt_not and sbt_not>0 and sbt_poor>0:
        str = str.replace(str[sbt_not:(sbt_poor+4)], 'good')
        return str
    else:
        return str
print(string('The lyrics is not that poor!'))
print(string('The lyrics is poor!'))

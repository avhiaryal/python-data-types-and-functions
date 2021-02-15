def same_chacacter(words):
    count = 0
    for word in words:
        if len(word) > 1 and word [0] == word[-1]:
            count +=1
    return count

print(same_chacacter(['abc','xyz','aba','1221']))

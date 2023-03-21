def count_code(s):
    cnt = 0
    res = 0
    for i in s:
        if(i == "c" and cnt == 0):
            cnt += 1
        elif(i == "o" and cnt == 1):
            cnt += 1
        elif(cnt == 2):
            cnt += 1
        elif(i == "e" and cnt == 3):
            cnt = 0
            res += 1
        else:
            cnt = 0
    return res

print(count_code("aaacoxecoze"))
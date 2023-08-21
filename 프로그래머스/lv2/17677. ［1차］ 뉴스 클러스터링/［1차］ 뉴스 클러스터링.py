from collections import Counter

def solution(str1, str2):
    answer = 0
    low_str1 = str1.lower()
    low_str2 = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(low_str1) - 1):
        if low_str1[i].isalpha() and low_str1[i+1].isalpha():
            str1_lst.append(low_str1[i:i+2])

    for i in range(len(low_str2) - 1):
        if low_str2[i].isalpha() and low_str2[i+1].isalpha():
            str2_lst.append(low_str2[i:i+2])
                   
    intersection = list((Counter(str1_lst) & Counter(str2_lst)).elements())
    union = list((Counter(str1_lst) | Counter(str2_lst)).elements())
                   
    if len(intersection) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
    

    
    return answer
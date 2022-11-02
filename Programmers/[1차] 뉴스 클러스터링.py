# 프로그래머스 # [1차] 뉴스 클러스터링 # 2018 KAKAO BLIND RECRUITMENT

from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower() # initialize both string to lower case
    # make multiples sets for each string
    multiple_set_1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    multiple_set_2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    # if there isn't any string sets, return immediately
    if not multiple_set_1 and not multiple_set_2: return 65536
    # use Counter in order to get the exact count for each element in each multiple_set
    counter_1 = Counter(multiple_set_1)
    counter_2 = Counter(multiple_set_2)
    # get the all elements by union both counter's keys
    elems = set(counter_1.keys()).union(set(counter_2.keys()))
    union_cnt, intersection_cnt = 0, 0 
    for elem in elems:
        num1, num2 = counter_1[elem], counter_2[elem]
        union_cnt += max(num1, num2) # max of num1, num2 for union
        intersection_cnt += min(num1, num2) # min of num1, num2 for union
    return int((intersection_cnt / union_cnt) * 65536) 
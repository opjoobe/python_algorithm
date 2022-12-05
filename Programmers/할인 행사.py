# 프로그래머스 # 할인 행사

from collections import defaultdict
def solution(want, number, discount):
    def status_check():
        for v in status.values():
            if v != 0: return False
        return True
    status = defaultdict(int)
    answer, flag = 0, False
    for item, need in zip(want, number):
        status[item] -= need
    for idx, new_sale_item in enumerate(discount):
        if idx < 10:
            status[new_sale_item] += 1
            if idx == 9 and status_check() == True: 
                flag = True
                answer += 1
            continue
        end_sale_item = discount[idx - 10]
        if new_sale_item != end_sale_item:
            status[new_sale_item] += 1
            status[end_sale_item] -= 1
            flag = status_check()
        if flag: answer += 1    
    return answer
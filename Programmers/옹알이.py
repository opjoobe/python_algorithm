# 프로그래머스 # 옹알이

def solution(babbling):
    answer = 0
    for now in babbling:
        flag = True
        for i, word in enumerate(['aya', 'ye', 'woo', 'ma'], 1):
            now = now.replace(word, str(i))
        for check in ('11','22','33','44'):
            if check in now:
                flag = False
                break
        if flag and now.isdigit():
            answer += 1
    return answer
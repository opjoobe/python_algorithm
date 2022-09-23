# 프로그래머스 # 구명보트

from collections import deque
def solution(people, limit):
    # 무거운 사람부터 보트에 태우기
    people.sort(reverse = True)
    q = deque(people)
    cnt = 0
    while q:
        cnt += 1
        now = q.popleft()
        if q and q[-1] + now <= limit: # 아직 사람이 남아있고, 가장 가벼운 사람도 태울 수 있다면
            q.pop() # 현재 보트에 같이 태운다
    return cnt
            
''' 
정렬 후에, 가장 무거운 사람부터 차례대로 보트에 태우기 시작한다.
그리고 태웠을 때, 만약 가장 가벼운 사람이 같이 탈 수 있다면, 같이 태운다.
같이 태울 수 없다면 그냥 가장 무거운 사람만 보트에 태우고, 다음 무거운 사람을 보트에 태운다.
'''
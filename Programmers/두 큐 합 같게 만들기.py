# 프로그래머스 # 두 큐 합 같게 만들기

# 풀이 1 : 성공한 풀이
from collections import deque
def solution(queue1, queue2):
    # 작으면 가져오고 # 크면 보내자
    # queue1 = deque(queue1)
    dq1, dq2, sum_dq1, sum_dq2 = deque(queue1), deque(queue2), sum(queue1), sum(queue2)
    if sum_dq1 == sum_dq2: return 0
    target, rest = divmod(sum_dq1 + sum_dq2, 2)
    if rest: return -1
    cnt = 0
    while dq1 and dq2:
        if sum_dq1 == target: 
            return cnt
        elif sum_dq1 < target:
            adder = dq2.popleft()
            dq1.append(adder)
            sum_dq1 += adder
        else:
            sum_dq1 -= dq1.popleft()
        if dq1 == queue1:
            break
        cnt += 1
    return -1

# 풀이 2: 시간초과 난 풀이 (복기용)
from collections import deque, defaultdict
def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    target, rest = divmod(sum1 + sum2, 2)
    if sum1 == sum2: return 0
    if rest: return -1
    q = deque([[queue1, queue2, sum1, sum2]])
    visited = defaultdict(list)
    visited[sum1].append(queue1)
    visited[sum2].append(queue2)
    flag = False
    cnt = 0
    
    while q and not flag:
        cnt += 1
        next_q = deque()
        while q:
            q1, q2, s1, s2 = q.popleft()
            if q1:
                new_s1, new_s2 = s1 - q1[0], s2 + q1[0]
                if new_s1 == target:
                    flag = True
                    break
                left_q1, left_q2 = q1[1:], q2 + [q1[0]]            
                if left_q1 not in visited[new_s1]:
                    visited[new_s1].append(left_q1)
                    next_q.append([left_q1, left_q2, new_s1, new_s2])
            if q2:
                new_s1, new_s2 = s1 + q2[0], s2 - q2[0]
                if new_s1 == target:
                    flag = True
                    break
                right_q1, right_q2 = q1 + [q2[0]], q2[1:]
                if right_q1 not in visited[new_s1]:
                    visited[new_s1].append(right_q1)
                    next_q.append([right_q1, right_q2, new_s1, new_s2])
        q = next_q
    return cnt if flag else -1
# 프로그래머스 # 롤케이크 자르기

from collections import Counter, defaultdict
def solution(topping):
    if len(topping) == 1: return 0
    # 철수가 모든 토핑을 다 갖고 시작해서, 하나씩 동생한테 빼준다고 설정
    chulsoo = Counter(topping)
    chulsoo_set, brother_set = set(chulsoo.keys()), set()
    answer = 0
    while topping:
        flavor = topping.pop()
        brother_set.add(flavor)
        # 철수가 어떤 토핑을 모두 동생한테 내주었다면, set에서 제거
        chulsoo[flavor] -= 1
        if chulsoo[flavor] == 0:
            chulsoo_set.remove(flavor)
        chulsoo_topping_cnt, brother_topping_cnt = len(chulsoo_set), len(brother_set)
        # 철수보다 동생이 더 많은 가짓수를 가지게 된다면, 더 이상 비교의 의미가 없으니 종료
        if chulsoo_topping_cnt < brother_topping_cnt:
            break
        # 철수와 동생이 동일한 갯수의 토핑을 들고 있게 된다면, 공평하게 자르는 방법 수로 세주기
        if chulsoo_topping_cnt == brother_topping_cnt:
            answer += 1
    return answer
# 프로그래머스 # 멀쩡한 사각형

# 풀이 1: 처음 풀이
'''
테스트 4, 테스트 17에서 오류가 계속 났음.
밑에 주석처리 해놓은 new_y를 구할 때, 기울기를 먼저 구하고 거기에 x좌표를 곱해주는 방식으로 계산했다.
하지만 프로그래밍 언어 특성상 소수점 처리가 완벽하지 않은 경우가 있다. 이 경우도 아무래도 나눗셈을 먼저 하다보니 미세한 오차가 발생한듯.
따라서 곱셈을 우선 해주고 나서 나눗셈을 진행하도록 괄호를 묶어주었더니 해결되었다.
1.1 + 0.1 == 1.2 가 False가 나온다는 사례를 몸소 체험할 수 있었다. 항상 유의해야지..
'''
import math
def solution(w,h):
    if w == h: return w * w - w
    if w > h: w, h = h, w
    wh_gcd = int(math.gcd(w,h))
    small_w, small_h = w // wh_gcd, h // wh_gcd
    cnt = 0
    before_y = small_h
    for x in range(1, small_w + 1):
        # new_y = - ((small_h / small_w) * x) + small_h
        new_y = - ((small_h * x) / small_w) + small_h
        cnt += (before_y - int(math.floor(new_y)))
        before_y = int(math.ceil(new_y))
    return (w * h) - (cnt * wh_gcd)

# 풀이 2: 정말 간단한 풀이......
'''분할정복으로 나눠지는 작은 사각형에서 멀쩡하지 않은 사각형을 가로로 small_w개, 세로로 small_h개를 색칠해보면, 오직 하나만 겹친다. 
즉 small_w + small_h - 1 개를 사용하지 못하게 되는 것이다.
따라서 작은 사각형이 최대공약수만큼 만들어진다는 점에서, 전체적으로는 (w + h - 최대공약수) 만큼이 쓰지 못하게 되는 것이다.
'''
import math
def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))
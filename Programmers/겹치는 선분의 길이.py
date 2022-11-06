# 프로그래머스 # 겹치는 선분의 길이

def solution(lines):
    red, green, blue = lines
    # assume that a dot stands for the sentence with length 1 (dot ~ dot + 1)
    rg = list(range(max(red[0], green[0]), min(red[1], green[1])))
    gb = list(range(max(blue[0], green[0]), min(blue[1], green[1])))
    br = list(range(max(blue[0], red[0]), min(blue[1], red[1])))
    rgb = set(rg+gb+br)
    return len(rgb)
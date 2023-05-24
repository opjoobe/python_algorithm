# 프로그래머스 # 바탕화면 정리

def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '.':
                continue
            lux, luy, rdx, rdy = min(lux, i), min(luy, j), max(rdx, i + 1), max(rdy, j + 1)
    return [lux, luy, rdx, rdy]
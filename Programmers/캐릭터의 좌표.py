# 프로그래머스 # 캐릭터의 좌표

def solution(keyinput, board):
    direction = {"left":(-1, 0), "right":(1, 0), "up":(0, 1), "down":(0, -1)}
    col, row = board[0] // 2, board[1] // 2 # 가로 세로
    x, y = 0, 0
    for key in keyinput:
        dx, dy = direction[key]
        x, y = min(max(-col, x + dx), col), min(max(-row, y + dy), row)
    answer = [x,y]
    return answer
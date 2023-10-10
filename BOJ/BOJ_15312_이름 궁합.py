# BOJ # 15312 # 이름 궁합

import sys
input = sys.stdin.readline
man = input().strip()
woman = input().strip()
strokes = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]))
base = []
for m_char, w_char in zip(man, woman):
    base.append(strokes[m_char])
    base.append(strokes[w_char])

while len(base) > 2:
    new_base = []
    for idx in range(len(base) - 1):
        new_base.append((base[idx] + base[idx + 1]) % 10)
    base = new_base
print(''.join([str(num) for num in base]))
    
    
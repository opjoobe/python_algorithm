# 프로그래머스 # 외계어 사전

from collections import Counter
def solution(spell, dic):
    spell_set = set(spell)
    for word in dic:
        word_dict = Counter(word)
        if word_dict.most_common(1)[0][1] == 1 and set(word_dict.keys()) == spell_set:
            return 1
    return 2
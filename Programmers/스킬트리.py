# 프로그래머스 # 스킬트리

def solution(skill, skill_trees):
    skill = skill[::-1]
    skill_set = set(skill) # 'in' 연산을 O(1)에 하기 위해 선언
    answer = 0
    for skill_tree in skill_trees:
        skill_stack = list(skill)
        for now in skill_tree:
            if now in skill_set:
                if skill_stack[-1] != now: break
                skill_stack.pop()
        else:
            answer += 1
    return answer
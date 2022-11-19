# 프로그래머스 # 영어가 싫어요
import re
def solution(numbers):
    numdict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    return int(''.join([numdict[numstr] for numstr in re.findall('one|two|three|four|five|six|seven|eight|nine|zero', numbers)]))

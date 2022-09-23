# 프로그래머스 # 전화번호 목록

# 풀이 1 (해시 활용 풀이)
def solution(phone_book):
    D = {}
    for phone in phone_book:
        D[phone] = 1
    for phone in phone_book:
        now = ''
        for digit in phone[:-1]:
            now += digit
            if now in D:
                return False
    return True

'''
문제 조건에 따라 "각 전화번호의 길이는 1 이상 20 이하" 이기에, 
해시를 쓰면 다른 전화번호랑 비교할 필요 없이 각 전화번호당 최소 0 ~ 최대 19 번만 for문을 돌며 해시를 확인하기만 하면 된다. 

반면 정렬없이 startswith나 정규표현식을 사용하는 경우, 각 i번째 전화번호 당 다른 전화번호인 전체 전화번호 갯수-i번만큼 for문을 돌아야 한다. 
phone_book의 길이 N이 최대 1,000,000 까지 가능하므로, O(N²)으로 가면 N이 커질수록 비효율적! 
'''

# 풀이 2 (해시는 아니지만, 문자열의 정렬 성질을 활용한 풀이)
def solution(phone_book):
    phone_book.sort()
    before = phone_book[0]
    for now in phone_book[1:]:
        if now.startswith(before):
            return False
        before = now
    return True
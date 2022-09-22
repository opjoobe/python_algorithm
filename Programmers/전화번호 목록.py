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

# 풀이 2 (해시는 아니지만, 문자열의 정렬 성질을 활용한 풀이)
def solution(phone_book):
    phone_book.sort()
    before = phone_book[0]
    for now in phone_book[1:]:
        if now.startswith(before):
            return False
        before = now
    return True
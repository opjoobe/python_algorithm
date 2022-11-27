# 프로그래머스 # 로그인 성공

def solution(id_pw, db):
    result = dict(db).get(id_pw[0])
    return "login" if result == id_pw[1] else "wrong pw" if result else "fail"

# 프로그래머스 # 조건에 맞는 회원수 구하기
SELECT COUNT(*) AS 'USERS'
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND AGE BETWEEN 20 AND 29

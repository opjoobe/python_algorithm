#프로그래머스 #나이 정보가 없는 회원 수 구하기

select count(user_id) as users
from user_info
where age is null

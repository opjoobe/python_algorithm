#프로그래머스 #조건에 맞는 도서 리스트 출력하기

select book_id, date_format(published_date, '%Y-%m-%d') published_date
from book
where category = '인문' and year(published_date) = 2021
order by published_date

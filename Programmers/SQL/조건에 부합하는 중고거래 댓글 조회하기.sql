# 프로그래머스 # 조건에 부합하는 중고거래 댓글 조회하기

SELECT TITLE, ugb.BOARD_ID, REPLY_ID, ugr.WRITER_ID, ugr.CONTENTS, date_format(ugr.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD ugb, USED_GOODS_REPLY ugr
WHERE ugb.BOARD_ID = ugr.BOARD_ID and ugb.CREATED_DATE like '2022-10%'
ORDER BY CREATED_DATE ASC, TITLE ASC

# 댓글이 아니라 게시글의 created_date를 기준으로 2022년 10월을 찾아주는 것이 포인트
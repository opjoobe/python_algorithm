-- 코드를 입력하세요
SELECT ugb.title, ugb.board_id, ugr.reply_id, ugr.writer_id, ugr.contents, ugr.created_date 
FROM USED_GOODS_BOARD ugb, USED_GOODS_REPLY ugr
WHERE ugb.board_id = ugr.board_id and ugb.created_date like '2022-10%'
ORDER BY ugr.created_date ASC, ugr.board_id ASC
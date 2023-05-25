-- 코드를 입력하세요
SELECT b.title,b.board_id,r.reply_id,r.writer_id,r.contents, date_format(r.created_date,'%Y-%m-%d') AS created_date from used_Goods_board b, used_goods_reply r 
    where b.board_id = r.board_id and
    date_format(b.CREATED_DATE,"%Y%m")= 202210
order by r.created_date asc, b.title asc
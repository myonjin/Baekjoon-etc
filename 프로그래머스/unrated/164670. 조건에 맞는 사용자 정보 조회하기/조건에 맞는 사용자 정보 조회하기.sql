-- 코드를 입력하세요
SELECT u.user_id, u.nickname, concat(u.city,' ',u.street_address1,' ',u.street_address2) as '전체주소', concat(LEFT(tlno,3), '-', MID(tlno,4,4),'-', RIGHT(tlno,4)) as '전화번호'
from used_goods_board b, used_goods_user u
where b.writer_id = u.user_id
GROUP BY 
    u.user_id 
HAVING 
    COUNT(*) >= 3
ORDER BY 
    u.user_id DESC;

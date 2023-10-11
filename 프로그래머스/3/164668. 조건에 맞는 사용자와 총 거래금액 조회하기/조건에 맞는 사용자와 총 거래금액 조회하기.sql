-- 코드를 입력하세요
SELECT U.USER_ID,U.NICKNAME,SUM(B.PRICE) as TOTAL_SALES FROM USED_GOODS_BOARD B JOIN USED_GOODS_USER U
on B.WRITER_ID = U.USER_ID
where B.STATUS = "DONE"
group by B.WRITER_ID
having SUM(B.PRICE) >= 700000
order by TOTAL_SALES
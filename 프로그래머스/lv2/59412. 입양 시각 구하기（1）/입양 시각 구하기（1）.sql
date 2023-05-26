-- 코드를 입력하세요
SELECT hour(DATETIME) AS HOUR, count(*) as count FROM ANIMAL_OUTS
group by hour
having hour >= 9 and hour<=19
order by hour asc
# select * from animal_outs
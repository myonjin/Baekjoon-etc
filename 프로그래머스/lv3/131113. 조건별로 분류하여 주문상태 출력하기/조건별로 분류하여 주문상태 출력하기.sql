-- 코드를 입력하세요
SELECT order_id,product_id,date_format(out_date, '%Y-%m-%d'), 
    case
        when out_date <= '2022-05-01' then '출고완료'
        when out_date > '2022-05-01' then '출고대기'
        else '출고미정'
    END AS 출고여부
from FOOD_ORDER order by order_id asc


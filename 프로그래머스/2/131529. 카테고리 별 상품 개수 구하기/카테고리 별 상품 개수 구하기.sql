-- 코드를 입력하세요
SELECT LEFT(product_code,2) AS CATEGORY,count(product_code) AS PRODUCTS FROM PRODUCT
group by LEFT(product_code,2)
order by product_CODE
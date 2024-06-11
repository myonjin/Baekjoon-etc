-- 코드를 작성해주세요
with cnt AS (
SELECT PARENT_ID AS ID, COUNT(PARENT_ID) AS CHILD_COUNT FROM ECOLI_DATA
where PARENT_ID is not null
group by PARENT_ID
order by PARENT_ID asc
    )
    
SELECT E.ID, IFNULL(C.CHILD_COUNT,0) AS CHILD_COUNT FROM ECOLI_DATA E
LEFT JOIN cnt c
on E.ID = c.ID

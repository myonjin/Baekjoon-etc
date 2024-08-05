-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
    CASE 
        WHEN LOWER(SEX_UPON_INTAKE) Like '%neutered%' THEN 'O'
        WHEN LOWER(SEX_UPON_INTAKE) Like '%spayed%' THEN 'O'
        ELSE 'X'
    END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
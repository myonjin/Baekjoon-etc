-- 코드를 작성해주세요
SELECT count(*) as FISH_COUNT FROM FISH_INFO
where Date_format(TIME,'%Y') = '2021'

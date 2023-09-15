/*
[테이블] : ANIMAL_OUTS
[나타낼 컬럼] : DATETIME(열 이름 'HOUR'), COUNT
[조회 조건] : DATETIME을 시간(0~23)으로 나누어 각 시간대별 데이터의 개수를 조회. 단, 데이터가 없어도 해당 시간대와 그 시간대의 데이터는 0으로 나와야 함.

SET @hour := -1 : 사용자 지정 변수 hour을 선언, 변수 값은 -1 (0시부터 나타내야함, 1씩 증가할거라)
@hour := @hour + 1 : ROW가 한번 지날 때마다 +1 (1씩 시간대가 증가)
WHERE @hour < 23 : 24시까지만 나타내고 종료
*/

SET @hour := -1;
SELECT (@hour := @hour + 1) as HOUR,
	(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT 
FROM ANIMAL_OUTS WHERE @hour < 23;
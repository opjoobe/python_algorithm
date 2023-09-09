# 프로그래머스 # 동명 동물 수 찾기
SELECT NAME, COUNT(name) AS 'COUNT'
FROM animal_ins
GROUP BY name
HAVING COUNT(name) >= 2
ORDER BY name

-- Display the best scores and orders descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

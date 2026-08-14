-- Write your query below
SELECT student_id, exam_id, score
FROM (SELECT student_id, exam_id, score, row_number() 
    OVER (
        PARTITION BY student_id ORDER BY score DESC, exam_id ASC
    ) AS label
    FROM exam_results
)
WHERE label = 1;
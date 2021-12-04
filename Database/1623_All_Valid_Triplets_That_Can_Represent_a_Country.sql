select s1.student_name as member_A, 
       s2.student_name as member_B,
       s3.student_name as member_C
from SchoolA as s1 join SchoolB as s2 on s1.student_id != s2.student_id and s1.student_name != s2.student_name
                   join SchoolC as s3 on s3.student_id != s2.student_id and s3.student_id != s1.student_id and 
                                         s3.student_name != s2.student_name and s3.student_name != s1.student_name;

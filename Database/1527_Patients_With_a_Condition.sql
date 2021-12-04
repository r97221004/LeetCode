select *
from Patients
where conditions regexp "^DIAB1.*" or conditions regexp ".* DIAB1.*";
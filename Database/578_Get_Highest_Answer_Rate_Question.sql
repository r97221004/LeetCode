select question_id as survey_log
from SurveyLog
group by question_id
order by ifnull(sum(action='answer')/sum(action='show'), 0) desc, question_id
limit 1;

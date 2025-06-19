'''
2 Problem 2 : Students and Examinations (https://leetcode.com/problems/students-and-examinations/ )
'''

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    res = students.merge(subjects, how='cross')
    df = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
    df = res.merge(df, how='left', on=['student_id','subject_name'])
    df['attended_exams']= df['attended_exams'].fillna(0).astype(int)
    return df[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(['student_id', 'subject_name']) 
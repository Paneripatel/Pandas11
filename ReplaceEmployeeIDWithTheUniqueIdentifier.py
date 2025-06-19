'''
Pandas11

1 Problem 1 : Replace Employee ID with the Unique Identifier( https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)
'''

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employees, employee_uni, how='left', on='id')
    return res[['unique_id', 'name']]
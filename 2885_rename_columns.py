import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    columns_to_rename = {
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    }
    return students.rename(columns=columns_to_rename)


import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df_data = {"student_id": [], "age": []}
    for student_id, age in student_data:
        df_data["student_id"].append(student_id)
        df_data["age"].append(age)
    return pd.DataFrame(df_data)
    

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_df = animals.query("weight > 100")
    return filtered_df.sort_values(by="weight", ascending=False)[["name"]]


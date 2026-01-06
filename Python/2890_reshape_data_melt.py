import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    value_vars = ["quarter_1", "quarter_2", "quarter_3", "quarter_4"]
    return pd.melt(
        report,
        id_vars=["product"], value_vars=value_vars,
        var_name="quarter", value_name="sales"
    )
    

import pandas as pd

def filter_data(df, start_date, end_date, state_filter):
    mask = (df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)
    if state_filter != "All":
        mask &= (df["state"] == state_filter)
    return df.loc[mask]

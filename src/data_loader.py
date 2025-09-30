import pandas as pd

def load_data(path="data/dummy_data.csv"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df

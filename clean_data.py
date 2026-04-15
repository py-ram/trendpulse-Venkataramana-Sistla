import pandas as pd

def clean_data():
    df = pd.read_json("data/hn_data.json")

    df = df[['title', 'score', 'by', 'time', 'url']]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.dropna()

    df.to_csv("data/clean_hn_data.csv", index=False)

    return df

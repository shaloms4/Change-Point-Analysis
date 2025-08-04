import pandas as pd

def load_event_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df.columns = ['Event', 'Date', 'Description']
    df['Date'] = pd.to_datetime(df['Date'])
    return df

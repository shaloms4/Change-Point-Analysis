import pandas as pd

def load_oil_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df.columns = ['Date', 'Price']
    df['Date'] = pd.to_datetime(df['Date'])  # Let pandas infer the format
    df = df.sort_values('Date').reset_index(drop=True)
    return df
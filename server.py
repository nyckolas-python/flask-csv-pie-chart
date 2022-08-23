import pandas as pd


u_path = 'test_dataset.csv'

def csv_df(u_path: str):
    
    try:
        df = pd.read_csv(u_path)
        return df
    except:
        pass
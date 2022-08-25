import pandas as pd
from datetime import datetime as dt

u_path = 'input/test_dataset.csv'
class DataFrame():
    pass

def csv_df(u_path: str) -> DataFrame:
    try:
        df = pd.read_csv(u_path)
        df.index = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df = df.groupby(by=[pd.Grouper(freq='M'), 'Country']).agg({'Target': 'sum'}).reset_index()
        df.sort_values(by='Date', inplace=True)
        
        return df

    except Exception as ex:
        print(ex)

def df_data_set(df: DataFrame) -> dict:
    try:
        data_set = {dt.strftime(k,'%B %Y') : g.Target.to_dict() for k, g in df.set_index('Country').groupby('Date')}
        
        return data_set
    
    except Exception as ex:
        print(ex)

def get_data_all_months() -> dict:
    try:
        dfc = df.groupby(by=['Date']).agg({'Target': 'sum'}).reset_index()
        dfc = dfc.set_index('Date').to_dict().get('Target')
        all_months ={dt.strftime(k,'%B %Y') : v for k,v in dfc.items()}
        
        return all_months
    
    except Exception as ex:
        print(ex)

def get_data_one_month(data_set: dict, label: str) -> dict:
    try:
        data = data_set.get(label)

        return {'data': list(data.values()), 'labels': list(data.keys()), 'month': label}

    except Exception as ex:
        print(ex)

df = csv_df(u_path)
data_set = df_data_set(df)
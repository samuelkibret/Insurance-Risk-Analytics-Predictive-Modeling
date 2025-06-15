import pandas as pd

def load_insurance_data(filepath):
    df = pd.read_csv(filepath, sep='|')
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])

    return df
def load_claims_data(filepath):
    df = pd.read_csv(filepath, sep='|')
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    df['ClaimAmount'] = df['ClaimAmount'].astype(float)
    return df
import pandas as pd
from sklearn.preprocessing import StandardScaler

from app.preprocessors.preprocessor_loader import load_preprocessor

def preprocess_data(data):
    preprocessor = load_preprocessor()
    #scaler = StandardScaler()

    df = pd.DataFrame([data.dict()])

    df = rename_columns(df)

    df = new_features(df)

    df = delete_columns(df)
    
    df = preprocessor.transform(df)
    
    #df_processed = scaler.fit_transform(df)
    
    return df

def rename_columns(df:pd.DataFrame):
    
    df.rename(columns={"stFlrSF": "1stFlrSF"}, inplace=True)
    df.rename(columns={"ndFlrSF": "2ndFlrSF"}, inplace=True)
    df.rename(columns={"SsnPorch": "3SsnPorch"}, inplace=True)

    return df

def new_features(df:pd.DataFrame):

    df['totalFSF'] = df['1stFlrSF'] + df['2ndFlrSF'] + df['BsmtFinSF1'] + df['BsmtFinSF2']
    df['ageHouse'] = df['YrSold'] - df['YearBuilt']
    df['overalMult'] = df['OverallQual'] * df['OverallCond']
    df['garageMult'] = df['GarageArea'] * df['GarageCars']
    df['totalPorch'] = df['OpenPorchSF'] + df['WoodDeckSF'] + df['EnclosedPorch'] + df['3SsnPorch'] + df['ScreenPorch']
    df['totalBath'] = df['BsmtFullBath'] + df['BsmtHalfBath'] / 2 + df['FullBath'] + df['HalfBath'] / 2
    df['totalAreaSF'] = df['TotalBsmtSF'] + df['GrLivArea']

    return df

def delete_columns(df:pd.DataFrame):

    df = df.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'TotalBsmtSF', 'GrLivArea', 'OverallQual', 
                          'OverallCond', 'YrSold', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'BsmtFinSF1', 'BsmtFinSF2', 
                          'BsmtFullBath', 'FullBath', 'BsmtHalfBath', 'HalfBath', 'OpenPorchSF', '3SsnPorch', 
                          'EnclosedPorch', 'ScreenPorch', 'WoodDeckSF', 'GarageArea', 'GarageCars', 'PoolArea', 
                          'GarageYrBlt'])

    return df
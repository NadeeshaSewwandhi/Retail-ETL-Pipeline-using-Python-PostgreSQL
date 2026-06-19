import pandas as pd 

def extract_data():
    features_df = pd.read_csv(r'E:\new practicals\Retail_ETL_Pipeline\Data\Features_dataset.csv')
    sales_df = pd.read_csv(r'E:\new practicals\Retail_ETL_Pipeline\Data\sales_dataset.csv')
    store_df = pd.read_csv(r'E:\new practicals\Retail_ETL_Pipeline\Data\stores_dataset.csv')

    print('features dataset')
    print(features_df.head())
    print(features_df.dtypes)

    print('sales dataset')
    print(sales_df.head())
    print(sales_df.dtypes)

    print('store dataset')
    print(store_df.head())
    print(store_df.dtypes)

    return features_df, sales_df, store_df
from clean_data import *
from fa_functions import *

import pandas as pd
import statistics
from statistics import mode

# Create data frame with the factorial analysis per item (used for Dimensions)
def item_corr(df, name):
    lis = drop_nn(df).idxmax(axis=1)
    #lis = [e.idxmax() if e.max() >= 0.3 else f'{e.idxmax()} saturation < 0.3' for i,e in drop_nn(f_an_t).iterrows()]
    datf = pd.DataFrame()
    datf['item#'] = df['item#'].to_numpy()
    datf[name] = lis
    return datf.set_index('item#')

# Create item dataframe for each dimension (used for Facets)
def fac_corr_df(df, dfv, dfv_col):
    lis = []
    dfv = drop_nn(dfv)
    df = drop_nn(df)
    for e in range(len(dfv)):
        if dfv.iloc[e][dfv_col] == dfv.iloc[e].max():
            lis.append('i'+str(e+1))
    return df[lis]

# Add item factorial info to info dataframe
def add_info(info_df, df):
    tot = info_df.merge(df, left_index=True, right_index=True, how='outer')
    return tot

# Add info if the actual dim and the estimated im are diferent
def dim_err(row):
    if row['Dimension'] == row['fa_dim']:
        val = 0
    elif row['Dimension'] != row['fa_dim']:
        val = 1
    return val

def fac_err(row):
    if row['Facet'] == row['fa_facet']:
        val = 0
    elif row['Facet'] != row['fa_facet']:
        val = 1
    return val

# Identify Dimensions and Facets
def mod_dim(dim, df):
    lis = [df.iloc[i]['Dimension'] for i,e in df.iterrows() if df.iloc[i]['f_dimension'] == f'{dim}']
    try:
        return mode(lis)
    except:
        return f"Dimension not accurate enough"
    
def mod_fac(dim, df):
    lis = [df.iloc[i]['Facet'] for i,e in df.iterrows() if df.iloc[i]['f_facet'] == f'{dim}']
    try:
        return mode(lis)
    except:
        return f"Facet not accurate enough"

# Create a df per dimansion with all the items that need to be revised
def get_dim_df(df, df_err, dim):
    if dim in set(list(df['Dimension'])):
        dff = df.loc[df['Dimension'] == str(dim)].drop(columns = ['dim_error','fac_error'])
        return dff.loc[dff['fa_dim'] == df_err.loc[dim].idxmax()]

# Get all items that need to be revised
def get_it_df(df):
    dff = df.loc[(df['dim_error'] == 1)]
    return dff

#======= NOT USED, YET =======#
# Define item satuartion
def low_saturation(an_df):
    it_lis = []
    dim_lis = []
    for i,e in drop_nn(an_df).iterrows():
        if e.max() <= 0.3:
            it_lis.append(an_df.iloc[i]['item#'])
            dim_lis.append(f'{e.idxmax()} saturation < 0.3')
    datf = pd.DataFrame()
    datf['item#'] = it_lis
    datf['low_sat'] = dim_lis
    return datf.set_index('item#')
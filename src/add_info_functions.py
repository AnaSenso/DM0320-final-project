from fa_functions import *

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
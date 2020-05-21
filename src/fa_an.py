from src.fn_add_info import *
from src.fn_fa import *

import seaborn as sns
import pandas as pd
import os

def an_inf(df,an):
    print('** ANALYZING DATA ... **')
    df.reset_index(inplace=True)
    df['fa_dim'] = df['f_dimension'].apply(lambda x: mod_dim(x,df))
    df['fa_facet'] = df['f_facet'].apply(lambda x: mod_dim(x,df))
    
    #df.drop(columns = ['f_dimension', 'f_facet'], inplace=True)
        
    df['dim_error'] = df.apply(dim_err ,axis=1)
    df['fac_error'] = df.apply(fac_err ,axis=1)
        
    d_error = pd.pivot_table(df, values='dim_error', index=['Dimension'], columns=['fa_dim'], aggfunc=np.sum, fill_value=0)
    dims = list(set(list(df['Dimension'])))

    if an == 'dm':
        print('Analyzing DIMENSION data ...')
        df.drop(columns = ['f_dimension', 'f_facet'], inplace=True)
        res_df = {i:get_dim_df(df, d_error,f'{i}') for i in dims}

        print('Create and save a df for each miension error items ...')
        for e in dims:
            res_df[e].to_csv(f"output/dim_{len(df)}_an/{e}_{len(df)}_AN.csv")
            print(f"{e} dataframe has been created")
            
    elif an == 'it':
        print('Analyzing ITEM data ...')
        df.drop(columns = ['f_dimension', 'f_facet'], inplace=True)
        it_error = get_it_df(df)
        it_error.drop(columns = ['dim_error', 'fac_error'], inplace=True)
        it_error.to_csv(f"output/IT_{len(df)}_AN.csv")
        print(f"Item analysis dataframe has been created")
    
    else:
        print(f"This kind of analysis si not available, try another item (it) or dimension (dm)")
#===== PROBLEM =====#
# sns.set()
# sns.countplot(y='Dimension', hue='fa_dim', data=it_error, palette="deep")
# plt.legend(loc='lower right')
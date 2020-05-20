from add_info_functions import *
from clean_data import *
from fa_functions import *

import pandas as pd

df = infoDF300

# Create Dimension df analysis
df['fa_dim'] = df['f_dimension'].apply(lambda x: mod_dim(x,df))
df['fa_facet'] = df['f_facet'].apply(lambda x: mod_dim(x,df))

df.drop(columns = ['f_dimension', 'f_facet'], inplace=True)

df['dim_error'] = df.apply(dim_err ,axis=1)
df['fac_error'] = df.apply(fac_err ,axis=1)

d_error = pd.pivot_table(df, values='dim_error', index=['Dimension'], columns=['fa_dim'], aggfunc=np.sum, fill_value=0)

dims = list(set(list(df['Dimension'])))

res_df = {i:get_dim_df(df, d_error,f'{i}') for i in dims}

for e in dims:
    res_df[e].to_csv(f"../output/dim_an/{e}_AN.csv")

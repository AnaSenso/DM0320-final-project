from add_info_functions import *
from clean_data import *
from fa_functions import *

df = df300
info = info300
#input('What df do you want to use?')

print('PHASE 1. Validate if factorial analysisi can be performed ...')
print(perform_fa(df))

print('PHASE 2. Getting best number of factors ...')
    #===== PROBLEM =====#
    #show_num_factors(df)
    #plt.savefig('../output/best_n_factors.png')
n_fac = best_num_factors(df)

print('PHASE 3. Performing factorial analysis: to get item correlation with Dimensions ...')
f_an_t = fac_an(df, n_fac, 'dimension')
#print(f_an_t.head(3))

print('PHASE 3.1. Creating item factorial dataframe  ...')
dim_info = item_corr(f_an_t, 'f_dimension')
#print(dim_info.head(3))

print('PHASE 3.2. Adding information to info df dataframe...')
infoD = add_info(info, dim_info)
#print(infoD.head(3))

print('PHASE 4. Analize dimensions: To get item correlation with all the Facets ....')

print('PHASE 4.1. Get item correlation with all the Facets ....')
cols = list(drop_nn(f_an_t).columns)

print('- Create a dataframe for each dimension ....')
df_f = {i:fac_corr_df(df, f_an_t, f"{i}") for i in cols}
#print(df_f['dimension1'].head(3))

print('- Perform factor analysis for each Dimension to get item correlation witn Factors ...')
f_an_f = {i:fac_an(df_f[i], 6, f"{i}_facet") for i in cols}
#print(f_an_f['dimension3'].head(3))

print('PHASE 4.2. Adding information to info df dataframe ...')
infoF = {i:item_corr(f_an_f[i], f'facet_{i}'[:-1]) for i in list(drop_nn(f_an_t).columns)}
infoDF = infoD
for e in cols:
    infoDF = add_info(infoDF, infoF[e]).fillna('')

infoDF['f_facet'] = infoDF.filter(regex=("facet_")).apply(lambda x: ''.join(x.astype(str)), axis=1)
infoDF = infoDF.drop(infoDF.filter(regex=("facet_")), axis=1)

print('PHASE 5. Exporting info dataframe as csv ...')
infoDF.to_csv(f"../output/IPIP_{len(infoDF)}_AN.csv")

print(infoDF.head(3))

#from src.add_info_functions import *
#from src.clean_data import *
from src.fa import *
from src.fa_an import *
from src.parser import *
import pandas as pd


def main():
    args = parse()
    ds=args.ds
    inf=args.inf
    an=args.an
    df = pd.read_csv(f"input/clean_data/{ds}.csv").drop(columns=['Unnamed: 0'])
    info = pd.read_csv(f"input/clean_data/{inf}.csv").drop(columns=['Unnamed: 0']).set_index('item#')
    #try:
    return an_inf(fa(df, info),an)
    #except Exception:
    #    print('Dataset may not exist or is in the wrong place. For more info try main.py -h')

if __name__ == "__main__":
    main()


# print('** ANALYZING DATA ... **')

# print('Analyzing DIMENSION data ...')
# infoDF['fa_dim'] = infoDF['f_dimension'].apply(lambda x: mod_dim(x,df))
# infoDF['fa_facet'] = infoDF['f_facet'].apply(lambda x: mod_dim(x,df))

# infoDF.drop(columns = ['f_dimension', 'f_facet'], inplace=True)

# infoDF['dim_error'] = infoDF.apply(dim_err ,axis=1)
# infoDF['fac_error'] = infoDF.apply(fac_err ,axis=1)

# d_error = pd.pivot_table(infoDF, values='dim_error', index=['Dimension'], columns=['fa_dim'], aggfunc=np.sum, fill_value=0)

# dims = list(set(list(infoDF['Dimension'])))

# res_df = {i:get_dim_df(infoDF, d_error,f'{i}') for i in dims}

#     # Create a df for each miension error items
# for e in dims:
#     res_df[e].to_csv(f"../output/dim_{len(df)}_an/{e}_{len(df)}_AN.csv")

# print('Analyzing ITEM data ...')
# it_error = get_it_df(infoDF)
# it_error.to_csv(f"../output/IT_{len(df)}_AN.csv")



# #===== PROBLEM =====#
# sns.set()
# sns.countplot(y='Dimension', hue='fa_dim', data=it_error, palette="deep")
# plt.legend(loc='lower right')
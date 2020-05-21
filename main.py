from src.fa import *
from src.fa_an import *
from src.parser import *
from src.email import *
import pandas as pd


def main():
    # Get argpars
    args = parse()
    ds=args.ds
    inf=args.inf
    an=args.an

    # Read CSVs
    df = pd.read_csv(f"input/clean_data/{ds}.csv").drop(columns=['Unnamed: 0'])
    info = pd.read_csv(f"input/clean_data/{inf}.csv").drop(columns=['Unnamed: 0']).set_index('item#')
    
    # Get analysis
    res = an_inf(fa(df, info),an)
    
    # Send email
    if an == 'it':
        it_email(res)
    if an == 'dm':
        dim_email(res)

if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt
import sklearn.datasets

from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo

from clean_data import *

# Validate if it's posible to perform Factorial analysis
def perform_fa(df):
    chi_square_value,p_value=calculate_bartlett_sphericity(df)
    if p_value > 0.05:
        return(f"P-value=({p_value}). Statistically insignifincant, factorial analaisis can not be performed")
    else:
        return(f"P-value=({p_value}). Statistically significant, factorial analaisis can be performed")

def perform_fa_KMO(df):
    kmo_all,kmo_model=calculate_kmo(df)
    if kmo_model < 0.6:
        print(f"KMO=({kmo_model}). Proportion of variance NOT suitable for factor analysis")
    else:
        print(f"KMO=({kmo_model}). Proportion of variance suitable for factor analysis")

# Define best number of factors
def show_num_factors(df):
    fa = FactorAnalyzer(bounds=(0.005, 1), impute='median', is_corr_matrix=False,method='minres', n_factors=10,
                        rotation='varimax', rotation_kwargs={},use_smc=True)
    fa.fit(df)
    ev, v = fa.get_eigenvalues()
    num_f = len([e for e in ev if e > ev.mean() + 2 * ev.std()])
    res_f = len([e for e in ev if e > 1])
    plt.scatter(range(1,df.shape[1]+1),ev)
    plt.plot(range(1,df.shape[1]+1),ev)
    plt.title('Scree Plot')
    plt.xlabel('Factors')
    plt.ylabel('Eigenvalue')
    plt.grid()
    plt.show()
    return f"Best number of factors: {num_f}. Other possible factors {res_f-num_f}"

def best_num_factors(df):
    fa = FactorAnalyzer(bounds=(0.005, 1), impute='median', is_corr_matrix=False,method='minres', n_factors=10,
                        rotation=None, rotation_kwargs={},use_smc=True)
    fa.fit(df)
    ev, v = fa.get_eigenvalues()
    num_f = len([e for e in ev if e > ev.mean() + 2 * ev.std()])
    return num_f

# Perform Factorial analysis
def fac_an(df, n_factors, name):
    drop_nn(df)
    fa = FactorAnalyzer(bounds=(0.005, 1), impute='median', is_corr_matrix=False,method='minres', 
                         n_factors=n_factors, rotation='varimax', rotation_kwargs={},use_smc=True)
    fa.fit(df)
    load = pd.DataFrame.from_records(fa.loadings_, columns=([f'{name}'+str(i+1) for i in range(n_factors)]))
    load['item#']= df.columns
    return load


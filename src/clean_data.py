import pandas as pd
import numpy as np
import re

df120_1 = pd.read_csv("../input/clean_data/IPIP_120_test1.csv").drop(columns=['Unnamed: 0'])
df120_2 = pd.read_csv("../input/clean_data/IPIP_120_test2.csv").drop(columns=['Unnamed: 0'])

df300 = pd.read_csv("../input/clean_data/IPIP_20_test.csv").drop(columns=['Unnamed: 0'])
df300.index = df300.index+1

info300 = pd.read_csv("../input/clean_data/IPIP_20_desc_item.csv").drop(columns=['Unnamed: 0']).set_index('item#')
info120 = pd.read_csv("../input/clean_data/IPIP_120_desc_item.csv").drop(columns=['Unnamed: 0']).set_index('item#')

infoDF300 = pd.read_csv("../output/IPIP_300_AN.csv")#.drop(columns=['Unnamed: 0']).set_index('item#')
infoDF120 = pd.read_csv("../output/IPIP_120_AN.csv")#.drop(columns=['Unnamed: 0']).set_index('item#')

def drop_nn(df):
    df = df.select_dtypes(include=['number'])
    return df


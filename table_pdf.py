# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:52:18 2021

@author: 15736
"""

from tabula import read_pdf
from tabulate import tabulate
import pandas as pd


df = read_pdf("C:/Users/15736/Downloads/RNDC_PO_0_FAR_540835.PDF") #address of pdf file

df2=df[0].columns


# df2 = pd.melt(df[0])

# foo = lambda x: pd.Series([i for i in reversed(x.split('|'))])
# rev = df[0].apply(foo)

# print(tabulate(df))

df3 = df[0].join(df[0]['Cases|Size |Pack|Item No.|Description|'].str.split('|', expand=True).add_prefix('sec'))
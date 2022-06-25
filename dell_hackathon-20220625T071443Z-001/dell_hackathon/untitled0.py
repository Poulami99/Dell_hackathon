# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:00:20 2019

@author: KIIT
"""
import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\KIIT\Desktop\dell\results.xlsx")

  
# create a dataframe 
dataframe = pd.DataFrame(df, columns = ['Id', 'Company', 'Product', 'TypeName','Inches', 'ScreenResolution', 'Cpu', 'Ram','Memory','Gpu', 'OpSys', 'Weight', 'Price_euros']) 
  
print("Given Dataframe :\n", dataframe)  
  
# selecting rows based on condition 
rslt_df = dataframe[dataframe['TypeName'] == "Gaming"] 
  
print('\nResult dataframe :\n', rslt_df) 

#df.loc[df['Weight'] == '1.22'] = 'Match'  


for x in df.column["Weight"]:
    if x =="1.22kg":
        print(row)
    
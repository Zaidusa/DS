import pandas as pd
import os

file_path=os.path.abspath("data.xlsx")

df=pd.read_excel(file_path)
df1=pd.read_excel(file_path)
filter1 = df["DEPT"]==df1["DEPT"]
filter2 = df["LN"]=="kumar"

df3=df.merge(df1,on=['LN','YOB']).where(filter2 & filter1).dropna()

filter3=df3["DEPT_x"]!=df3["DEPT_y"]

df3['fullname']=df3["DEPT_x"] + "," + df3["DEPT_y"]
columns=["LN","YOB"]
df3['fullname']=df3["DEPT_x"] + "," + df3["DEPT_y"]
df3[columns].where(filter3).dropna()
print(df3)
df4=df3[columns].where(filter3).dropna().join(df3['fullname'])
print(df4)
#
# gfg_csv_data = df4.to_csv('GfG.csv', index = True)
# print('\nCSV String:\n', gfg_csv_data)



#print(df3[columns].where(filter3).dropna())

#print(df3[columns].where(filter3).dropna())
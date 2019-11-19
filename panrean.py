import pandas as pd
import io
import boto3
import warnings
from zipfile import ZipFile
from urllib.request import urlopen
url = 'https://www.bls.gov/oes/special.requests/oesm17all.zip'
zf =  ZipFile(io.BytesIO(urlopen(url).read()))
df17 = pd.read_excel(zf.open('oesm17all/all_data_M_2017.xlsx'))
url = 'https://www.bls.gov/oes/special.requests/oesm13all.zip'
zf = ZipFile(io.BytesIO(urlopen(url).read()))
df13 = pd.read_excel(zf.open('oes_data_2013.xlsx'))
df1 = df17[['occ_code','occ_title','naics','tot_emp','area_title']]
df1.assign(initialTotEmp= "")
df2 = df13[['naics','area_title','occ_code','occ_title','tot_emp']]
df2= df2.rename({'tot_emp':'initialTotEmp'})
result = pd.merge(df1, df2, on=['naics', 'occ_code'])
print(result)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/clean_compras.csv')

print(data.columns)
print(data.dtypes)

data = data[['BENEFICIARIO', 'FACT-NUE-FO', 'CONTRATO', 'CONCEPTO', 'TIPO', 'FDO-#OP', 'FECHA', 'IMPORTE', 'SHEET']]

print(data['BENEFICIARIO'].value_counts())

data['IMPORTE'].hist()

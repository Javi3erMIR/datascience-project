import pandas as pd

def read_excel_df(path, sheet_name, rows=5):
    df = pd.read_excel(path, sheet_name=sheet_name, skiprows=rows)
    df['SHEET'] = sheet_name
    return df

if __name__ == '__main__':
    df_gastos_varios = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='GTOS VARIOS')
    df_contratistas = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='OB.PUBLICA-GTS VARIOS (FDO ESP)')
    df_serv_pros = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='SERV PROF')
    df_comunic = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='COMUNIC')
    df_gastos_repre = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='GTOS REPRESENT')
    df_serv_per = read_excel_df(path='./data/DICIEMBRE_2021.xlsx', sheet_name='SERV PERS')

    df_compras_dic = pd.concat([df_gastos_varios, df_contratistas, df_serv_pros, df_comunic, df_gastos_repre, df_serv_per])
    df_compras_dic = df_compras_dic.dropna(how='any')

    df_compras_dic.to_csv('./data/clean_compras.csv', index=None)
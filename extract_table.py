import camelot
import pandas as pd

names= ['fuvest_2020','fuvest_2019','fuvest_2018','fuvest_2017','fuvest_2016','fuvest_2015','fuvest_2014','fuvest_2013','fuvest_2012']
column_name = [ 'CODIGO_E_NOME_DA_CARREIRA', 'VAGAS', 'INSCRITOS', 'AUSENTES', 'CONVOC_2_FASE', 'CONVOC_POR_VAGA', 'CORTE_MIN', 'MAX']

def get_table():
    for n in names:
        tables = camelot.read_pdf("./pdf/"+n+".pdf", pages= "all")
        dataframes = []

        #concatenate all tables from pdf
        for i in tables:
            d = i.df
            if(len(d.columns) == 8):
                d.columns = column_name
                #remove header lines
                d.drop(d.index[0:2], inplace=True)
                dataframes.append(i.df)

        big_table = pd.concat(dataframes)
        #drop useless columns (1..7)
        #big_table.drop(big_table.columns[[1,2,3,4,5,7]], axis=1, inplace=True)
        big_table.to_csv("./csv/"+n + ".csv", index=False)
        print("------------------------- n -------------------------")
        print(big_table)

get_table()

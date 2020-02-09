import pandas as pd
import re
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

names= ['fuvest_2020','fuvest_2019','fuvest_2018','fuvest_2017','fuvest_2016','fuvest_2015','fuvest_2014','fuvest_2013','fuvest_2012']
final_columns = ['CORTE_2020','CORTE_2019','CORTE_2018','CORTE_2017','CORTE_2016', 'CORTE_2015', 'CORTE_2014', 'CORTE_2013','CORTE_2012']
dataframes = []

WHITE = (255, 255, 255)

running = True

def filter(df):
    #elimina linhas vazias
    df = df.dropna(subset=['CODIGO_E_NOME_DA_CARREIRA'])
    #elimina linhas que nao sao de ampla concorrencia
    df = df.drop(df[df['CODIGO_E_NOME_DA_CARREIRA'].str.contains("Escola Pública")].index)
    #seleciona apenas as linhas que sao d e ampla concorrencia
    df_ampla = df.loc[df['CODIGO_E_NOME_DA_CARREIRA'].str.contains("Ampla"),:]

    if(not df_ampla.empty):
        df_curso = df.loc[df['CODIGO_E_NOME_DA_CARREIRA'].str.contains(r'\d'),:]

        #print('---------------------------------df_ampla---------------------------------')

        df_ampla = df_ampla.drop('CODIGO_E_NOME_DA_CARREIRA', axis=1)
        df_ampla.reset_index(drop=True, inplace=True)

        df_curso = df_curso['CODIGO_E_NOME_DA_CARREIRA']
        df_curso.reset_index(drop=True, inplace=True)

        df_final = pd.concat([df_curso, df_ampla], axis=1)

    else:
        df_final = df

    df_final['CODIGO_E_NOME_DA_CARREIRA'] = df_final['CODIGO_E_NOME_DA_CARREIRA'].str.extract('(\d+)')

    return df_final

def load(save = False):
    for name in names:
        data = pd.read_table("./csv/"+name+".csv",skip_blank_lines=True, skipinitialspace=True, sep=',')
        data = filter(data)
        #print(data)
        if(save): data.to_csv(name+"_TESTE.csv", index=False)
        dataframes.append(data)
    return dataframes

def select (columns_name, data):
    return data[columns_name]

dataset = load()
dataset_selected = []
for df in dataset:
    df = df.rename(index = df['CODIGO_E_NOME_DA_CARREIRA'])
    d = select(['CORTE_MIN'], df)
    d['CORTE_MIN'] = d['CORTE_MIN'].astype('float64')
    d = d.dropna()
    dataset_selected.append(d)
#print(dataset_selected)

def plot_violin(result):
    diff_df = result.diff(axis=1, periods= -1)
    plt.figure(figsize=(100,10))
    ax = sns.violinplot(data=diff_df.T, palette="Pastel1", aspect=1.8)
    ax.set_title("Variação da nota de corte da Fuvest", fontsize = 50)
    ax.set_xlabel('Código do Curso', fontsize=40)
    ax.set_ylabel('Pontos', fontsize=40)
    fig = ax.get_figure()
    fig.savefig("Violin.png", bbox_inches='tight')
    #plt.show()

def plot_boxplot(result):
    diff_df = result.diff(axis=1, periods= -1)
    plt.figure(figsize=(100,10))
    ax = sns.boxplot(data=diff_df.T, palette="Pastel1")
    ax.set_title("Variação da nota de corte da Fuvest", fontsize = 50)
    ax.set_xlabel('Código do Curso', fontsize=40)
    ax.set_ylabel('Pontos', fontsize=40)
    fig = ax.get_figure()
    fig.savefig("Boxplot.png", bbox_inches='tight')
    #plt.show()

result = pd.concat(dataset_selected, axis=1, sort=False)
result.columns = final_columns

plot_boxplot(result)
plot_violin(result)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from plot_pizza import *

def plot_bar_por_cidade(df, cidade, var, title, label_y):
    '''
	Plota o grafico por cidade
	Params:
		df(DataFrame): dataset
        cidade(string): cidade desejada
        var([string]): as variaveis que deseja plotar (só pode ser de len = 2)
        title(string): Titulo do gŕafico
        label_y: label que representará o eixo y
	'''
    labels = [cidade]
    men_means = []
    women_means = []
    df = df[df.NOME_CIDADE == cidade]
    men_means.append(df[var[0]].mean())
    women_means.append(df[var[1]].mean())
    # localizacao da label
    x = np.arange(len(labels))  
    # largura da barra
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label=var[0])
    rects2 = ax.bar(x + width/2, women_means, width, label=var[1])

    # Editando a visualização
    ax.set_ylabel(label_y)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.show()



def plot_bar_2columns(df,var_1, var_2, label_1, label_2, label_y, title):
    '''
	Plota o grafico com duas variaveis por medição
	Params:
		df(DataFrame): dataset
        var_1(string): Variavel que aparecerá primeiro. Exemplo: 'QTD_DOMICILIOS'
        label_1(string): Label para facilitar entendimento da primeira variavel . Exemplo: 'Quantidade de docimicilios'
        var_2(string): Variavel que aparecerá segundo. Exemplo: 'TAXA_ANALF_MAIS_60'
        label_2(string): Label para facilitar entendimento da seguda variavel . Exemplo: 'Analfabetos com 60+'
        title(string): Titulo do gŕafico
        label_y: label que representará o eixo y
	'''
    estados = df['UF'].unique()
    labels = estados
    men_means = []
    women_means = []

    for i in range(len(estados)):
        teste = df[df.UF == estados[i]]
        men_means.append(teste[var_1].mean())
        women_means.append(teste[var_2].mean())


    x = np.arange(len(labels))  

    width = 0.35  

    fig, ax = plt.subplots(figsize=(18, 6))
    ax.bar(x - width/2, men_means, width, label=label_1)
    ax.bar(x + width/2, women_means, width, label=label_2)

    ax.set_ylabel(label_y)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

def plot_bar_idades(df):
    '''
	Plota o grafico por idade
	Params:
		df(DataFrame): dataset
	'''
    data =[]
    data.append(df['PERC_POPULACAO_TOTAL_0a5'].mean())
    data.append(df['PERC_POPULACAO_TOTAL_6a14'].mean())
    data.append(df['PERC_POPULACAO_TOTAL_14a24'].mean())
    data.append(df['PERC_POPULACAO_TOTAL_25a39'].mean())
    data.append(df['PERC_POPULACAO_TOTAL_40a59'].mean())
    data.append(df['PERC_POPULACAO_TOTAL_ACIMA60'].mean())

    plot_pizza(data,
    ['0 a 5','6 a 14', '14 a 24','25 a 39', '40 a 59', 'Acima 60'],
    "POR IDADE")

def plot_bar_salario_por_cidade(df, cidade):
    '''
	Plota o grafico de salário por cidade
	Params:
		df(DataFrame): dataset
        cidade(string): Nome da cidade
	'''

    labels = [cidade]
    men_means = []
    women_means = []
    df = df[df.NOME_CIDADE == cidade]
    men_means.append(df['MEDIA_REND_NOMINAL_HOMENS'].mean())
    women_means.append(df['MEDIA_REND_NOMINAL_MULHERES'].mean())
    # localizacao da label
    x = np.arange(len(labels))  
    # largura da barra
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Homem')
    rects2 = ax.bar(x + width/2, women_means, width, label='Mulher')

    # Editando a visualização
    ax.set_ylabel('Salário (R$)')
    ax.set_title('Renda média')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

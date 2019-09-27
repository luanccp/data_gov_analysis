import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_by_uf(df,uf):
    sns.set(style="whitegrid")

    f, ax = plt.subplots(figsize=(6, 55))

    sns.set_color_codes("muted")
    sns.barplot(x="PERC_POPULACAO_FEMININA", y="NOME_CIDADE", data=df[df.UF == uf],label="FEM", color="b")

    sns.set_color_codes("pastel")
    sns.barplot(x="PERC_POPULACAO_MASCULINA", y="NOME_CIDADE", data=df[df.UF == uf],label="MAS", color="b")

    # Add a legend and informative axis label
    ax.legend(ncol=2, loc="lower right", frameon=True)
    ax.set(xlim=(0, 100), ylabel="",xlabel="Automobile collisions per billion miles")
    sns.despine(left=True, bottom=True)


def plot_pizza_gender(df, city_id):
    labels = 'MAS','FEM'
    data = df[df.ID_CIDADE == city_id]
    newdata = [data.PERC_POPULACAO_FEMININA[0], data.PERC_POPULACAO_MASCULINA[0]]
    
    plot_pizza(newdata, labels, data['NOME_CIDADE'][0])


def plot_pizza(data, labels,title):
    fig1, ax1 = plt.subplots()

    ax1.pie(data, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    ax1.legend(labels, title=title, loc=4)
    plt.show()

def plot_pizza_avg_UF(df, uf):
    new_df = df[df.UF == uf]
    data =[new_df['PERC_POPULACAO_FEMININA'].mean(), new_df['PERC_POPULACAO_MASCULINA'].mean()]

    plot_pizza(data,['MAS','FEM'], uf)

def plot_pizza_gender_equal(df):
    data = pd.DataFrame(df['UF'].value_counts())
    plt.rcParams['figure.figsize'] = (11,7)
    
    plt.bar(np.arange(len(data)), df['UF'].value_counts(), align='center')
    plt.xticks(np.arange(len(data)), data['UF'].keys())
    plt.ylabel('Municípios')
    plt.title('Estados igualitários')

    plt.show()


## Mapear diferenca entre rural e urbano
def plot_pizza_rural_urbano(df):
    fig1, ax1 = plt.subplots()
    ax1.pie([df['PERC_POPULACAO_URBANA'].mean(), df['PERC_POPULACAO_RURAL'].mean()], labels=["URBANO", "RURAL"], autopct='%1.1f%%', shadow=True, startangle=90, colors = ['grey','green'])
    ax1.axis('equal')

    fig1.suptitle('Relação URB x RUR', fontsize=16)
    plt.show()


def plot_pizza_qtd_domicilio(df):
    fig1, ax1 = plt.subplots()

    ax1.pie([df['QTD_DOMICILIOS_RESP_HOMEM'].mean(), df['QTD_DOMICILIOS_RESP_MULHER'].mean()], labels=["Homem", "Mulher"], autopct='%1.1f%%', shadow=True, startangle=90, colors=['gray','green'])
    ax1.axis('equal')
    fig1.suptitle('Responsáveis pelo domicílio', fontsize=16)
    plt.show()

def plot_bar_2columns(df,var_1, var_2, label_1, label_2, label_y, title):
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

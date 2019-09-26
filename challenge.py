
# e deseja-se como output uma explicação sobre quais perfis de 
# municípios são possíveis distinguir com relação à igualdade de gêneros.
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import utils


dataset = pd.read_csv('Dados/dataset.csv')

# dataset.describe()
# dataset.info()
# dataset.ix[0:0].info()



# df_uf = dataset[['UF']].drop_duplicates()
# print(df_uf['UF'][0])

# df_uf_PB = dataset[dataset.UF == 'PB']
# df_uf_PB.describe()



#%% PLOTANDO GRAFICO

def plot_pizza_gender_equal(df):
    data = pd.DataFrame(df['UF'].value_counts())
    plt.rcParams['figure.figsize'] = (11,7)
    
    plt.bar(np.arange(len(data)), df['UF'].value_counts(), align='center')
    plt.xticks(np.arange(len(data)), data['UF'].keys())
    plt.ylabel('Municípios')
    plt.title('Estados igualitários')

    plt.show()






# CHAMADA DAS FUNCOES

# plot_pizza_gender(dataset,2514305)
# plot_pizza_avg_UF(dataset,"PB")

## Reunimos as cidades mais igualitárias
citiesGenderEquals = utils.show_cities_gender_equals(dataset)

## Pré processamos os dados dela
datasetProcessed = utils.replace_nan(citiesGenderEquals)

## Plotamos os estados mais igualitarios
plot_pizza_gender_equal(datasetProcessed)

def main():
    ## Ver relação Urbano X Rural
    plot_pizza_rural_urbano(datasetProcessed)


# # citiesGenderEquals = citiesGenderEquals.apply(replace_nan, axis=1)
# print(citiesGenderEquals)


# plot_by_uf(dataset, "PB")

#%%

## Mapear diferenca entre rural e urbano
def plot_pizza_rural_urbano(df):
    fig1, ax1 = plt.subplots()
    ax1.pie([df['PERC_POPULACAO_URBANA'].mean(), df['PERC_POPULACAO_RURAL'].mean()], labels=["URBANO", "RURAL"], autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

main()
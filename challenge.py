
# e deseja-se como output uma explicação sobre quais perfis de 
# municípios são possíveis distinguir com relação à igualdade de gêneros.
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from utils import *
from plots import *

def load_config():
    ## Setando estilo dos graficos
    plt.style.use(["bmh", "dark_background"])

#%%
def main():

    ## Leitura dos dados
    dataset = pd.read_csv('Dados/dataset.csv')

    load_config()

    ## Reunimos as cidades mais igualitárias
    citiesGenderEquals = show_cities_gender_equals(dataset)

    ## Pré processamos os dados dela
    datasetProcessed = replace_nan(citiesGenderEquals)

    ## Plotamos os estados mais igualitarios
    plot_pizza_gender_equal(datasetProcessed)

    ## Ver relação Urbano X Rural
    # plot_pizza_rural_urbano(datasetProcessed)

    ## Ver relação proprietarios dos domicilios GERAL
    # plot_bar_2columns(datasetProcessed,
    # "QTD_DOMICILIOS_RESP_HOMEM",
    # "QTD_DOMICILIOS_RESP_MULHER",
    # "Homem", 
    # "Mulher", 
    # "Pessoas",
    # "Proprietários de domicílio")

    ## Ver relação proprietarios dos domicilios MEDIA
    # plot_pizza_qtd_domicilio(datasetProcessed)

    ## Ver relação de casal com filhos ou sem filhos em cidades igualitárias
    # plot_bar_2columns(datasetProcessed,
    # "PERC_DOMICILIOS_NUCLEAR_CASAL_COM_FILHOS",
    # "PERC_DOMICILIOS_NUCLEAR_CASAL_SEM_FILHOS",
    # "Com filhos", 
    # "Sem filhos", 
    # "Casais com filhos",
    # "Relação de casais com filhos")

    ## Ver relação de renda entre homem e mulher
    plot_bar_2columns(datasetProcessed,
    "MEDIA_REND_NOMINAL_HOMENS",
    "MEDIA_REND_NOMINAL_MULHERES",
    "Homem", 
    "Mulher", 
    "Renda mensal (R$)",
    "Relação de renda por genero")

# # citiesGenderEquals = citiesGenderEquals.apply(replace_nan, axis=1)
# print(citiesGenderEquals)


# plot_by_uf(dataset, "PB")

#%%
main()
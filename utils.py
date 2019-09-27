from plot_pizza import *
from plot_bar import *

def show_cities_gender_equals(df):
    '''
    Agrupa as cidades que possuem igualdade populacional em porcentual 
    Returns:
        df: Dataframe com o resultado
    '''
    data = df[df.PERC_POPULACAO_FEMININA == 50]
    return data

def replace_nan(df):
    '''
    Substitui valores nullos ou NaN's com 0 (zero) 
    Returns:
        df: Dataframe com a substituição dos NaN's
    '''
    df.fillna(0,inplace=True)
    return df

def detalhar_cidade(df):
    '''
    Detalha cidade plotando graficos para: RURxURB, Idades, Domicilios, Casais com filhos, Pais solteiros, Saneamento básico
    '''
    plot_pizza_rural_urbano(df)
    
    plot_bar_idades(df)

    plot_pizza_qtd_domicilio(df)
    
    plot_bar_por_cidade(df, 
    df.values[0][1],
    ['PERC_DOMICILIOS_NUCLEAR_HOMEM_COM_FILHOS', 'PERC_DOMICILIOS_NUCLEAR_MULHER_COM_FILHOS'],
    'Pais solteiros',
    'Solteiro com filhos (%)')
    
    plot_bar_por_cidade(df, 
    df.values[0][1],
    ['PERC_DOMICILIOS_SANEAMENTO_ADEQUADO', 'PERC_DOMICILIOS_SANEAMENTO_SEMI_INADEQUADO'],
    'Saneamento básico',
    'Percentual da população (%)')  
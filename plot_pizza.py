import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_pizza_gender(df, city_id):
	'''
	Plota o grafico de genero da cidade solicitada
	Params:
		df(DataFrame): dataset
		city_id(int): id da cidade ou municipio
	'''
	labels = 'MAS','FEM'
	data = df[df.ID_CIDADE == city_id]
	newdata = [data.PERC_POPULACAO_FEMININA[0], data.PERC_POPULACAO_MASCULINA[0]]

	plot_pizza(newdata, labels, data['NOME_CIDADE'][0])


def plot_pizza(data, labels,title):
	'''
	Plota o grafico de pizza
	Params:
		df(DataFrame): dataset
		labels([string]): Vetor com as colunas
		title(string): Titulo do gráfico
	'''
	fig1, ax1 = plt.subplots()

	ax1.pie(data, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')

	ax1.legend(labels, title=title, loc=4)
	plt.show()

def plot_pizza_avg_UF(df, uf):
	'''
	Plota o grafico de genero com média por estado
	Params:
		df(DataFrame): dataset
		uf(string): Valor da UF. Exemple:'ES'
	'''
	new_df = df[df.UF == uf]
	data =[new_df['PERC_POPULACAO_FEMININA'].mean(), new_df['PERC_POPULACAO_MASCULINA'].mean()]

	plot_pizza(data,['MAS','FEM'], uf)

def plot_pizza_gender_equal(df):
	'''
	Plota o grafico de estados mais igualitarios com a contagem de municípios
	Params:
		df(DataFrame): dataset
	'''
	data = pd.DataFrame(df['UF'].value_counts())
	plt.rcParams['figure.figsize'] = (11,7)

	plt.bar(np.arange(len(data)), df['UF'].value_counts(), align='center')
	plt.xticks(np.arange(len(data)), data['UF'].keys())
	plt.ylabel('Municípios')
	plt.title('Estados igualitários')

	plt.show()


## Mapear diferenca entre rural e urbano
def plot_pizza_rural_urbano(df):
	'''
	Plota o grafico relacionando Rural X Urbanp
	Params:
		df(DataFrame): dataset
	'''
	fig1, ax1 = plt.subplots()
	ax1.pie([df['PERC_POPULACAO_URBANA'].mean(), df['PERC_POPULACAO_RURAL'].mean()], labels=["URBANO", "RURAL"], autopct='%1.1f%%', shadow=True, startangle=90, colors = ['grey','green'])
	ax1.axis('equal')

	fig1.suptitle('Relação URB x RUR', fontsize=16)
	plt.show()


def plot_pizza_qtd_domicilio(df):
	'''
	Plota grafico da relação Homem X Mulher que é responsavel por domicílio.
	Params:
		df(DataFrame): dataset
	'''
	fig1, ax1 = plt.subplots()

	ax1.pie([df['QTD_DOMICILIOS_RESP_HOMEM'].mean(), df['QTD_DOMICILIOS_RESP_MULHER'].mean()], labels=["Homem", "Mulher"], autopct='%1.1f%%', shadow=True, startangle=90, colors=['gray','green'])
	ax1.axis('equal')
	fig1.suptitle('Responsáveis pelo domicílio', fontsize=16)
	plt.show()

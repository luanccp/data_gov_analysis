import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_bar_por_cidade(df, cidade, var, title, label_y):
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
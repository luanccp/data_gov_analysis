def plot_by_uf(df,uf):
    sns.set(style="whitegrid")

    # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(6, 55))

    # genders = sns.load_dataset(dataset).sort_values("total", ascending=False)

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

def show_cities_gender_equals(df):
    data = df[df.PERC_POPULACAO_FEMININA == 50]
    return data

def replace_nan(df):
    df.fillna(0,inplace=True)
    return df

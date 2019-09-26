def show_cities_gender_equals(df):
    data = df[df.PERC_POPULACAO_FEMININA == 50]
    return data

def replace_nan(df):
    df.fillna(0,inplace=True)
    return df

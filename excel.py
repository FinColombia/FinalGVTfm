import pandas as pd
# cargar data5.csv en un DataFrame
df = pd.read_csv('data5.csv')

# guardar el DataFrame en un archivo Excel
df.to_excel('Phidias.xlsx')

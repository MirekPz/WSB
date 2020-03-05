import pandas as pd

df = pd.read_csv('plik.csv', sep=';')
df.to_excel('plik_wynikowy.xlsx', index=None, header=True)

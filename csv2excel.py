# Konwersja plików CSV do formatu Excela 

# uwaga: w folderze "Dane" mpogą być przed konwersją tylko pliki CSV

import os
import pandas as pd

files_list = os.listdir("Dane")
print("\nZawartość katalogu przed konwersją plików:\n", files_list)

os.chdir("Dane")

for plik in files_list:
    df = pd.read_csv(plik, sep=';')
    df.to_excel(plik[:-4] + '.xlsx', index=None, header=True)
    # [:-4] - wycina z nazwy pliku tekst: .csv

new_files_list = os.listdir()

print("\nZawartość katalogu po konwersji plików:\n", new_files_list)

os.chdir("..")

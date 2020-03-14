# Konwersja wielu plików CSV do formatu Excela 
# uwaga: w folderze "Dane" mogą być przed konwersją tylko pliki CSV

import os
import pandas as pd

from tqdm import tqdm
import time

print(os.getcwd())

files_list = os.listdir("Dane")
print("\nZawartość katalogu przed konwersją plików:\n", files_list)

print()
print(os.getcwd())

liczba_plikow_csv = len(files_list)
print("Liczba plików CSV:", liczba_plikow_csv)

os.chdir("Dane")

for i in tqdm(range(liczba_plikow_csv)):
    print(i)
    plik = files_list[i]
    print(plik)
    df = pd.read_csv(plik, sep=';')
    df.to_excel(plik[:-4] + '.xlsx', index=None, header=True)
    # [:-4] - wycina z nazwy pliku tekst: .csv
    time.sleep(0.9)   # opóźnienie - zakomentować cały wiersz 

new_files_list = os.listdir()

print("\nZawartość katalogu po konwersji plików:\n", new_files_list)

os.chdir("..")

print(os.getcwd())

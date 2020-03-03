import os

files_list = os.listdir('Dane')
print("\nZawartość katalogu przed zmianą:\n", files_list)

prefix = "WI_"

os.chdir("Dane")

for plik in files_list:
    os.rename(plik, prefix + plik)

new_files_list = os.listdir()
print("\nZawartość katalogu po zmianie nazw plików:\n", new_files_list)

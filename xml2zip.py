# Kompresowanie pliku XML do ZIP

import os
import glob
import zipfile
import sys

print("\nKompresowanie pliku XML do ZIP.")

print()
print("Ścieżka do bieżącej lokalizacji:\t", os.getcwd())
print()
print("Zawartość bieżącego katalogu:\t", os.listdir())
print()

xml_files = []
files_list = os.listdir()
for element in files_list:
    if ".xml" in element:
        print(element)
        xml_files.append(element)
        print(xml_files)

liczba_plikow_XML_w_katalogu = len(xml_files)
print('Liczba plików XML w bieżącym katalogu:', liczba_plikow_XML_w_katalogu)

if liczba_plikow_XML_w_katalogu == 0:
    print("Brak plików XML do kompresji!")
    sys.exit()

katalog = '*.xml'
# katalog = '/home/mirek/test/*.xml'

for file_xml in glob.glob(katalog):
    print(file_xml)
    new_file = file_xml[0:-4]
    print(new_file)
    os.rename(file_xml, new_file)
    file_xml = new_file
    print(file_xml)
    file_zip = zipfile.ZipFile(file_xml + ".zip", "w")
    file_zip.write(file_xml, compress_type=zipfile.ZIP_DEFLATED)

    # file_zip jest uchwytem do pliku a nie plikiem !!!!!!

    print(file_xml)
    print(file_zip)
    print('-'*50)

    file_zip.close()

    print(os.listdir())
    print('realpath = ', os.path.realpath(file_xml))
    print('basename = ', os.path.basename(file_xml))
    print("\n")

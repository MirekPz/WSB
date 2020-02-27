import os
import glob
import zipfile

katalog = '*.xml'
# katalog = '/home/mirek/test/*.xml'


print("\n")

for file_xml in glob.glob(katalog):
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

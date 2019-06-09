task = """
HW 6. Строки и файлы
1. Скачать архив
https://github.com/kirill-levenets/python_course/blob/master/lesson6.zip
2. Подобрать пароль (3 строчных латинских буквы). Для работы с архивами можно использовать модуль zipfile. Для подбора паролей - itertools.
3. Распаковать (в итоге получится группа папок с файлами логов в таком формате
“device\tage\tsex\tcity\tuser_id\tsearch_keyword\tdomain\turl\ttype”
4. Создать папку и в ней для каждого города который встретится в логах, создать файл (вида “new_jersey.tsv”) в котором вывести все поисковые запросы и количество уникальных user_id с которыми они встречались (через \t)
alabama.tsv
   facebook\t23
   youtube\t13
   facebook login\t6
   ebay\t6
"""

print(task)
print("{:=^80s}".format("< 1. HW 6. Строки и файлы >"))


from string import ascii_lowercase
from itertools import permutations

passwords = ["".join(p) for p in permutations(ascii_lowercase, 3)]
#print (passwords)

import os
base_path = os.getcwd()
file_name = "new.zip"
full_path = base_path + "/" + file_name

import zipfile

archive = zipfile.ZipFile(full_path, mode='r')

# zip_file = open(full_path, "rb")
# if zipfile.is_zipfile(zip_file):
#     print("Файл {} являетя валидным ZIP-архивом".format(zip_file))
# else:
#     print("Файл {} НЕ являетя валидным ZIP-архивом".format(zip_file))

print(archive)


password = None
opened_zip = None
opened = False


#archive.printdir()
archive.extractall(path=base_path, pwd=b'asd')
#full_path, mode='r', pwd=bytes("asd"))
print(str.encode("asd"), "asd".encode("utf-8"))

chunk = "я строка".encode('utf8')
print(chunk)



print(opened_zip)

# def brute(archive, password):
#     try:
#         archive.extractall(pwd=password)
#         print('[+] Password is {}'.format(password))
#     except:
#         pass

#     try:
#         data = ZipFile.open(file, mode="r", pwd=p)
#         print("Found password {}".format(p))
#     except:
#         pass
#
# # opened = False
# # while not opened:
# #     zipfile.ZipFile.open(full_path, "rb")
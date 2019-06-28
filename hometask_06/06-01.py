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


import os
base_path = os.getcwd()
archive = base_path + "/" + "lesson6.zip"

import zipfile
arch = zipfile.ZipFile(archive, "r")

from string import ascii_lowercase
from itertools import permutations
passwords = ["".join(p).encode() for p in permutations(ascii_lowercase, 3)]

#successfully extracted using "zip" password, i.e. no need to repeat this block every time i do further coding ^_^
import time
start = time.time()

for word in passwords:
    try:
        if time.time() - start > 1:
            print("Currently passing \'{}\' ...".format(word.decode()))
            start = time.time()
        arch.extractall(base_path, pwd=word)
    except Exception:
        pass
    else:
        print("Correct password is \'{}\'!".format(word.decode() ))
        break

os.chdir("lesson6")

print("Found these log files:")
log_paths = []
for info in [x for x in os.walk(os.getcwd())]:
    for log in info[-1]:
        log_paths.append(info[0]+"/"+log)

[print(x) for x in log_paths]


os.chdir(base_path)

database = {}
for log_path in log_paths:
    print("Processing: {}".format(log_path))
    with open(log_path, "r") as file:
        for line in file:
            try:
                row = [x.strip() for x in line.split("\t")]
                city, user, request = row[3], row[4], row[5]
                if city not in database:
                    database[city] = {}
                if request not in database[city]:
                    database[city][request] = [user]
                elif user not in database[city][request]:
                    database[city][request].append(user)
            except Exception:
                print("While importing data from \n\'{}\'\nat line \n\'{}\'\n an error happened!!!".format(file,line))

import shutil
shutil.rmtree("lesson6")

if not os.path.exists("results_per_city"):
    os.mkdir("results_per_city")
os.chdir("results_per_city")

for city in database:
    with open(city+".tsv","+w") as output:
        print("Writing to file {}".format(city+".tsv"))
        for request in database[city]:
            output.write("{}\t{}\n".format(request, len(database[city][request])))
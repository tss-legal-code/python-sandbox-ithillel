print("{:=^80s}".format(" < P R A C T I C E # 3 > "))

task = """класс и как декоратор и как менеджер контекста;
замеряет время выполнения;
что быстрее - отработать исключение или использовать уловный оператор?"""

import sys
from time import time

class Hameleon:
    def __init__(self, func=1):
        self.func = func
        self.b = self.e = None

    def __enter__(self):
        #print("start")
        self.b = time()
        #return 'dfddgdagasasasas '

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.e = time()
        return self.e - self.b
        #print("exited context manager in {} secs".format(self.e-self.b))

    def __call__(self, *args, **kwargs):
        self.__enter__()
        try:
            self.func(*args, **kwargs)
        finally:
            exc_type, exc_val, exc_tb = sys.exc_info()
            self.__exit__(exc_type, exc_val, exc_tb)



@Hameleon
def a(heroin):
    print(heroin*' [x] ')

asd = a(10)

with Hameleon() as h:
    print(h*10)





print("{:=^80s}".format(" < P R A C T I C E # 2 > "))

from contextlib import contextmanager
from random import randint

@contextmanager
def pick():
    print("start")
    yield randint(1,100)
    print("end")


for x in range (10):
    with pick() as p:
        print(p ** 22)




#
#
# print("{:=^80s}".format(" < P R A C T I C E # 1 > "))
#
# class log_err(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self)
#         print ('LOG ERR!!', self.message)
#
#     def writedown(self):
#         with open("log_err.txt", "a") as f:
#             f.write("logged some info\n")
#
#     def __str__(self):
#         return "FUCK OFF!!!"
#
#
# try:
#     raise log_err("MESSAGEEEE!")
#
# except log_err as asd123:
#     asd123.writedown()
#     print("hello LOG_ERR")
#     print(asd123)



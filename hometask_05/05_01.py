task = """
1. Реализовать декораторы рассмотренные на лекции

1.1. таймер - выводит время работы функции
1.2. запоминатель - кэширует аргументы функции и её результаты, и возвращает готовые значения при повторном обращении
1.3. счетчик вызовов - считает сколько раз вызывалась функция
1.4. единичный вызов - выполняет вызов функции только при первом обращении, затем выводит сообщение, что функция уже вызывалась

"""


print("{:=^80s}".format("< 1.1. @timer >"))

import time

def timer(function):
    def wrapper(x):
        print("Starting execution of \'{}\'".format(function.__name__))
        t0 = time.time()
        function(x)
        t1 = time.time()
        print("Execution of \'{}\' took \'{:.10f}\' seconds".format(function.__name__, t1-t0))
    return wrapper

@timer
def function_0(x):
    for y in range(1000000):
        d = y ** 3
    print("... function processed \'{}\'".format(x))

function_0("some argument")




print("{:=^80s}".format("< 1.2. @rememberer >"))
#добавил обработку произвольного числа позиционных аргументов

def rememberer(function):
    d={}
    def wrapper(*args):
        if args in d:
            print("\nFunction \'{}\' with arguments \'{}\' was recently calculated, so result was stored and now it is extracted from dictionary".format(function.__name__, args))
            print("result of calculation", d[args])
        else:
            print("\nFirst run of function \'{}\' with arguments \'{}\'".format(function.__name__, args))
            res = function(*args)
            print("result of calculation", res)
            d[args]=res
    return wrapper

@rememberer
def function_1(t, x):
    print(x)
    for y in range(1000000):
        d = y ** 3
    return x*23

function_1("some argument", 12)

function_1("some argument", 12) #check it

function_1("some argument", 13)

function_1("some argument", 13) #check it



print("{:=^80s}".format("< 1.3. @counter >"))
# добавил запоминание количества вызовов КАЖДОЙ функции с декоратором

def counter(function):
    d={}
    def wrapper(*args):
        if function.__name__ not in d:
            d[function.__name__] = 1
            print("Function {} was called for the first time!".format(function.__name__))
            res = function(*args)
            print("result:", res)
        else:
            d[function.__name__] += 1
            print("Function {} was called {} times!".format(function.__name__, d[function.__name__]))
            res = function(*args)
            print("result:", res)
    return wrapper

@counter
def function_2_1(t, x):
    for y in range(1000000):
        d = y ** 3
    return x*23

@counter
def function_2_2(t, x):
    for y in range(1000000):
        d = y ** 3
    return x*23

function_2_1("some argument", 12)

function_2_1("some argument", 12) #check it

function_2_2("some argument", 13)

function_2_2("some argument", 13) #check it

print("{:=^80s}".format("< 1.4. @single_call >"))
# логическая проверка элегантно работает для ЕДИНИЧНОГО вызова,
# а для фиксированного количества разрешенных вызовов можно реализовать декоратор
# так же как и счетчик, только с условием прекращения выполнения на определенной итерации

def single(function):
    first_run = True
    def wrapper(*args):
        nonlocal first_run
        if first_run:
            print("first run of \'{}\'".format(function.__name__))
            res = function(*args)
            print("result:", res)
        else:
            print("Error! \'{0}\' has already been run! NOTE: \'{0}\' can run only once!".format(function.__name__))
        first_run = False
    return wrapper

@single
def function_3(t, x):
    for y in range(1000000):
        d = y ** 3
    return x*23

function_3("some argument", 12)

function_3("some argument", 12) #check it

function_3("some argument", 13) #check it

function_3("some argument", 13) #check it
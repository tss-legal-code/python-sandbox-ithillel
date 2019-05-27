import time


#timer
# def dec(fun):
#     def wrapper(x):
#         t0 = time.time()
#         print("decorator")
#         fun(x)
#         print("/decorator")
#         t1 = time.time()
#         print("elapsed {}".format(t1-t0))
#     return wrapper
#
# @dec
# def funct(x):
#     print(x)
#     for y in range(1000000):
#         d = y ** 3
#
# funct(10)

#запоминатель

# def dec1(fun):
#     d={}
#     def wrapper(args):
#         if args in d:
#             t0 = time.time()
#             print(d[args])
#             t1 = time.time()
#             print("elapsed {}".format(t1 - t0))
#         else:
#             t0 = time.time()
#             #print("decorator")
#             res = fun(args)
#             print(res)
#             #print("/decorator")
#             t1 = time.time()
#             print("elapsed {}".format(t1-t0))
#             d[args]=res
#             print("args and results:", d)
#     return wrapper
#
# @dec1
# def funct1(x):
#     print(x)
#     for y in range(1000000):
#         d = y ** 3
#     return x*23
#
# funct1(10)
#
# funct1(12)
#
# funct1(14)
#
# funct1(12)

#счетчик вызовов

# def dec2(fun):
#     d={}
#     f=0
#     def wrapper(args):
#         nonlocal f
#
#         if args in d:
#             t0 = time.time()
#             print(d[args])
#             t1 = time.time()
#             print("elapsed {}".format(t1 - t0))
#         else:
#             t0 = time.time()
#             #print("decorator")
#             res = fun(args)
#             print(res)
#             #print("/decorator")
#             t1 = time.time()
#             print("elapsed {}".format(t1-t0))
#             d[args]=res
#             print("args and results:", d)
#         f += 1
#         print("call No.{}".format(f))
#     return wrapper
#
# @dec2
# def funct2(x):
#     print(x)
#     for y in range(1000000):
#         d = y ** 3
#     return x*23
#
# funct2(10)
#
# funct2(12)
#
# funct2(14)
#
# funct2(12)

# единичный вызов
#
# def dec3(fun):
#     d={}
#     f=0
#     def wrapper(args):
#         nonlocal f
#         if f == 0:
#             if args in d:
#                 t0 = time.time()
#                 print(d[args])
#                 t1 = time.time()
#                 print("elapsed {}".format(t1 - t0))
#             else:
#                 t0 = time.time()
#                 # print("decorator")
#                 res = fun(args)
#                 print(res)
#                 # print("/decorator")
#                 t1 = time.time()
#                 print("elapsed {}".format(t1 - t0))
#                 d[args] = res
#                 print("args and results:", d)
#             f += 1
#             print("call No.{}".format(f))
#         else:
#             print("Do not call me no more, bastard! I mean it!")
#     return wrapper
#
# @dec3
# def funct3(x):
#     print(x)
#     for y in range(1000000):
#         d = y ** 3
#     return x*23
#
# funct3(10)
#
# funct3(12)
#
# funct3(14)
#
# funct3(12)

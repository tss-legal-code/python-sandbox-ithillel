

def suppressor(*errs):
    def wrapper_(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e0:
                print("caught \'{}\'".format(e0))
                if isinstance(e0, errs):
                    return "You are stupid! There is no RESULT"
        return wrapper
    return wrapper_

@suppressor(ZeroDivisionError)
def generate_error():
    print(1/0)

tmp = generate_error()

print(tmp)


# def suppressor(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as e0:
#             print(e0)
#             return "You are stupid!"
#     return wrapper
#
# @suppressor
# def generate_error():
#     print(1/0)
#
# tmp = generate_error()
#
# print(tmp)


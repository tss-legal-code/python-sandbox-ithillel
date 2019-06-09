task = """

3. Сделать свою реализацию декоратора lru_cache, 
аналогичную библиотечному (описание в конце презентации).

LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые 
дольше всего не запрашивались. Соответственно, необходимо хранить время последнего 
запроса к значению. И как только число закэшированных значений превосходит N необходимо 
вытеснить из кеша значение, которое дольше всего не запрашивалось.

Задача - 1
Создать декоратор lru_cache (подобный тому который реализован в Python).

Задача - 2
Ваш lru_cache декоратор должен иметь служебный метод cache_info  - статистика 
использования вашего кеша (например: сколько раз вычислялась ваша функция, а 
сколько раз значение было взято из кеша, сколько места свободно в кэше, время жизни кэша)

Задача - 3
Ваш lru_cache декоратор должен иметь служебный метод cache_clear - очищает кэш

"""

print(task)

print("{:=^80s}".format("< 1-3. @personal_lru_cache >"))
from time import time, sleep


def personal_lru_cache(func, max_size=5, ttl=1):
    cache = {}
    call_counter = 0
    taken_from_cache_counter = 0

    def wrapper(*args, **kwargs):
        nonlocal call_counter, taken_from_cache_counter
        call_counter += 1

        key = str([str(a) for a in args] + [str(k) for k in kwargs])

        if (key in cache) and (time() - cache[key]["created"] <= ttl):
            print("Using a cached value")
            cache[key]["used"] = time()
            taken_from_cache_counter += 1

        else:
            if len(cache) == max_size:
                last_used = sorted(cache.keys(), key=lambda x: cache[x]["used"])[0]
                del cache[last_used]
                print("Deleted a most long ago used key \'{}\' from cache".format(last_used))

            cache[key] = {}
            cache[key]["created"] = cache[key]["used"] = time()
            print("Added/Re-added a key \'{}\' to a cache".format(key))
            cache[key]["value"] = func(*args, **kwargs)

        def cache_info():
            if call_counter: print("{:=^80s}".format("< 2. Cache info report>"))
            print("Function {} was called {} times".format(func.__name__, call_counter))
            print("Value was taken from cache {} times".format(taken_from_cache_counter))
            print("TTL of values in cache is {} sec".format(ttl))
            print("Cache free space is {} items".format(max_size - len(cache)))
            if call_counter:
                print("Cache contents are:")
                for x in sorted(cache.keys()):
                    print(x, cache[x])

        def cache_clear():
            nonlocal call_counter, taken_from_cache_counter
            print("{:=^80s}".format("< 3. Cache clear report>"))
            cache.clear()
            call_counter = taken_from_cache_counter = 0
            cache_info()

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return cache[key]["value"]

    return wrapper


@personal_lru_cache
def fib(n):
    if n <= 2:
        return n
    return fib(n - 1) + fib(n - 2)


calc = [fib(i) for i in range(2000)]
print(calc)
fib.cache_info()
fib.cache_clear()

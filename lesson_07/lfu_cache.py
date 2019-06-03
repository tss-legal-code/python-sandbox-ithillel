def lfu_cache(func,maxsize=2):
    cache() = {}

    def wrapper(*args, **kwargs):
        key = tuple([a for a in args] + [item for item in kwargs.items()])
        if key not in cache:
            cache[key]['val'] = func(*args, **kwargs)
            cache[key]['count'] = 1
            if len(cache) > maxsize:
                f = sorted(cache, key=lambda a: a.items()[]

            return cache[key][val]
        else:
            return cache[key][val]


    return wrapper



@lfu_cache
def triply(x):
    s = x ** x ** x
    return s

for i in (1,2,4,1,1,23,4,1,2,3,1,12,3,2,1,12,2,3,3,1,12,4,3,2,1,12,3,3):
    print(triply(i))



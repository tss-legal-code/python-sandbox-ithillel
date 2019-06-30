task = """
По аналогии с LRU кешем реализовать LFU кеш.
LFU (Least frequently used) - кеш в которм при необходимости удаления - выбирается элемент который использовался реже всего.
"""

print(task)
print("{:=^80s}".format("< 1. HW 7. LFU cache >"))

def lfu_cache(func, maxsize=3):
    cache = {}
    def wrapper(*args,**kwargs):
        print("wrapper works...")
        key = str([str(a) for a in args] + [str(k) for k in kwargs])
        if key not in cache:
            if len(cache) + 1 > maxsize:
                sacrifice = sorted(cache, key=lambda i: cache[i]["count"])[0]
                print("...removing key {} from cache".format(sacrifice))
                del cache[sacrifice]
            print("...adding key {} to cache\n".format(key))
            result = func(*args, **kwargs)
            cache[key]={}
            cache[key]['count'] = 1
            cache[key]['val'] = result
        else:
            print("...taking key {} from cache\n".format(key))
            cache[key]["count"] += 1

        wrapper.cache = cache
        return cache[key]['val']


    return wrapper

@lfu_cache
def triply(x):
    s = x ** 3
    return s

for i in (1,2,4,1,1,23,4,1,2,3,1,12,3,2,1,12,2,3,3,1,12,4,3,2,1,12,3,3):
    print("Number {} in third power is {}:".format(i, triply(i)))
    print("\nCacahe contents:")
    [print(x) for x in triply.cache.items()]
    print()


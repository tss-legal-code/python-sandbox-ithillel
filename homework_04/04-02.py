
d = lambda x: True if sum([int(n) for n in bin(100)[2:]]) % 2 == 0 else False


print(d(2))
task="""
4. Дан список словарей. Нужно их отсортировать. 
- по стоимости, от больших к меньшим
- использовать для сортировки лямбду и обычную функцию

autos = [
  {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},
  {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": 3000},
  {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},
  {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},
  {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},
  {"brand": "Nissan", "model": None, "year": 1964, "price": None},
  {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},
  {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},
  {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}
]
"""

autos = [
  {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},
  {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": 3000},
  {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},
  {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},
  {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},
  {"brand": "Nissan", "model": None, "year": 1964, "price": None},
  {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},
  {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},
  {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}
]

print(task)

print("\n4.a. Сортировка по стоимости, от больших к меньшим с использованием лямбды")

autos_lambda = sorted(autos, key=lambda a: a["price"] if a["price"] else 0, reverse=True)
[print(x) for x in autos_lambda]

print("\n4.b. Сортировка по стоимости, от больших к меньшим с использованием обычной функции")

def fun(a):
    return a["price"] if a["price"] else 0

autos_fun = sorted(autos, key=fun, reverse=True)

[print(x) for x in autos_fun]
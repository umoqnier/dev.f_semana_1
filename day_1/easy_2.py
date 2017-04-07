from functools import reduce
def multi_list():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    entero = reduce(lambda x,y: x * y, lista)
    print(entero)

multi_list()
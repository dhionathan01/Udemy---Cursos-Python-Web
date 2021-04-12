"""
Zip

zip() -> Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla, set ou dicionário.

print(list(zip1))
zip1 = zip(lista1, lista2, 'abc')

print(tuple(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

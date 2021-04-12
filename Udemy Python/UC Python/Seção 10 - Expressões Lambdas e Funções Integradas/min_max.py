"""
Min e Max
max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.
"""
# Exemplos
'''
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))   # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(lista))   # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(lista))   # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # 129
'''

'''
# Faça um programa que receba dois valores do usuário e mostre o maior

valor1 = int(input('Digite o Valor 1:'))
valor2 = int(input('Digite o Valor 2:'))
print(max(valor1, valor2))
'''
'''
print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g'))
print(max(3.145, 5.789))
print(max('Dhionathan Jobim - Geek University'))
'''

"""
min() ->Retornar o menor valor em um iterável ou menor de dois ou mais elementos
"""
# Exemplos min()
'''
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))   # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(lista))   # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(lista))   # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # a

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # 1

# Faça um programa que receba dois valores do usuário e mostre o menor

valor1 = int(input('Digite o Valor 1:'))
valor2 = int(input('Digite o Valor 2:'))
print(min(valor1, valor2))

print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'g'))
print(min(3.145, 5.789))
print(min('Dhionathan Jobim - Geek University'))
'''

# Outros exemplos

'''
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# Leva em consideração a ordem alfabética
print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))   # Ollivander
print(min(nomes, key=lambda nome: len(nome)))   # Tim

'''

musicas = [
    {'titulo': "Thunderstruck", 'tocou': 3},
    {'titulo': "Dead Skin Mask", 'tocou': 2},
    {'titulo': "Back in Black", 'tocou': 4},
    {'titulo': "Too old to rock'in' roll, to young to die", 'tocou': 32}
]
'''
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
'''
# Desafio! Como encontrar a música mais tocada e a menos tocada sem usar max(), min(), e lambda

mais_tocada = 0

for music in musicas:
    if music['tocou'] > mais_tocada:
        mais_tocada = music['tocou']

for music in musicas:
    if music['tocou'] == mais_tocada:
        print(music['titulo'])

menos_tocada = 99999

for music in musicas:
    if music['tocou'] < menos_tocada:
        menos_tocada = music['tocou']

for music in musicas:
    if music['tocou'] == menos_tocada:
        print(music['titulo'])
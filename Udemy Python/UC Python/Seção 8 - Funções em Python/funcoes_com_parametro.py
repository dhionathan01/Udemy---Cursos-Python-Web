"""
Funções com Parâmetro (de entrada)

 - Funções que recebem dados para serem processados dentro da mesma.
Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída
Se a gente pensar em função, já sabemos que temos funções que:
 - Não possuem entrada.
 - Não possuem saída.
 - Possuem entrada mas não possuem saída.
 - Não possuem entrada mas possuem saída.
 - possuem entrada e saída.


"""

# Refatorando uma função

"""
def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)
"""
# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')
    return ''


print(cantar_parabens('Dhioanthan'))

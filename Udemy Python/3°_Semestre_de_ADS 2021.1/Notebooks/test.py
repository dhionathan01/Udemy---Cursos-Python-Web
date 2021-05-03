open_file = open("notas_estudantes.txt")
file_content = open_file.read()
alunos = []
fragmento = file_content.split('\n')
print(fragmento)
open_file.seek(0)
media = []
for i in range(len(fragmento)):
    alunos.append(open_file.readline().strip('\n'))
for des_frag in range(len(fragmento)):
    alunos[des_frag] =  alunos[des_frag].rstrip(':')
    alunos[des_frag] =  alunos[des_frag].split(':')
for contador in range (len(fragmento)):
    for nota in range(1, len(alunos[contador])):
        alunos[contador][nota] = int(alunos[contador][nota])
for iterador in range(len(fragmento)-1):
    if sum(alunos[iterador][1:])/(len(alunos[iterador][1:])) >= 6:
        print(alunos[iterador][0])


for contagem in range(len(fragmento)-1):
    media = []
    for calculador in range(len(alunos[contagem][1:])):
        media.append(sum(alunos[contagem][1:])/len(alunos[contagem][1:]))
        print(f"Aluno:{alunos[contagem][0]} Média: {media[calculador]:.2f}")

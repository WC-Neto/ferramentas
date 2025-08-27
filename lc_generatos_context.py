numeros = [1, 2, 3, 4, 5]
dobro = [item * 2 for item in numeros]
dobro_dos_pares = [item * 2 if item % 2 == 0 else item for item in numeros] # dobro dos pares e mantem item se não

#print(dobro)
#print(dobro_dos_pares)

alunos = ['Ana', 'Beto', 'Carlos']
notas = [10, 8, 9]
alunos_e_notas = dict()

#for aluno, nota in zip(alunos, notas):
#    alunos_e_notas[aluno] = nota

#print(alunos_e_notas)
alunos_e_notas_2 = {aluno: nota for aluno, nota in zip(alunos, notas)}
#print(alunos_e_notas_2)

minha_lista = [x*x for x in range(5)]
#print(minha_lista)

def gerador_de_quadrados(numero_max):
  for i in range(numero_max):
    yield i * i

quadrados = gerador_de_quadrados(5)
'''for i in quadrados:
  print(i)'''

# A classe que você criou
import time

class Cronometro:
  def __enter__(self):
    self.inicio = time.time()
    return self

  def __exit__(self, tipo, valor, traceback):
    final = time.time()
    print(f'Tempo decorrido: {final - self.inicio:.4f} segundos')

print("Vamos testar o cronômetro...")
with Cronometro():
  soma = 0
  for i in range(10_000_000):
    soma += i
print("...teste finalizado!")

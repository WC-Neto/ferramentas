import pandas as pd
import numpy as np
import datetime

dataset = pd.read_csv("Brasileirao_Matches.csv")

#print(f'As 5 primeiras linhas do dataset são compostas por \n {dataset.head()}')
teste = dataset.isna()
#print(f'O maior número de gols feitos por um time da casa é de {dataset.home_goal.max()} gols')
#print(f'O maior número de gols feitos por um time de fora é de {dataset.away_goal.max()} gols')
sem_nulos = dataset.dropna().copy()
sem_nulos['home_goal'] = sem_nulos['home_goal'].astype('int64')
sem_nulos['away_goal'] = sem_nulos['away_goal'].astype('int64')
sem_nulos['datetime'] = pd.to_datetime(sem_nulos['datetime'])
sem_nulos['diasdasemana'] = sem_nulos['datetime'].dt.day_name()
#print(sem_nulos.diasdasemana)
sem_nulos['mes_da_partida'] = sem_nulos['datetime'].dt.month
#print(sem_nulos['mes_da_partida'])
'''Próxima tarefa:

Prove que a coluna diasdasemana tem valor. 
Mostre-me a média de gols totais (casa + visitante) para cada dia da semana.
Quero ver o resultado ordenado, do dia com a maior média de gols para o dia com a menor.
Execute.'''

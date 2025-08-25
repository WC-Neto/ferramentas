import csv
import os
import struct
import re

def escrita_txt(): #função para leitura de arquivos .txt
    print("=" * 60 )
    print('1. ESCRITA DE ARQUIVOS (.TXT)')
    print("=" * 60 )
    arquivo = 'exemplo.txt'
    
    with open (arquivo, 'w', encoding='utf-8') as f:
        
        f .write('Primeira linha do arquivo\n')
        f .write(f'Segunda linha com acentos:  {2} {4} {6}\n')
        f .write(f'Terceira linha com acentos: {3} {6} {9}\n')
        f .write(f'Quarta linha com acentos: {-3} {6} {-9}\n')


    print(f'arquivo {arquivo}')

def leitura_txt(): #função para leitura de arquivos .txt
    print("=" * 60 )
    print('2. LEITURA DE ARQUIVOS (.TXT)')
    print("=" * 60 )
    arquivo = 'exemplo.txt'
    
    try:    
        with open(arquivo, 'r', encoding ='utf-8') as f:
            conteudo_completo = f.read()
            print(conteudo_completo)
            print(f'Leitura do arquivo {arquivo} concluida')
            
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado')
    except UnicodeDecodeError:
        print('Erro: Problema na codificação')

escrita_txt()        
leitura_txt()
        
def leitura_linha_text():
    print("=" * 60 )
    print('2. LEITURA DE ARQUIVOS (.TXT)')
    print("=" * 60 )
    arquivo = 'exemplo.txt'
    print('=' * 60)
    
    try:    
        with open(arquivo, 'r', encoding ='utf-8') as f:
            linhas = f.readlines()
            print(f'Total de linhas {len(linhas)}\n')
            for i, linha in enumerate(linhas, 1):
                print(f'linha {i}: em {linha}')
                   
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado')
    except UnicodeDecodeError:
        print('Erro: Problema na codificação')

leitura_linha_text()
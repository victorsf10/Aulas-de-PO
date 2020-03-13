#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT09 – Nona contribuição da primeira etapa                                                                                                                                     
#Implementar o bucket sort e imprimir os graficos conforme segue:                                                                                                                   
#                                                                                                                                                                                   
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                                                                                                    
#   
#                                                                                                                                                                                   
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 15K, 25K, 35K, 45K, 55K.                                                                          
#

#"Importação das devidas bibliotecas ;)"

import sys

import math

import random
from random import randint

import timeit

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

#{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('lines', linewidth=1.5)
plt.style.use('dark_background')
sys.setrecursionlimit(10**9)
#}       

#{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('lines', linewidth=1.5)
plt.style.use('dark_background')
#}    

#"Segunda Função responsável pela criação do gráfico(x,y) para estudo do desempenho de algoritmo" *(Usada para criar o gráfico dos 3 casos apresentados juntos na mesma malha)
#Implementação do professor + implementação do aluno#{      
def desenhaGrafico2(x, y, yde, yce, yqck, ymrg, ybub, ysel, ysrt, file_name, label, label2, label3, label4, label5, label6, label7, label8, file_title, line_color, line_color2, line_color3, line_color4, line_color5, line_color6, line_color7, line_color8, xl, yl):                                                                                               
    fig = plt.figure(figsize=(20, 20))                                                                                                                                                                 
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = ':',linewidth=6,label = label)                           
    ax.plot(x,yde, color=line_color2,linestyle = ':',linewidth=8,label = label2)                     
    ax.plot(x,yce, color=line_color3,linestyle = ':',linewidth=10,label = label3)
    ax.plot(x,yqck, color=line_color4,linestyle = ':',linewidth=12,label = label4)
    ax.plot(x,ymrg, color=line_color5,linestyle = ':',linewidth=14,label = label5)
    ax.plot(x,ybub, color=line_color6,linestyle = ':',linewidth=16,label = label6)
    ax.plot(x,ysel, color=line_color7,linestyle = ':',linewidth=18,label = label7)
    ax.plot(x,ysrt, color=line_color8,linestyle = ':',linewidth=20,label = label8)
                                                                                                                                                       
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                 
    plt.setp(stemlines, 'linewidth', 2)                                                                                                                
    stemlines = plt.stem(x,yde, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                            
    plt.setp(stemlines, 'linewidth', 2)                                                                                                                
    stemlines = plt.stem(x,yce, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2)
    stemlines = plt.stem(x,yqck, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2)
    stemlines = plt.stem(x,ymrg, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2)
    stemlines = plt.stem(x,ybub, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2)
    stemlines = plt.stem(x,ysel, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2)
    stemlines = plt.stem(x,ysrt, markerfmt=' ',linefmt='w:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 2) 
                                                                                                                                                       
    ax.grid(True)                                                                                                                                      
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                         
    plt.xlabel(xl)                                                                                                                                                                                                                         
    plt.title(file_title)                                                                                                                                                                                                            
    fig.savefig(file_name)                                                                                                                                                                                                          
#}       

#"Função De Ordenação Auxiliar do Bucket Sort: Bubble Sort" *(Versão mais optimizada do algoritmo, para executar o código um pouco mais rápido)
#Implementação do aluno#{
def bubbleSort(lista):                                                                                                                                                                                                                                                                                                                     
    n = len(lista)
    while True:
        swapped = False
        for i in range(1, n):
            if lista[i-1] > lista[i]:
                lista[i-1], lista[i] = lista[i], lista[i-1]
                swapped = True
        n -= 1
        if not swapped:
            break
#}

#"Função De Ordenação Auxiliar do Bucket Sort: Selection Sort" *(Versão mais optimizada do algoritmo, para executar o código um pouco mais rápido) 
#Implementação do aluno#{
def selectionSort(lista):                                                                                                                                                                                                                                                                                                                     
    for i in range(len(lista)): 
        min_idx = i 
        for j in range(i+1, len(lista)): 
            if lista[min_idx] > lista[j]: 
                min_idx = j 
                       
        lista[i], lista[min_idx] = lista[min_idx], lista[i]                                                 
#}

#"Função De Ordenação Auxiliar do Bucket Sort: Quick Sort"
#Implementação do aluno#{
def particao_QuickSort(lista,indice_inicio,indice_fim):                                                                                                                                                                                        
    i = ( indice_inicio - 1 )                                                                                                                                            
    x =  randint(indice_inicio, indice_fim)                                                                                          
                                                                                                                                      
    for j in range(indice_inicio , indice_fim):                                                                                     
        if   lista[j] <= x:                                                                                                         
                                                                                                                                      
            i = i+1                                                                                                                 
            lista[i],lista[j] = lista[j],lista[i]                                                                                                                                                                                      
                                                                                                                                    
    lista[i+1],lista[indice_fim] = lista[indice_fim],lista[i+1]                                                                                                                                                                                             
    return ( i+1 )                                                                                                                  

def quickSort(lista,indice_inicio,indice_fim):                                                                                                                                                                                                                                                                                                                     
    if indice_inicio < indice_fim:                                                             
                                                                                               
        pivot = particao_QuickSort(lista,indice_inicio,indice_fim)                              
                                                                                               
        quickSort(lista, indice_inicio, pivot-1)                                               
        quickSort(lista, pivot+1, indice_fim)                                                  
#}

#"Função De Ordenação Auxiliar do Bucket Sort: Merge Sort"
#Implementação do aluno#{
def funcao_Merge(esquerda,direita):                                                                                                                                                                                                            #                                                                                                                              
    index_esquerd, index_direit = 0, 0                                                                                              
    result = []                                                                                                                     
                                                                                                                               
    while index_esquerd < len(esquerda) and index_direit < len(direita):                                                            
                                                                                                                                            
        if esquerda[index_esquerd] < direita[index_direit]:                                                                                                                                                                               
            result.append(esquerda[index_esquerd])                                                                                  
            index_esquerd += 1                                                                                                                                                                                                                                          
        else:                                                                                                                                                                                                                             
            result.append(direita[index_direit])                                                                                    
            index_direit += 1                                                                                                                                                                     
                                                                                                                                    
    result += esquerda[index_esquerd:]                                                                                               
    result += direita[index_direit:]                                                                                                 
                                                                                                                                    
    return result                                                                                                                   

def mergeSort(lista):                                                                                                                                                                                                                                               
    if len(lista) <= 1:                                                                                                                                             
        return lista                                                                           
                                                                                               
    meio = len(lista) // 2                                                                     
    esquerda = mergeSort(lista[:meio])                                                         
    direita = mergeSort(lista[meio:])                                                          
                                                                                               
    return funcao_Merge(esquerda,direita)                                                      
#}

#"Função De Ordenação Auxiliar do Bucket Sort: Insertion Sort"
#Implementação do aluno#{
def insertionSort(lista):                                                                                                                                                                                                                            
	for i in range(1, len(lista)):
		tmp = 0
		tmp = lista[i]
		position = i
		while position > 0 and lista[position - 1] > tmp:
			lista[position] = lista[position - 1]
			position -= 1
		lista[position] = tmp
###}

#"Função De Ordenação Auxiliar do Bucket Sort: Shell Sort"
#Implementação do aluno#{
def shellSort(lista):                                                                                                                                                                                                                            
    tam_lista = len(lista)                                                                     
    gap =  tam_lista//2                                                                                                                                                                    
    while gap > 0:                                                                               
        for i in range(gap, tam_lista):                                                         
            aux = lista[i]                                                                                                                                                               
            j = i                                                                                                                                                                           
            while (j >= gap) and (lista[j-gap] > aux):                                           
                lista[j] = lista[j-gap]                                                         
                j = j - gap                                                                                                                                                                                                                         
            lista[j] = aux                                                                                                                                                              
        gap //= 2                                                                              
#}

#"Função De Ordenação Auxiliar do Bucket Sort: Counting Sort"
#Implementação do aluno#{
def countingSort(lista,max_val):                                                                                                                                                                                                                            
    ref = max_val + 1                                                                          
    contador = [0] * ref                                                                                                                                                                                    
    for a in lista:                                                                            
        contador[a] += 1                                                                                                                                        
    i = 0                                                                                      
    for a in range(ref):                                                                                
        for c in range(contador[a]):                                                             
            lista[i] = a                                                                       
            i += 1                                                                             
#}

#"Funções De Divisão ,Do Vetor De Elementos A Serem Ordenados, Auxiliar do Bucket Sort"
#Implementação do aluno#{
def hashing(lista):
    m = lista[0]
    
    for i in range(1, len(lista)):
        if ( m < lista[i] ):
            m = lista[i]
            
    result = [m,int(math.sqrt( len(lista)))]
    
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
#}

#"Função Bucket + Bubble Sort"
#Implementação do aluno#{
def bucketSort1(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        bubbleSort(bucket)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Selection Sort"
#Implementação do aluno#{
def bucketSort2(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        selectionSort(bucket)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Insertion Sort"
#Implementação do aluno#{
def bucketSort3(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        insertionSort(bucket)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Quick Sort"
#Implementação do aluno#{
def bucketSort4(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        quickSort(bucket,0,len(bucket)-1)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Merge Sort"
#Implementação do aluno#{
def bucketSort5(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        mergeSort(bucket)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Shell Sort"
#Implementação do aluno#{
def bucketSort6(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        shellSort(bucket)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Counting Sort"
#Implementação do aluno#{
def bucketSort7(lista,max_val):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        countingSort(bucket,max_val)
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função Bucket + Função '.sort()' do Python(Tim Sort)" (EXTRA - Apenas para motivos de comparação mesmo!
#Implementação do aluno#{
def bucketSort8(lista):                                                                                                                                                                                                                        
    code = hashing(lista)
    buckets = [list() for _ in range(code[1])]
    
    for i in lista:
        x = re_hashing(i,code)
        buck = buckets[x]
        buck.append(i)
        
    for bucket in buckets:
        bucket.sort()
         
    ndx = 0
    
    for b in range(len( buckets )):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1                                                             
#}

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa OITAVA ATIVIDADE será em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#Obs.:(O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos)
#Implementação do aluno#{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #

  tempos_orden_bubble = list()
  tempos_orden_selec = list()   
  tempos_orden_quick = list()
  tempos_orden_merge = list() 
  tempos_orden_insert = list()
  tempos_orden_shell = list()
  tempos_orden_count = list()
  tempos_orden_sort = list()
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória                                                                                                                                                                                                                                              
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)


    tempos_orden_bubble.append(timeit.timeit("bucketSort1({})".format(lista),setup="from __main__ import bucketSort1",number=1))
    tempos_orden_selec.append(timeit.timeit("bucketSort2({})".format(lista),setup="from __main__ import bucketSort2",number=1))
    tempos_orden_insert.append(timeit.timeit("bucketSort3({})".format(lista),setup="from __main__ import bucketSort3",number=1))
    tempos_orden_quick.append(timeit.timeit("bucketSort4({})".format(lista),setup="from __main__ import bucketSort4",number=1))
    tempos_orden_merge.append(timeit.timeit("bucketSort5({})".format(lista),setup="from __main__ import bucketSort5",number=1))
    tempos_orden_shell.append(timeit.timeit("bucketSort6({})".format(lista),setup="from __main__ import bucketSort6",number=1))
    tempos_orden_count.append(timeit.timeit("bucketSort7({},{})".format(lista,i),setup="from __main__ import bucketSort7",number=1))
    tempos_orden_sort.append(timeit.timeit("bucketSort8({})".format(lista),setup="from __main__ import bucketSort8",number=1))                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico2(lista_entrada,tempos_orden_insert,tempos_orden_shell,tempos_orden_count,tempos_orden_quick,tempos_orden_merge,tempos_orden_bubble,tempos_orden_selec,tempos_orden_sort,"GraphBucketSort(Tamanho_Lista-X-Tempo_Ordenacoes)Lista_Aleatoria_Exemplo_Extra.png", "Tempo(Lista->Aleatória[Insertion+Bucket Sort])","Tempo(Lista->Aleatória[Shell+Bucket Sort])","Tempo(Lista->Aleatória[Counting+Bucket Sort])","Tempo(Lista->Aleatória[Quick+Bucket Sort])","Tempo(Lista->Aleatória[Merge+Bucket Sort])","Tempo(Lista->Aleatória[Bubble+Bucket Sort])","Tempo(Lista->Aleatória[Selection+Bucket Sort])","Tempo(Lista->Aleatória[Função'.Sort()'+Bucket Sort])",'(Bucket + .Sort()/Bubble/Selection/Quick/Merge/Insertion/Shell/Counting Sort - Lista: Aleatória - Amostragem Extra)Tamanho_Lista X Tempo_Ordenacoes','blue','magenta','lime','yellow','red','grey','orange','cyan',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
#}

#Inicialização da aplicação:
#
lista_teste = [15000,25000,35000,45000,55000]              
cria_Graficos(lista_teste)                                               
#
#                                               

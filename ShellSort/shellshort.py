
#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT06 – contribuição da primeira etapa                                                             
#Implementar o algoritmo shellsort e imprimir os graficos conforme segue:                                  
#                                                                                                          
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                           
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] ~ OPCIONAL                        
#                                                                                                          
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 30K, 40K, 50K, 60K, 70K. 

#"Importação das devidas bibliotecas ;)"

import random

import timeit

import matplotlib as mpl

import matplotlib.pyplot as plt

import numpy as np

#{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('lines', linewidth=0.5)
plt.style.use('_classic_test')
#}

#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos"
#Implementação do professor + implementação do aluno#    
def desenhaGrafico(x,y,yde,file_name, label, label2,file_title, line_color, line_color2, mark,xl, yl):                                         
    fig = plt.figure(figsize=(18, 16))                                                                                                                                                                
    ax = fig.add_subplot(111)                                                                                                                         
    ax.plot(x,y, color=line_color,linestyle = '-',label = label,linewidth=7)                                                                          
    ax.plot(x,yde, color=line_color2,linestyle = ':', marker = mark,markerfacecolor='none',linewidth=6,markeredgewidth=2,markersize=30,label = label2)
                                                                                                                                                      
    plt.scatter(x,y, s=500,marker='X',facecolor='black',edgecolors= 'black', linewidths=3)                                                            
    stemlines = plt.stem(x,y, markerfmt='kX',linefmt='k:', basefmt='k:',use_line_collection=True)                                                                                               
    plt.setp(stemlines, 'linewidth', 1)                                                                                                               
                                                                                                                                                      
    plt.scatter(x,yde, s=500,marker=' ',facecolor='black',edgecolors = 'black',linewidths=3)                                                          
    stemlines2 = plt.stem(x,yde, markerfmt=' ',linefmt='k', basefmt=' ',use_line_collection=True)                                                                                               
    plt.setp(stemlines2, 'linewidth', 1)                                                                                                                                                                                                                                                                                                                                                                           #
                                                                                                                                                      
    ax.grid(True)                                                                                                                                     
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                             
    plt.ylabel(yl)                                                                                                                                                                                                                        
    plt.xlabel(xl)                                                                                                                                                                                                                        
    plt.title(file_title)                                                                                                                                                                                                           
    fig.savefig(file_name)                                                                                                                                                                                                         
#


#"Função Shell Sort"
#Implementação do aluno#
def shellSort(lista):                                                                          
                                                                                               
    num_iteracoes = 0                                                                          
                                                                                               
    tam_lista = len(lista)                                                                      
    gap =  tam_lista//2                                                                        
                                                                                                   
    while gap > 0:                                                                               
        for i in range(gap, tam_lista):                                                         
            aux = lista[i]                                                                     
                                                                                                           
            j = i                                                                           
                                                                                                           
            while (j >= gap) and (lista[j-gap] > aux):                                           
                lista[j] = lista[j-gap]                                                         
                j = j - gap                                                                    
                num_iteracoes += 1                                                             
                                                                                                           
            lista[j] = aux                                                                      
                                                                                                       
        gap //= 2                                                                              
                                                                                               
    return num_iteracoes                                                                       
#

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa SEXTA ATIVIDADE serão em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos(Da DECRESCENTE que o aluno decidiu fazer apenas para fins acadêmicos).
#Implementação do aluno#{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                           
  tempos_orden = list()
  tempos_orden_decresc = list()
  numer_iteracoes = list()
  numer_iteracoes_decresc = list()
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)                                                                                                                                                                                                                                                
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)

    tempos_orden.append(timeit.timeit("shellSort({})".format(lista),setup="from __main__ import shellSort",number=1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    numer_iteracoes.append(shellSort(lista))   
    
    #2) Lista já ORDENADA em ordem DECRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO-Para comparar com o Insertion Sort, já que este algoritmo é uma implementação aprimorada dele!)                                                                                                                                                                                                                              
    lista = list(range(i,-1,-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    tempos_orden_decresc.append(timeit.timeit("shellSort({})".format(lista),setup="from __main__ import shellSort",number=1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    numer_iteracoes_decresc.append(shellSort(lista))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico(lista_entrada,tempos_orden,tempos_orden_decresc,"GraficoShellSort(Tam_List-X-Temp_Ordena)Lista_Aleatoria.png", "Tempo(Lista->Aleatoria)","Tempo(Lista->Decrescente)",'(Shell Sort-Lista Aleatória)Tamanho_Lista X Tempo_Ordenacoes','cyan','deeppink','s',"<Entradas/>","<Tempo-Saída/>")                                                      
  desenhaGrafico(lista_entrada, numer_iteracoes,numer_iteracoes_decresc,"GraficoShellSort(Tam_List-X-Num_Itera)Lista_Aleatoria.png","Numero_Iteracao(Lista->Aleatoria)","Numero_Iteracao(Lista->Decrescente)",'(Shell Sort-Lista Aleatória)Tamanho_Lista X Numero_Iteracoes','yellow','grey','d',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#}

#Inicialização da aplicação:
#
lista_teste = [30000,40000,50000,60000,70000]                
cria_Graficos(lista_teste)                                               
#

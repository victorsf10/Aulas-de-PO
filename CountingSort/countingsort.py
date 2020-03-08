
#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT07 – Sétima contribuição da primeira etapa                                                                                                                                     
#Implementar o counting sort e imprimir os graficos conforme segue:                                                                                                                 
#                                                                                                                                                                                   
#   *Tamanho da lista de números x Tempo para ordenar pelo método                                                                                                   
#                                                                                                                                                                                   
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 30K, 40K, 50K, 60K, 70K.                                                                          
#

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

#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos" *(Usada para criar os gráficos dos 3 casos apresentados de forma separada)
#Implementação do professor + implementação do aluno#     
def desenhaGrafico(x,y,k,file_name, label,file_title, num,line_color,xl, yl):                                                                            
    fig = plt.figure(figsize=(18, 14))                                                                                                                                                            
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = k, marker = '|',linewidth=12,markeredgewidth=7,markersize=num,label = label)                                                                                                
                                                                                                                                                       
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt='k:',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #
                                                                                                                                                       
    ax.grid(True)                                                                                                                                      
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                         
    plt.xlabel(xl)                                                                                                                                                                                                                     
    plt.title(file_title)                                                                                                                                                                                                           
    fig.savefig(file_name)                                                                                                                                                                                                     
#      

#"Segunda Função responsável pela criação do gráfico(x,y) para estudo do desempenho de algoritmo" *(Usada para criar o gráfico dos 3 casos apresentados juntos na mesma malha)
#Implementação do professor + implementação do aluno#    
def desenhaGrafico2(x,y,yde,yce,file_name, label,label2,label3,file_title, num,num2,num3,line_color,line_color2,line_color3,xl, yl):                                                                                               
    fig = plt.figure(figsize=(20, 20))                                                                                                                                                                 
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = '-', marker = '|',linewidth=12,markeredgewidth=7,markersize=num,label = label)                           
    ax.plot(x,yde, color=line_color2,linestyle = '--', marker = '|',linewidth=12,markeredgewidth=7,markersize=num2,label = label2)                     
    ax.plot(x,yce, color=line_color3,linestyle = ':', marker = '|',linewidth=12,markeredgewidth=7,markersize=num3,label = label3)                                                                                            
                                                                                                                                                       
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt='k:',use_line_collection=True)                                                                                                 
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt='k:',use_line_collection=True)                                                                                                 
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt='k:',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          #
                                                                                                                                                       
    ax.grid(True)                                                                                                                                      
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                        
    plt.xlabel(xl)                                                                                                                                                                                                                         
    plt.title(file_title)                                                                                                                                                                                                            
    fig.savefig(file_name)                                                                                                                                                                                                        
#       

#"Função Counting Sort"
#Implementação do aluno#
def coutingSort(lista,max_val):                                                                                                                                       
                                                                                               
    ref = max_val + 1                                                                          
    contador = [0] * ref                                                                                       
                                                                                               
    for a in lista:                                                                            
        contador[a] += 1 #Contagem das ocorrências                                              
                                                                                               
    i = 0                                                                                      
    for a in range(ref):                                                                                
        for c in range(contador[a]):                                                             
            lista[i] = a                                                                    
            i += 1                                                                             
                                                                                               
    return lista                                                                               
#

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa SÉTIMA ATIVIDADE será em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos(Da DECRESCENTE que o aluno decidiu fazer apenas para fins acadêmicos).
#Implementação do aluno#{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #
                                                                                                                                                                                                                                                                                                           
  tempos_orden = list()
  tempos_orden_decresc = list()
  tempos_orden_cresc = list()
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória                                                                                                                                                                                                                                                 
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)

    tempos_orden.append(timeit.timeit("coutingSort({},{})".format(lista,i),setup="from __main__ import coutingSort",number=1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #                                                                                                                                                                                                                                                                                                           #  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #                                                                                                                                                                                                                                                                                   #
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico(lista_entrada,tempos_orden,'-',"GraphCountingSort(Tam_List-X-Temp_Ordena)Lista_Aleatoria.png", "Tempo(Lista->Aleatoria)",'(Counting Sort- Lista: Aleatória)Tamanho_Lista X Tempo_Ordenacoes',75,'cyan',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
  
#Inicialização da aplicação:
#
lista_teste = [30000,40000,50000,60000,70000]               
cria_Graficos(lista_teste)                                               
#

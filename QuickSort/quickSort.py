
#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT04 – Quarta contribuição da primeira etapa                                                            
#Implementar o algoritmo quicksort e imprimir os seguintes gráficos para listas invertidas(ordenadas por   
#ordem decrescente):                                                                                       
#                                                                                                          
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                           
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] ~ OPCIONAL                        
#                                                                                                          
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 100K, 200K, 300K, 400K, 500K    


#"Importação das devidas bibliotecas ;)"

from random import randint

import timeit

import matplotlib as mpl

import matplotlib.pyplot as plt

import sys

#Devido ao tamanho muito grande das listas de entrada, o limite da pilha de recursividade que o python admite é atingido em algum ponto durante as chamadas recursivas.
sys.setrecursionlimit(10**9)#######


#{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('axes', linewidth=10)
plt.style.use('fivethirtyeight')
#}

#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos"
#Implementação do professor + implementação do aluno#   
def desenhaGrafico(x,y,file_name, label, file_title, line_color, xl, yl):                                                                                                   
    fig = plt.figure(figsize=(18, 16))                                                                                                                                                    
    ax = fig.add_subplot(111)                                                                                                                  
    ax.plot(x,y, color=line_color,linestyle = ':', marker='d', markersize=25,linewidth=3,dashes=(0.5,5),dash_capstyle='round',label = label)   
    stemlines = plt.stem(x, y, linefmt='r:',basefmt='r:',markerfmt='y*',use_line_collection=True)                                           
    plt.setp(stemlines, 'linewidth', 5)                                                                                                        
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                   
    plt.ylabel(yl)                                                                                                                                                                                                               
    plt.xlabel(xl)                                                                                                                                                                                                                
    plt.title(file_title)                                                                                                                                                                                                   
    fig.savefig(file_name)

#
num_iteracoes = 0#<-Variável GLOBAL para se contar os 'SWAPS'(Ou o que seriam eles nesta implementação do quick sort recursivo)

#"Função ''Auxiliar'' para o Quick Sort Recursivo"
#Implementação do aluno#
def particao_QuickSort(lista,indice_inicio,indice_fim):                                                                             
                                                                                                                                    
    global num_iteracoes                                                                                                            
                                                                                                                                                                                                         
    i = ( indice_inicio - 1 )                                                                                                       
                                                                                                                                    
    #Tenha em mente que nosssa variável 'x' estará exercendo o papel de 'pivot'                                                     
    #Na verdade era para a linha de código abaixo ser: 'x = lista[indice_fim]' porém para garantir melhor densempenho do algoritmo  
    #, a modificação abaixo mostrou-se de grande ajuda na redução do tempo de execução do mesmo.                                    
    x =  randint(indice_inicio, indice_fim)                                                                                         
                                                                                                                                      
    for j in range(indice_inicio , indice_fim):                                                                                     
        if   lista[j] <= x:                                                                                                         
                                                                                                                                      
            i = i+1                                                                                                                 
            lista[i],lista[j] = lista[j],lista[i]                                                                                   
                                                                                                                                    
            num_iteracoes += 1                                                                                                       
                                                                                                                                    
    lista[i+1],lista[indice_fim] = lista[indice_fim],lista[i+1]                                                                       
                                                                                                                                
    return ( i+1 )                                                                                                                  
#

#"Função Quick Sort(Recursivo)"
#Implementação do aluno#
def quickSort(lista,indice_inicio,indice_fim):                                                 
                                                                                               
    global num_iteracoes                                                                       
                                                                                               
    if indice_inicio < indice_fim:                                                             
                                                                                               
        pivot = particao_QuickSort(lista,indice_inicio,indice_fim)                             
                                                                                               
        quickSort(lista, indice_inicio, pivot-1)                                               
        quickSort(lista, pivot+1, indice_fim)                                                  
                                                                                               
    aux = num_iteracoes                                                                        
                                                                                                                      
    return aux                                                                                 
#

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa QUARTA ATIVIDADE serão em ordem DECRESCENTE) e retorna os devidos gráficos comparativos"

#Implementação do aluno#
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                           
  global num_iteracoes                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                           
  #tempos_orden = list()                                                                                                                                                                                                                                                                                    
  #numer_iteracoes = list()                                                                                                                                                                                                                                                                                 
  tempos_orden_2 = list()                                                                                                                                                                                                                                                                                 
  numer_iteracoes_2 = list()                                                                                                                                                                                                                                                                              
  #tempos_orden_3 = list()                                                                                                                                                                                                                                                                                 
  #numer_iteracoes_3 = list()                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
    
    #Piores Casos (Especiais) do Quick Sort:                                                                                                                                                                                                                                                               
    #1) Lista já ORDENADA em ordem DECRESCENTE <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)    
    #lista = list(range(i,-1,-1))
    #2) Lista já ORDENADA em ordem CRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                               
    lista2 = list(range(0,i+1,1))                                                                                                                                                                                                                                                                         
    #3) Lista já ORDENADA onde todos os seus elementos são IGUAIS<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                          
    #lista3 = list(range(0,i+1,1))                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                           
    #lista3.append(1)#Como os ELEMENTOS DEVEM SER IGUAIS escolheu-se todos serem o número 1, para fins mais rápidos     
        
    #tam = len(lista)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #
    tam2 = len(lista2)                                                                                                                                                                                                                                                                                    
    #tam3 = len(lista3)                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                           
    
                                                                                                                                                                                                                                                                                                           
    #tempos_orden.append(timeit.timeit("quickSort({},{},{})".format(lista,0,tam-1),setup="from __main__ import quickSort",number=1))                                                                                                                                                                       
    #numer_iteracoes.append(quickSort(lista,0,tam-1))                                                                                                                                                                                                                                                      
    
    tempos_orden_2.append(timeit.timeit("quickSort({},{},{})".format(lista2,0,tam2-1),setup="from __main__ import quickSort",number=1))                                                                                                                                                                   
    numer_iteracoes_2.append(quickSort(lista2,0,tam2-1))                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #tempos_orden_3.append(timeit.timeit("quickSort({},{},{})".format(lista3,0,tam3-1),setup="from __main__ import quickSort",number=1))                                                                                                                                                                   
    #numer_iteracoes_3.append(quickSort(lista3,0,tam3-1))    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #                                                                                                                                                                                                                                                                      #
    num_iteracoes = 0                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                           
  #desenhaGrafico(lista_entrada,tempos_orden,"GraficoQuickSort(Tam_List-X-Temp_Orden)Decrescente.png", "Tempo(Lista->Decrescente)",'(Quick Sort-Lista Decrescente)Tamanho_Lista X Tempo_Ordenacoes','black',"<Entradas/>","<Tempo-Saída/>")                                                      
  #desenhaGrafico(lista_entrada, numer_iteracoes,"GraficoQuickSort(Tam_List-X-Num_Itera)Decrescente.png", "Numero_Iteracao(Lista->Decrescente)",'(Quick Sort-Lista)Tamanho_Lista X Numero_Iteracoes','grey',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")                        
  
  desenhaGrafico(lista_entrada,tempos_orden_2,"GraficoQuickSort(Tam_List-X-Temp_Orden)Crescente.png", "Tempo(Lista->Crescente)",'(Quick Sort-Lista Crescente)Tamanho_Lista X Tempo_Ordenacoes','black',"<Entradas/>","<Tempo-Saída/>")                                                         
  desenhaGrafico(lista_entrada, numer_iteracoes_2,"GraficoQuickSort(Tam_List-X-Num_Itera)Crescente.png", "Numero_Iteracao(Lista->Crescente)",'(Quick Sort-Lista Crescente)Tamanho_Lista X Numero_Iteracoes','yellow',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")                         
                                                                                                                                                                                                                                                                                                           
  #desenhaGrafico(lista_entrada,tempos_orden_3,"GraficoQuickSort(Tam_List-X-Temp_Orden)Elementos-Todos-Iguais.png", "Tempo(Lista->Elementos Iguais)",'(Quick Sort-Lista Elementos Iguais)Tamanho_Lista X Tempo_Ordenacoes','black',"<Entradas/>","<Tempo-Saída/>")                              
  #desenhaGrafico(lista_entrada, numer_iteracoes_3,"GraficoQuickSort(Tamanho_Lista-X-Numero_Itera)Elementos-Todos-Iguais.png", "Numero_Iteracao(Lista->Elementos Iguais)",'(Quick Sort-Lista Elementos Iguais)Tamanho_Lista X Numero_Iteracoes','blue',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")
                                                                                                                                                                                                                                                                                                           
#

#Inicialização da aplicação:
#
lista_teste = [100000,200000,300000,400000,500000]         
cria_Graficos(lista_teste)                                               
#


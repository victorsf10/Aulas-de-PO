
#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT05 – Quinta contribuição da primeira etapa                                                            
#Implementar o algoritmo mergesort e imprimir os graficos conforme segue:                                  
#                                                                                                          
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                           
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] ~ OPCIONAL                        
#                                                                                                          
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 20K, 40K, 60K, 80K, 100k.

#"Importação das devidas bibliotecas ;)"

import random

import timeit

import matplotlib as mpl

import matplotlib.pyplot as plt

import sys

#Devido ao tamanho muito grande das listas de entrada, o limite da pilha de recursividade que o python admite é atingido em algum ponto durante as chamadas recursivas.
sys.setrecursionlimit(10**9)#
#O comando acima AUMENTA esse limite de recursão...

#{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('axes', linewidth=0.5)
plt.style.use('seaborn-whitegrid')
#}

#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos"
#Implementação do professor + implementação do aluno#     
def desenhaGrafico(x,y,file_name, label, file_title, line_color, xl, yl):                                                                                                     
    fig = plt.figure(figsize=(18, 16))                                                                                                                                                         
    ax = fig.add_subplot(111)                                                                                                                  
    ax.plot(x,y, color=line_color,linestyle = ':', marker='+', markersize=25,linewidth=2.5,dashes=(0.5,5),dash_capstyle='round',label = label) 
    stemlines = plt.stem(x, y, linefmt='r',markerfmt='ko',use_line_collection=True)                                                            
    plt.setp(stemlines, 'linewidth', 0.5)                                                                                                      
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                      
    plt.ylabel(yl)                                                                                                                                                                                                                 
    plt.xlabel(xl)                                                                                                                                                                                                                 
    plt.title(file_title)                                                                                                                                                                                                    
    fig.savefig(file_name)                                                                                                                                                                                                  
#       

num_iteracoes = 0#<-Variável GLOBAL para se contar os 'SWAPS'(Ou o que seriam eles nesta implementação do merge sort recursivo)

#"Função ''Auxiliar'' para o Merge Sort Recursivo"
#Implementação do aluno#
def funcao_Merge(esquerda,direita):                                                                                                 
                                                                                                                                    
    global num_iteracoes                                                                                                            
                                                                                                                                    
    index_esquerd, index_direit = 0, 0                                                                                              
    result = []                                                                                                                     
                                                                                                                                        
    while index_esquerd < len(esquerda) and index_direit < len(direita):                                                            
                                                                                                                                            
        if esquerda[index_esquerd] < direita[index_direit]:                                                                         
            num_iteracoes += 1                                                                                                      
            result.append(esquerda[index_esquerd])                                                                              
            index_esquerd += 1                                                                                                      
                                                                                                                                                
        else:                                                                                                                       
            num_iteracoes += 1                                                                                                      
            result.append(direita[index_direit])                                                                                    
            index_direit += 1                                                                                                       
            num_iteracoes += 1 #Aqui que ocorre a TROCA de elementos.                                                               
                                                                                                                                    
    result += esquerda[index_esquerd:]                                                                                               
    result += direita[index_direit:]                                                                                                 
                                                                                                                                    
    return result                                                                                                                   
#

#"Função Merge Sort(Recursivo)"
#Implementação do aluno#
def mergeSort(lista):                                                                         
                                                                                               
    global num_iteracoes                                                                       
                                                                                               
    if len(lista) <= 1:  #Base da recursão                                                     
                                                                                                       
        return lista                                                                           
                                                                                               
    meio = len(lista) // 2                                                                     
    esquerda = mergeSort(lista[:meio])                                                         
    direita = mergeSort(lista[meio:])                                                          
                                                                                               
    return funcao_Merge(esquerda,direita)                                                      
                                                                                               
#

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa QUINTA ATIVIDADE serão em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos(No caso, da LISTA DECRESCENTE, que o aluno decidiu fazer apenas para fins acadêmicos).
#Implementação do aluno#
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                           
  global num_iteracoes                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                           
  tempos_orden = list()                                                                                                                                                                                                                                                                                    
  numer_iteracoes = list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          # 
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)                                                                                                                                                                                                                                                
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)                                                                                                                                                                                                                                                                               
    #2) Lista já ORDENADA em ordem DECRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO-Pior caso do MERGE SORT já que sempre será necessário efetuar TROCAS após as comparações!)                                                                                                                                                                                                                              
    #lista = list(range(i,-1,-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                           
    tam = len(lista)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           # 
                                                                                                                                                                                                                                                                                                           
    tempos_orden.append(timeit.timeit("mergeSort({})".format(lista),setup="from __main__ import mergeSort",number=1))                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                           
    mergeSort(lista)                                                                                                                                                                                                                                                                                       
    aux = num_iteracoes                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                           
    numer_iteracoes.append(aux)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #
    num_iteracoes = 0                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                           
  desenhaGrafico(lista_entrada,tempos_orden,"GraficoMergeSort(Tam_List-X-Temp_Ordena)Lista_Aleatoria.png", "Tempo(Lista->Aleatoria)",'(Merge Sort-Lista Aleatória)Tamanho_Lista X Tempo_Ordenacoes','black',"<Entradas/>","<Tempo-Saída/>")                                                      
  desenhaGrafico(lista_entrada, numer_iteracoes,"GraficoMergeSort(Tam_List-X-Num_Itera)Lista_Aleatoria.png", "Numero_Iteracao(Lista->Aleatoria)",'(Merge Sort-Lista Aleatória)Tamanho_Lista X Numero_Iteracoes','red',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")                         
                                                                                                                                                                                                                                                                                                           
  #desenhaGrafico(lista_entrada,tempos_orden,"GraficoMergeSort(Tam_List-X-Temp_Ordena)Lista_Decrescente.png", "Tempo(Lista->Decrescente)",'(Merge Sort-Lista Decrescente)Tamanho_Lista X Tempo_Ordenacoes','black',"<Entradas/>","<Tempo-Saída/>")                                               
  #desenhaGrafico(lista_entrada, numer_iteracoes,"GraficoMergeSort(Tam_List-X-Num_Itera)Lista_Decrescente.png", "Numero_Iteracao(Lista->Decrescente)",'(Merge Sort-Lista Decrescente)Tamanho_Lista X Numero_Iteracoes','red',"<Entradas/>","<'Swaps'(Num_Iterações)-Saída/>")                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
#

#Inicialização da aplicação:
#
lista_teste = [20000, 40000, 60000, 80000, 100000]                                                                                                                                                                                                                                                                                                                  
cria_Graficos(lista_teste)                                               
#

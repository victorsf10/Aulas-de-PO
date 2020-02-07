
#AVALIACAO: (Prof.Ronaldo)
#PO01 – Primeira contribuição da primeira etapa                                                      
#Implementa o algoritmo bSort e imprimir os seguintes gráficos:                                   
#                                                                                                      
#   *Tamanho da lista de números x Tempo para ordenar pelo método                                      
#   *Tamanho da lista x Quantidade de operações (swap)                                                 
#                                                                                                      
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 1000, 10000, 30000, 60000.#
########################################################################################################

#"Importação das devidas bibliotecas ;)"
import timeit

from random import randint

import matplotlib as mpl
import matplotlib.pyplot as plt

###############################################################################{
#"Declarações iniciais..."
mpl.use('Agg')
plt.style.use('ggplot')
mpl.rc('lines', linewidth=2)
#plt.style.use('dark_background') #<-Faz o plano de fundo ser escuro!(opcional)
###############################################################################}

#"Função geradora de lista, sendo o comprimento desta definido como parâmetro de entrada, de elementos aleatórios"   
def geraLista(tam):                                                        
    lista = []                                                             
    for i in range(tam):                                                   
        n = randint(1,1*tam)                                              
        if n not in lista: lista.append(n)                                 
    return lista                                                           
############################################################################  
  
#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos"
def desenhaGrafico(x,y, file_name, label, file_title, line_color,xl = "<Entradas/>", yl = "<Saídas/>"): 
    fig = plt.figure(figsize=(10, 8))                                                                   
    ax = fig.add_subplot(111)                                                                           
    ax.plot(x,y, color=line_color,label = label)                                                        
    plt.stem(x, y, linefmt='b:',markerfmt='C3o',use_line_collection=True)                               
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                               
    plt.ylabel(yl)                                                                                      
    plt.xlabel(xl)                                                                                      
    plt.title(file_title)                                                                               
    fig.savefig(file_name)                                                                              
#########################################################################################################   

#"Função Bubble Sort(Sem o uso da variável 'flag')"
#Implementação do aluno#####################################################
def bSort(lista):                                                     
                                                                           
    num_iteracoes = 0                                                      
                                                                           
    for i in range(0, len(lista)-1):                                       
                                                                           
      for j in range(0, len(lista)-1-i):                                   
                                                                           
        if lista[ j ] > lista[j + 1]:                                      
                                                                           
          lista[j], lista[j + 1] = lista[j + 1], lista[j]                  
          num_iteracoes += 1                                               
                                                                            
    return num_iteracoes                                                   
############################################################################

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente e retorna os devidos gráficos comparativos"
#Implementação do aluno##################################################################################################################################
def cria_Graficos(lista_entrada):                                                                                                                       
                                                                                                                                                        
  tempos_orden = list()                                                                                                                                 
  numer_iteracoes = list()                                                                                                                              
                                                                                                                                                        
  for i in lista_entrada:                                                                                                                               
                                                                                                                                                        
    lista = geraLista(i)                                                                                                                                
    tempos_orden.append(timeit.timeit("bSort({})".format(lista),setup="from __main__ import bSort",number=1))                                 
    numer_iteracoes.append(bSort(lista))                                                                                                           
                                                                                                                                                        
  desenhaGrafico(lista_entrada,tempos_orden, "Grafico(Tamanho_Lista-X-Tempo_Ordenacoes).png", "Tempo",'Tamanho_Lista X Tempo_Ordenacoes','yellow')     
  desenhaGrafico(lista_entrada, numer_iteracoes, "Grafico(Tamanho-X-Numero_Iteracoes).png", "Numero_Iteracao",'Tamanho_Lista X Numero_Iteracoes','lime')
#########################################################################################################################################################

#Inicialização da aplicação:
#########################################
lista_teste = [1000,10000,30000,60000]#
cria_Graficos(lista_teste)              #
#########################################


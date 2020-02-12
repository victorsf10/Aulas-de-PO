
#ATIVIDADE PEDIDA: (Prof.Ronaldo)#
#CT02 – Segunda contribuição da primeira etapa                                                              
#Implementar o algoritmo selection sort e imprimir os seguintes gráficos para listas geradas aleatoriamente e 
#para listas invertidas(ordenadas por ordem decrescente)(pior caso do selection):                             
#                                                                                                             
#   *Tamanho da lista de números x Tempo para ordenar pelo método                                             
#   *Tamanho da lista x Quantidade de operações (Número de comparações)                                       
#                                                                                                             
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 1000, 10000, 30000 e 60000.     

#"Importação das devidas bibliotecas ;)"
import timeit

from random import randint

import matplotlib as mpl
import matplotlib.pyplot as plt


#"Declarações iniciais..."#
mpl.use('Agg')
#plt.style.use('ggplot')
mpl.rc('lines', linewidth=2)
plt.style.use('dark_background')


#"Função geradora de lista, sendo o comprimento desta definido como parâmetro de entrada, de elementos aleatórios" 
#Implementação do professor#    
def geraLista(tam):                                                        
    lista = []                                                             
    for i in range(tam):                                                   
        n = randint(1,1*tam)                                               
        if n not in lista: lista.append(n)                                 
    return lista                                                             

#lista = lista[::-1]<-lista vai ser invertida(deve estar previamente ordenada)
  
#"Função responsável pela criação de gráfico(x,y) para estudo do desempenho de algoritmos"
#Implementação do professor + implementação do aluno#   
def desenhaGrafico(x,y,y2,file_name, label, label2, file_title, line_color,line_color2,xl = "<Entradas/>", yl = "<Saídas/>"): 
    fig = plt.figure(figsize=(10, 8))                                                                                        
    ax = fig.add_subplot(111)                                                                                                
    ax.plot(x,y, color=line_color,label = label)                                                                             
    ax.plot(x,y2, color=line_color2,label = label2)                                                                          
    plt.stem(x, y, linefmt='r:',markerfmt='C3D',use_line_collection=True)                                                    
    plt.stem(x, y2, linefmt='b:',markerfmt='C2D',use_line_collection=True)                                                   
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                                  
    plt.ylabel(yl)                                                                                                                                                                                               
    plt.xlabel(xl)                                                                                                                                                                                               
    plt.title(file_title)                                                                                                                                                                                  
    fig.savefig(file_name)                                                                                                                                                                                
    

#"Função Selection Sort"#
#Implementação do aluno#
def selectionSort(lista):                                                  
                                                                           
    num_iteracoes = 0                                                      
                                                                           
    for i in range(len(lista)):                                            
                                                                           
      min_idx = i                                                          
                                                                           
      for j in range(i+1, len(lista)):                                     
                                                                           
          if lista[min_idx] > lista[j]:                                    
              min_idx = j                                                  
              num_iteracoes += 1                                           
                                                                           
      lista[i], lista[min_idx] = lista[min_idx], lista[i]                  
                                                                            
    return num_iteracoes                                                   

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente e retorna os devidos gráficos comparativos"
#Implementação do aluno#
def cria_Graficos(lista_entrada):                                                                                                                                                                                                               
                                                                                                                                                                                                                                                
  tempos_orden = list()                                                                                                                                                                                                                         
  numer_iteracoes = list()                                                                                                                                                                                                                      
  tempos_orden_inv = list()                                                                                                                                                                                                                                                                                                                                                                                                                                        
  numer_iteracoes_inv = list()                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                
  for i in lista_entrada:                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                
    lista = geraLista(i)                                                                                                                                                                                                                        
    tempos_orden.append(timeit.timeit("selectionSort({})".format(lista),setup="from __main__ import selectionSort",number=1))                                                                                                                   
    numer_iteracoes.append(selectionSort(lista))                                                                                                                                                                                                
                                                                                                                                                                                                                                                
    lista.sort()                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                
    lista = lista[::-1] #"Gambiarra" para inverter uma lista já previamente ORDENADA! ;)                                                                                                                                                        
                                                                                                                                                                                                                                                
    tempos_orden_inv.append(timeit.timeit("selectionSort({})".format(lista),setup="from __main__ import selectionSort",number=1))                                                                                                               
    numer_iteracoes_inv.append(selectionSort(lista))                                                                                                                                                                                            
                                                                                                                                                                                                                                                
  desenhaGrafico(lista_entrada,tempos_orden, tempos_orden_inv,"GraficoSelectionSort(Tamanho_Lista-X-Tempo_Ordenacoes).png", "Tempo", "Tempo(Pior Caso)",'(Selection Sort)Tamanho_Lista X Tempo_Ordenacoes','magenta','gray')                    
  desenhaGrafico(lista_entrada, numer_iteracoes, numer_iteracoes_inv,"GraficoSelectionSort(Tamanho-X-Numero_Iteracoes).png", "Numero_Iteracao", "Numero_Iteracao(Pior Caso)",'(Selection Sort)Tamanho_Lista X Numero_Iteracoes','cyan','yellow')


#Inicialização da aplicação:
########################################
lista_teste = [1000,10000,30000,60000]
cria_Graficos(lista_teste)              


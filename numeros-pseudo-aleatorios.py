# Importando bibliotecas
import random
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

''''
Gera números aleatórios pelo Método Congruente Linear (MCL)
Esta sendo utilizada aqui a fórmula dos geradores congruentes lineares, que são definidos por:
    x_i+1 = (A * X_i + C) mod M
'''
def gerarNumerosAleatoriosMCL(num_amostras):
    lista = list()
    semente = 1
    a = 1000432423545323
    b = 7534577343423434
    m = 8234509343456434

    for i in range(num_amostras):
        semente = (a * semente + b) % m
        lista.append(round(semente, 1))

    # Convertendo os valores para números entre 0 e 1 com uma casa decimal
    aux = list()
    max_lista = max(lista)
    for num in lista:
        res = round(num/max_lista, 1)
        aux.append(res)    
    return aux


def plotarHistograma(lista, titulo):
    plt.figure(figsize=(12,6))
    ax = sns.histplot(lista, kde = True)
    plt.title(titulo)
    ax.set_xlabel('Valores aleatórios')
    ax.set_ylabel('Total')
    plt.show()


def main():
    list_random_nativo_mil = list()
    list_random_nativo_dez_mil = list()
    list_random_mcl_mil = list()
    list_random_mcl_dez_mil = list()

    # número de amostras aleatórias
    experimento_1= 1000 
    experimento_2= 10000

    print('Gerando números aleatórios nativamente no Python:')
    for i in range(experimento_1):
        num = random.random()
        list_random_nativo_mil.append(round(num, 1))
    plotarHistograma(list_random_nativo_mil, 'Distribuição da Frequência Relativa de Números Aleatórios - Python com 1000 amostras')

    for i in range(experimento_2):
        num = random.random()
        list_random_nativo_dez_mil.append(round(num, 1))
    plotarHistograma(list_random_nativo_dez_mil, 'Distribuição da Frequência Relativa de Números Aleatórios - Python com 10000 amostras')

    print('Gerando números aleatórios pelo método congruente linear:')
    list_random_mcl_mil = gerarNumerosAleatoriosMCL(experimento_1)
    plotarHistograma(list_random_mcl_mil, 'Distribuição da Frequência Relativa de Números Aleatórios - Congruência Linear com 1000 amostras')

    list_random_mcl_dez_mil = gerarNumerosAleatoriosMCL(experimento_2)
    plotarHistograma(list_random_mcl_dez_mil, 'Distribuição da Frequência Relativa de Números Aleatórios - Congruência Linear com 10000 amostras')

main()

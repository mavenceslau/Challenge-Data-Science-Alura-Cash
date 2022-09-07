import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Configurações de exibição

def config_exibicao():
    pd.set_option("display.max_columns", 100)
    pd.set_option("display.max_colwidth", None)

#Configurações de gráficos

def config_graficos():
    sns.set_palette('Accent')
    sns.set_style('darkgrid')

#configuração de parametros de exibição de valores fora da notação cientifica
#https://stackoverflow.com/questions/63372647/disable-scientific-notation-and-offset-in-pandas-plot-function



import matplotlib as mpl
mpl.rcParams['axes.formatter.limits'] = (-5,12)


#Função para plotagem de gráficos de dispersão dados

def dispersao(data, x, y):
    ax = sns.scatterplot(data = data, x = x, y = y)
    ax.figure.set_size_inches(14, 6)
    ax.set_title(f'Dispersão de Variáveis {x} X {y} ', fontsize = 20)
    ax.set_xlabel(x, fontsize = 16)
    ax.set_ylabel(y, fontsize = 16)
    plt.plot()
    
    
#Função para plotagem de boxplot

def box(data, x):
    ax = sns.boxplot(data = data, x = x, orient = 'h', width = 0.5)
    ax.figure.set_size_inches(10, 8)
    ax.set_title(f'Boxplot da variável {x}', fontsize=20)
    ax.set_xlabel(x, fontsize=16)
    plt.plot()
    
#Função para remover outliers

def remove_outlier(data, variavel, nome_variavel):
    variavel = data[nome_variavel]
    Q1 = variavel.quantile(.25)
    Q3 = variavel.quantile(.75)
    IIQ = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IIQ
    limite_superior = Q3 + 1.5 * IIQ
    selecao = (variavel >= limite_inferior) & (variavel <= limite_superior)
    data = data[selecao]
    return data        
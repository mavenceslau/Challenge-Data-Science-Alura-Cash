import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay


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

#Função para separação dos dados do dataset, em dados de treino e dados de teste
def treino_teste(x, y, SEED):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = SEED)
    return x_train, x_test, y_train, y_test    

#Função para treinamento e previsão do modelo
def classificador(classificador, x_train, x_test, y_train):
    modelo = classificador.fit(x_train, y_train)
    y_pred = modelo.predict(x_test)
    return y_pred

#Função para realizar metricas do modelo
def metricas(y_pred, y_test):
    print("Acurácia:", round(metrics.accuracy_score(y_test, y_pred), 2))
    print("Precisão:", round(metrics.precision_score(y_test, y_pred), 2))
    print("Recall:", round(metrics.recall_score(y_test, y_pred), 2)) 
    print("F1:", round(metrics.f1_score(y_test, y_pred), 2))
    #print("Matriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix = cm)
    disp.plot()
    
#Curva Roc
def curva_roc(classificador, x_test, y_test):
    y_pred_proba = classificador.predict_proba(x_test)[::, 1]
    fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_proba)
    auc = metrics.roc_auc_score(y_test, y_pred_proba)
    plt.rcParams['figure.figsize'] = (20, 8)
    plt.plot(fpr, tpr, label = 'LR, auc = ' + str(auc))
    plt.plot([0,1], [0,1], color = 'red', lw = 2, linestyle = '--')
    plt.legend(loc = 4)

#Comparação de Metricas
def comp_metricas(classificadores, x, y, SEED):
    x_train, x_test, y_train, y_test = treino_teste(x, y, SEED)
    for classifier in classificadores:
        cf = classifier
        y_pred = classificador(cf, x_train, x_test, y_train)
        name = classifier.__class__.__name__
        print("="*30)
        print(name)
        print('')
        print('****Resultados****')
        metricas(y_pred, y_test)
        print('')

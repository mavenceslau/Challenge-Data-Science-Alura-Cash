# Challenge de Data Science

O Banco Digital Internacional fictício **Alura Cash** está tendo problemas com clientes inadimplentes. Para resolver esse problema foi proposto
uma análise dos dados dos clientes, tendo como objetivo indentificar padrões e uma possível inadimplencia.

Durante 4 semanas os dados serão analisados e entendidos a fim de criar um modelo de Machine Learning para classificar potenciais clientes inadimplentes
e resolver o problema da **Alura Cash**.

## Semana 01 - Tratamento de dados: entendendo como tratar dados com SQL

Para esse projeto será utilizado o [Cookiecutter](https://www.cookiecutter.io/), para criação e organização dos diretórios do projeto. Abaixo pode ser visto 
como esta organização será feita.

Organização do Projeto
------------

    ├── LICENSE
    ├── Makefile           <- Makefile com comandos como `make data` ou `make train`
    ├── README.md          <- O README de nível superior para desenvolvedores que usam este projeto.
    ├── data
    │   ├── external       <- Dados de fontes de terceiros.
    │   ├── interim        <- Dados intermediários que foram transformados.
    │   ├── processed      <- Os conjuntos de dados canônicos finais para modelagem.
    │   └── raw            <- O dump de dados original e imutável.
    │
    ├── docs               <- Um projeto Sphinx padrão; veja sphinx-doc.org para detalhes.
    │
    ├── models             <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos.
    │
    ├── notebooks          <- Jupyter notebooks. A convenção de nomenclatura é um número (para ordenação),
    │                         as iniciais do criador e uma breve descrição delimitada por `-`, ex:
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Dicionários de dados, manuais, e todos os outros materiais explicativos.
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos gerados e figuras para serem usadas em relatórios.
    │
    ├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise, e.x.
    │                         gerado como `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Torna o projeto pip instalável (pip install -e .) então src pode ser importado
    ├── src                <- Código fonte para uso neste projeto.
    │   ├── __init__.py    <- Faz src um módulo Python.
    │   │
    │   ├── data           <- Scripts para download ou geração de dados
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar dados brutos em recursos para modelagem
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para treinar modelos e então usar modelos treinados para criar
    │   │   │                 predições
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para criar visualizações exploratórias e orientadas a resultados
    │       └── visualize.py
    │
    └── tox.ini            <- tox arquivo com configurações para execução tox; see tox.readthedocs.io
    
<p><small>O projeto será baseado no template <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. </small></p>
    

Na primeira semana com o arquivo do tipo **Dump** disponibilizado pelo setor financeiro da **Alura Cash** e utilizando o [MySQL Workbench](https://www.mysql.com/products/workbench/)
foi criado um banco de dados com informações dos clientes. As informações dos clientes estão divididas em 4 tabelas.

Para um maior entendimento dos dados, foi fornecido um [Dicionário de Dados](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/references/Dicionario_de_Dados.md) detalhando o que cada coluna do banco de dados representa.

Foram efetuados alguns tratamentos nos dados, como por exemplo, a alteração de tipos de dados das colunas, tradução das colunas e de registros. 
O arquivo detalhado pode ser visto nesse [link](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/src/features/tratamento_sql.sql).

Ao final do tratamento, foi criada uma unica tabela que contém dados dos clientes, essa tabela foi exportada para um arquivo [.csv](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/tree/master/data/interim),
que será utilizado durante as próximas semanas do desafio.

## Semana 02 - Aprendendo com os dados: criando um modelo de previsão de inadimplência

Duarante essa semana foi feita uma limpeza mais completa nos dados, como remoção de dados nulos e de outliers. O processo detalhado pode ser visto nesse [notebook](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/notebooks/Notebook_01_Limpeza_de_Dados.ipynb).

Foram gerados alguns gráficos para maior entendimento dos dados, nesse [notebook](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/notebooks/Notebook_02_Vizualiza%C3%A7%C3%A3o_de_Dados.ipynb).

E por fim foram criados modelos de classificação e medidos seus desempenhos, o melhor deles foi melhorado com hiperparâmetros, os processos detalhados estão [aqui](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/notebooks/Notebook_03_Modelos_Machine_Learning.ipynb).

O modelo final foi exportado para o [diretório](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/tree/master/models).

## Semanas 03 e 04 - Analisando métricas: criando visualizações com o Power BI

As semanas 03 e 04 tiveram como foco a apresentação das métricas e resultados do trabalho desenvolvido anteriormente. Além de apresentação da solucão final.

Inicialmente foi desenvolvida uma [API](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/models/api_modelo.py), para que o modelo de classificação esteja disponível para consumo. A API foi desenvolvida com a linguagem de programação Python juntamente com a biblioteca [FastAPI](https://fastapi.tiangolo.com/).

Para exibição e consulta dos resultados foi utilizado o [Power BI](https://powerbi.microsoft.com/pt-br/), com esse foi possível a vizualização dos resultados do modelo e além de consultar algumas informações de clientes existentes nos cadastros da empresa. O dashboard final pode ser visto abaixo:

[![dashbord](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/reports/figures/modelo_print.png)](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/tree/master/reports)

Com isso o problema de de classificação da **Alura Cash** foi resolvido, pois agora a mesma consegue identificar potenciais clientes que podem ser inadimplentes.


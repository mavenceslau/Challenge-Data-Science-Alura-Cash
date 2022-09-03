# Challenge de Data Science

O Banco Digital Internacional fictício **Alura Cash** está tendo problemas com clientes inadimplentes. Para resolver esse problema foi proposto
uma análise dos dados dos clientes, tendo como objetivo indentificar padrões e uma possível inadimplencia.

Durante 4 semanas os dados serão analisados e entendidos a fim de criar um modelo de Machine Learning para classificar potenciais clientes inadimplentes
e resolver o problema da **Alura Cash**.

## Semana 1 - Tratamento de dados: entendendo como tratar dados com SQL

Para esse projeto será utilizado o [Cookiecutter](https://www.cookiecutter.io/), para criação e organização dos diretórios do projeto. Abaixo pode ser visto 
como esta organização será feita.

Organização do Projeto
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    
<p><small>O projeto será baseado no template <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. </small></p>
    

Na primeira semana com o arquivo do tipo **Dump** disponibilizado pelo setor financeiro da **Alura Cash** e utilizando o [MySQL Workbench](https://www.mysql.com/products/workbench/)
foi criado um banco de dados com informações dos clientes. As informações dos clientes estão divididas em 4 tabelas.
Foram efetuados alguns tratamentos nos dados, como por exemplo, a alteração de tipos de dados das colunas, tradução das colunas e de registros. 
O arquivo detalhado pode ser visto nesse [link](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/blob/master/src/features/tratamento_sql.sql).
Ao final do tratamento, foi criada uma unica tabela que contém dados dos clientes, essa tabela foi exportada para um arquivo [.csv](https://github.com/mavenceslau/Challenge-Data-Science-Alura-Cash/tree/master/data/interim),
que será utilizado durante as próximas semanas do desafio.

## Semana 2 - Em construção

## Semana 3 - Em construção

## Semana 4 - Em construção

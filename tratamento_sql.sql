#Tratamento de Dados SQL

#Tradução das colunas
#Tabela dados_mutuarios

ALTER TABLE dados_mutuarios 
CHANGE person_id pessoa_id VARCHAR(16),
CHANGE person_age pessoa_idade INT,
CHANGE person_income pessoa_salario_anual float,
CHANGE person_home_ownership pessoa_status_propriedade varchar(16),
CHANGE person_emp_length pessoa_tempo_trabalho int;

#Tabela emprestimos

ALTER TABLE emprestimos
CHANGE loan_id emprestimo_id VARCHAR(16),
CHANGE loan_intent emprestimo_motivo VARCHAR(32),
CHANGE loan_grade emprestimo_pontuacao VARCHAR(1),
CHANGE loan_amnt emprestimo_valor_total float,
CHANGE loan_int_rate emprestimo_taxa_juros float,
CHANGE loan_status emprestimo_inadimplente bit(1),
CHANGE loan_percent_income emprestimo_renda_percentual float;

#Tabela historico_banco

ALTER TABLE historicos_banco
CHANGE cb_id historico_id VARCHAR(16),
CHANGE cb_person_default_on_file historico_inadimplencia VARCHAR(1),
CHANGE cb_person_cred_hist_length historico_tempo_credito int;

#Tabela id

ALTER TABLE id
CHANGE person_id pessoa_id VARCHAR(16),
CHANGE loan_id emprestimo_id VARCHAR(16),
CHANGE cb_id historico_id VARCHAR(16);

SELECT DISTINCT(pessoa_status_propriedade) FROM dados_mutuarios;

#Na query é verificado o registro, caso seja algum dos especificados a atualização
#do campo é feita, caso contrário o campo recebe vazio('').

UPDATE dados_mutuarios SET pessoa_status_propriedade = CASE
   WHEN pessoa_status_propriedade = 'Rent' THEN 'Alugada'
   WHEN pessoa_status_propriedade = 'Own' THEN 'Própria'
   WHEN pessoa_status_propriedade = 'Mortgage' THEN 'Hipotecada'
   WHEN pessoa_status_propriedade = 'Other' THEN 'Outros'
   ELSE ''
   END;

#Tabela emprestimos

#Verificar os registros unicos da culuna emprestimo_motivo 
SELECT distinct(emprestimo_motivo) FROM emprestimos;

#Na query é verificado o registro, caso seja algum dos especificados a atualização
#do campo é feita, caso contrário o campo recebe vazio('').

UPDATE emprestimos SET emprestimo_motivo = CASE
   WHEN emprestimo_motivo = 'Personal' THEN 'Pessoal'
   WHEN emprestimo_motivo = 'Education' THEN 'Educativo'
   WHEN emprestimo_motivo = 'Medical' THEN 'Médico'
   WHEN emprestimo_motivo = 'Venture' THEN 'Empreendimento'
   WHEN emprestimo_motivo = 'Homeimprovement' THEN 'Melhora do lar'
   WHEN emprestimo_motivo = 'Debtconsolidation' THEN 'Pagamento de débitos'
   ELSE ''
   END;
   
#Tabela historico_banco

#Verificar os registros unicos da culuna emprestimo_motivo 
select distinct(historico_inadimplencia) from historicos_banco;

#Na query é verificado o registro, caso seja algum dos especificados a atualização
#do campo é feita, caso contrário o campo recebe vazio('').

UPDATE historicos_banco SET historico_inadimplencia = CASE
	WHEN historico_inadimplencia = 'N' THEN 'N'
    WHEN historico_inadimplencia = 'Y' THEN 'S'
    ELSE ''
    END;
   
# Criação de chaves primarias nas tabelas
# Na tabela dados_mutuaris existem dados na pessoa_id em branco, assim imposibilitando a 
#criação de chave primaria no campo(Chave primária representa registro unico). 

ALTER TABLE dados_mutuarios ADD PRIMARY KEY (pessoa_id);
ALTER TABLE emprestimos ADD PRIMARY KEY(emprestimo_id);
ALTER TABLE historicos_banco ADD PRIMARY KEY(historico_id);

#União das tabelas dados_mutuarios, emprestimos e historicos_banco através dos ids da tabela id,
#foi utilizado o inner join.

SELECT 
    M.pessoa_idade,
    M.pessoa_salario_anual,
    M.pessoa_status_propriedade,
    M.pessoa_tempo_trabalho,
    E.emprestimo_motivo,
    E.emprestimo_pontuacao,
    E.emprestimo_valor_total,
    E.emprestimo_taxa_juros,
    E.emprestimo_inadimplente,
    E.emprestimo_renda_percentual,
    H.historico_inadimplencia,
    H.historico_tempo_credito
FROM id AS I
INNER JOIN dados_mutuarios AS M ON I.pessoa_id = M.pessoa_id
INNER JOIN emprestimos AS E ON I.emprestimo_id = E.emprestimo_id
INNER JOIN historicos_banco AS H ON I.historico_id = H.historico_id;
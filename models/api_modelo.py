from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import pickle
import os
import pandas as pd

app = FastAPI(
    title = "API para classificação de inadimplência",
    version = 1.0,
    description = "APi para classificação de possiveis clientes inadimplentes."
)
   
#Rotas

@app.get('/')
def root():
    return {"Mensagem": "Bem vindo a API de Classificação de Clientes"}


@app.get('/predict/v1={pessoa_idade}&v2={pessoa_salario_anual}&v3={pessoa_status_propriedade}&v4={pessoa_tempo_trabalho}&v5={emprestimo_motivo}&v6={emprestimo_pontuacao}&v7={emprestimo_valor_total}&v8={emprestimo_taxa_juros}&v9={emprestimo_renda_percentual}&v10={historico_inadimplencia}&v11={historico_tempo_credito}')
def predict(pessoa_idade, pessoa_salario_anual, pessoa_status_propriedade, pessoa_tempo_trabalho, emprestimo_motivo, emprestimo_pontuacao,
            emprestimo_valor_total, emprestimo_taxa_juros, emprestimo_renda_percentual,
            historico_inadimplencia, historico_tempo_credito):
    
    data = {
        'pessoa_idade' : [int(pessoa_idade)], 
        'pessoa_salario_anual' : [float(pessoa_salario_anual)],
        'pessoa_status_propriedade' : [(pessoa_status_propriedade)],
        'pessoa_tempo_trabalho' : [int(pessoa_tempo_trabalho)],
        'emprestimo_motivo' : [(emprestimo_motivo)],
        'emprestimo_pontuacao' : [emprestimo_pontuacao],
        'emprestimo_valor_total' : [float(emprestimo_valor_total)],
        'emprestimo_taxa_juros' : [float(emprestimo_taxa_juros)],
        'emprestimo_renda_percentual' : [float(emprestimo_renda_percentual)],
        'historico_inadimplencia' : [int(historico_inadimplencia)],
        'historico_tempo_credito' : [float(historico_tempo_credito)]   
    }   
    
    colunas = ['pessoa_idade', 'pessoa_salario_anual', 'emprestimo_valor_total',
       'emprestimo_taxa_juros', 'pessoa_tempo_trabalho',
       'emprestimo_renda_percentual', 'historico_inadimplencia',
       'historico_tempo_credito', 'pessoa_status_propriedade_Alugada',
       'pessoa_status_propriedade_Hipotecada',
       'pessoa_status_propriedade_Outros', 'pessoa_status_propriedade_Própria',
       'emprestimo_motivo_Educativo', 'emprestimo_motivo_Empreendimento',
       'emprestimo_motivo_Melhora do lar', 'emprestimo_motivo_Médico',
       'emprestimo_motivo_Pagamento de débitos', 'emprestimo_motivo_Pessoal',
       'emprestimo_pontuacao_A', 'emprestimo_pontuacao_B',
       'emprestimo_pontuacao_C', 'emprestimo_pontuacao_D',
       'emprestimo_pontuacao_E', 'emprestimo_pontuacao_F',
       'emprestimo_pontuacao_G']
    
    data = pd.DataFrame(data)
    
    #Aplicando encoder
    ohe_model = open('models\one_hot_encoder.pkl', 'rb')
    ohe = pickle.load(ohe_model)
    data = ohe.transform(data)
    ohe_model.close() 
    
    data_final = pd.DataFrame(data, columns = colunas)
            
    #Escalando dados        
    scaler_model = open('models\scaler.pkl', 'rb')
    scaler = pickle.load(scaler_model)
    data_final = scaler.transform(data_final)
    scaler_model.close()    
        
    data_final = pd.DataFrame(data_final, columns = colunas)    
    
    #Fazendo previssão
    modelo = open('models\modelo_classificacao_inadimplencia.pkl', 'rb')
    classificador = pickle.load(modelo)
    modelo.close()    
        
    result = classificador.predict(data_final)[0]
    result_proba = classificador.predict_proba(data_final)
        
    if(result == 0):
        return JSONResponse({'Cliente' : 'Adimplente',
                             'Probabilidade': result_proba.tolist()[0][0]})
    else:
        return JSONResponse({'Cliente' : 'Inadimplente',
                             'Probabilidade': result_proba.tolist()[0][1]})
    
    """return JSONResponse({'Cliente': classificador.predict(data_final).tolist(),
                       'Probabilidade': result_proba.tolist()})"""

#Criando servidor local
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(
        app = app,
        host='127.0.0.1',
        port = port
    )
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
import pickle
import os
from pydantic import BaseModel
import pandas as pd


app = FastAPI(
    title = "API para classificação de inadimplência",
    version = 1.0,
    description = "APi para classificação de possiveis clientes inadimplentes."
)

class Cliente(BaseModel):
    pessoa_idade : int 
    pessoa_salario_anual : float
    pessoa_tempo_trabalho : int
    emprestimo_valor_total : float
    emprestimo_taxa_juros : float
    emprestimo_renda_percentual : float
    historico_inadimplencia : int
    historico_tempo_credito : float
    pessoa_status_propriedade_Alugada : int
    pessoa_status_propriedade_Hipotecada : int
    pessoa_status_propriedade_Outros : int
    pessoa_status_propriedade_Própria : int
    emprestimo_motivo_Educativo : int
    emprestimo_motivo_Empreendimento : int
    emprestimo_motivo_Melhora_do_lar : int 
    emprestimo_motivo_Medico : int
    emprestimo_motivo_Pagamento_de_débitos : int
    emprestimo_motivo_Pessoal : int
    emprestimo_pontuacao_A : int
    emprestimo_pontuacao_B : int
    emprestimo_pontuacao_C : int
    emprestimo_pontuacao_D : int
    emprestimo_pontuacao_E : int
    emprestimo_pontuacao_F : int 
    emprestimo_pontuacao_G : int

#Rotas

@app.get('/')
def root():
    return {"Mensagem": "Bem vindo a API de Classificação de Clientes"}


@app.post('/predict')
def predict(cliente : Cliente):
    data = pd.DataFrame(vars(cliente), index = [0])
            
    scaler_model = open('models\scaler.pkl', 'rb')
    scaler = pickle.load(scaler_model)
    data_final = scaler.transform(data)
    scaler_model.close()    
    
    modelo = open('models\modelo_classificacao_inadimplencia.pkl', 'rb')
    classificador = pickle.load(modelo)
    modelo.close()    
        
    result = classificador.predict(data_final)
    result_proba = classificador.predict_proba(data_final)
    
    #result_proba_json = jsonable_encoder(result_proba)
    
    if(result == 0):
        return JSONResponse({'Cliente': 'Adimplente'})
    else:
        return JSONResponse({'Cliente': 'Inadimplente'})

#Criando servidor local
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(
        app = app,
        host='127.0.0.1',
        port = port
    ) 

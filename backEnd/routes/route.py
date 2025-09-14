from fastapi import FastAPI
from pydantic import BaseModel
from helpers.leituraDados import ler_dados_csv
from helpers import regressaoMultipla
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["*"] para liberar para todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# Carregar dados e ajustar modelos ao iniciar
# ===============================
df = ler_dados_csv('data/Dataset Projeto IA.csv')

X = df[['Idade', 'Uso_Beber', 'Uso_Cozinhar', 'Arsenio_Agua']].values
y = df['Arsenio_Unhas'].values

# Modelo completo
beta = regressaoMultipla.regressao_linear_multipla(X, y, intercept=True)
y_pred = regressaoMultipla.prever(X, beta, intercept=True)

# Modelo alternativo (apenas arsênio na água)
X_alt = df[['Arsenio_Agua']].values
beta_alt = regressaoMultipla.regressao_linear_multipla(X_alt, y, intercept=True)
y_pred_alt = regressaoMultipla.prever(X_alt, beta_alt, intercept=True)

# ===============================
# Estrutura para entrada de dados
# ===============================
class PredInput(BaseModel):
    idade: float
    uso_beber: float
    uso_cozinhar: float
    arsenio_agua: float

# ===============================
# Endpoints
# ===============================
@app.get("/api/modelo")
def modelo():
    return {
    "coefficients": beta.tolist(),
    "r2": regressaoMultipla.r2(y, y_pred),
    "r2_adjusted": regressaoMultipla.r2_ajustado(y, y_pred, p=X.shape[1]),
    "rmse": regressaoMultipla.rmse(y, y_pred),
    "mse": regressaoMultipla.mse(y, y_pred),
    "mae": regressaoMultipla.mae(y, y_pred),
    }

@app.post("/api/predizer")
def predizer(data: PredInput):
    X_novo = np.array([[data.idade, data.uso_beber, data.uso_cozinhar, data.arsenio_agua]])
    y_novo = regressaoMultipla.prever(X_novo, beta, intercept=True)
    return {"previsao": float(y_novo[0])}

@app.get("/api/residuos")
def residuos():
    res = regressaoMultipla.residuos(y, y_pred)
    tabela = [
        {
            "obs": int(i+1),
            "y_observado": float(y[i]),
            "y_predito": float(y_pred[i]),
            "residuo": float(res[i])
        }
        for i in range(len(y))
    ]
    return tabela

@app.get("/api/modelo-alternativo")
def modelo_alternativo():
    return {
        "r2": regressaoMultipla.r2(y, y_pred_alt),
        "rmse": regressaoMultipla.rmse(y, y_pred_alt),
        "mse": regressaoMultipla.mse(y, y_pred_alt),
        "mae": regressaoMultipla.mae(y, y_pred_alt),
    }

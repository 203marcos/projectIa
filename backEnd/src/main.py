from helpers.leituraDados import ler_dados_csv
from helpers import regressaoMultipla
import pandas as pd
import numpy as np

# ===============================
# Leitura dos dados
# ===============================
df = ler_dados_csv('data/Dataset Projeto IA.csv')
X = df[['Idade', 'Uso_Beber', 'Uso_Cozinhar', 'Arsenio_Agua']].values
y = df['Arsenio_Unhas'].values

# ===============================
# (a) Regressão Linear Múltipla
# ===============================
print("=== (a) Regressão Linear Múltipla ===")
beta = regressaoMultipla.regressao_linear_multipla(X, y, intercept=True)
print("Coeficientes (com intercepto):", np.round(beta, 4))

# ===============================
# (b) Previsão para um exemplo
# ===============================
print("\n=== (b) Previsão de um exemplo ===")
novo_X = np.array([[30, 5, 5, 0.135]])
y_novo = regressaoMultipla.prever(novo_X, beta, intercept=True)
print("Previsão para [Idade=30, Uso_Beber=5, Uso_Cozinhar=5, Arsênio_Água=0.135]:", round(y_novo[0], 4))

# ===============================
# (d) R² e R² Ajustado
# ===============================
print("\n=== (d) R² e R² Ajustado ===")
y_pred = regressaoMultipla.prever(X, beta, intercept=True)
r2 = regressaoMultipla.r2(y, y_pred)
r2_adj = regressaoMultipla.r2_ajustado(y, y_pred, p=X.shape[1])
print("R²:", round(r2, 4))
print("R² Ajustado:", round(r2_adj, 4))

# ===============================
# (f) Modelo alternativo: somente Arsênio na água
# ===============================
print("\n=== (f) Modelo alternativo (apenas Arsênio na Água) ===")
X_alt = df[['Arsenio_Agua']].values
beta_alt = regressaoMultipla.regressao_linear_multipla(X_alt, y, intercept=True)
y_pred_alt = regressaoMultipla.prever(X_alt, beta_alt, intercept=True)
r2_alt = regressaoMultipla.r2(y, y_pred_alt)
print("R² (somente arsênio na água):", round(r2_alt, 4))
print("Modelo mais adequado:", "Completo" if r2 > r2_alt else "Alternativo")

# ===============================
# (f2) Resíduos
# ===============================
print("\n=== (f2) Resíduos do modelo completo ===")
res = regressaoMultipla.residuos(y, y_pred)
tabela_residuos = pd.DataFrame({
    "Obs": np.arange(1, len(y) + 1),
    "y_obs": y,
    "y_pred": y_pred,
    "Residuo": res
}).round(4)
print(tabela_residuos.to_string(index=False))

# ===============================
# (g) Modelo sem intercepto
# ===============================
print("\n=== (g) Modelo sem intercepto ===")
beta_zero = regressaoMultipla.regressao_linear_multipla(X, y, intercept=False)
y_pred_zero = regressaoMultipla.prever(X, beta_zero, intercept=False)
r2_zero = regressaoMultipla.r2(y, y_pred_zero)
print("R² (sem intercepto):", round(r2_zero, 4))

print("RMSE (com intercepto):", round(regressaoMultipla.rmse(y, y_pred), 4))
print("RMSE (sem intercepto):", round(regressaoMultipla.rmse(y, y_pred_zero), 4))

# ===============================
# (h) Outras métricas
# ===============================
print("\n=== (h) Outras métricas do modelo completo ===")
print("MSE:", round(regressaoMultipla.mse(y, y_pred), 4))
print("MAE:", round(regressaoMultipla.mae(y, y_pred), 4))

print("\n=== (h2) Outras métricas do modelo alternativo ===")
print("MSE:", round(regressaoMultipla.mse(y, y_pred_alt), 4))
print("MAE:", round(regressaoMultipla.mae(y, y_pred_alt), 4))

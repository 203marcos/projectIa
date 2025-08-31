from helpers.leituraDados import ler_dados_csv
from helpers import regressaoMultipla
import pandas as pd
import numpy as np

# (a) Ajuste do modelo de regressão linear múltipla
df = ler_dados_csv('data/Dataset Projeto IA.csv')
X = df[['Idade', 'Uso_Beber', 'Uso_Cozinhar', 'Arsenio_Agua']].values
y = df['Arsenio_Unhas'].values
beta = regressaoMultipla.regressao_linear_multipla(X, y, intercept=True)
print("a) Coeficientes do modelo (incluindo intercepto):", beta)

# (b) Previsão para novo caso
novo_X = np.array([[30, 5, 5, 0.135]])
y_novo = regressaoMultipla.prever(novo_X, beta, intercept=True)
print("\nb) Previsão para idade=30, beber=5, cozinhar=5, arsênio_agua=0.135:", round(y_novo[0], 4))

# (d) R² do modelo
y_pred = regressaoMultipla.prever(X, beta, intercept=True)
r2 = regressaoMultipla.coeficienteDeterminacao(y, y_pred)
print("\nd) R² do modelo:", round(r2, 4))

# (e) R² ajustado e explicação
r2_adj = regressaoMultipla.coeficienteDeterminacaoAjustado(y, y_pred, p=X.shape[1])
print("\ne) R² ajustado:", round(r2_adj, 4))
print("O R² ajustado penaliza o uso de variáveis irrelevantes. Se for maior que o R² comum, indica que as variáveis usadas são relevantes. Se for menor, pode haver variáveis desnecessárias.")

# (f) Modelo alternativo: apenas arsênio na água
X_alt = df[['Arsenio_Agua']].values
beta_alt = regressaoMultipla.regressao_linear_multipla(X_alt, y, intercept=True)
y_pred_alt = regressaoMultipla.prever(X_alt, beta_alt, intercept=True)
r2_alt = regressaoMultipla.coeficienteDeterminacao(y, y_pred_alt)
print("\nf) R² do modelo alternativo (apenas arsênio na água):", round(r2_alt, 4))
if r2 > r2_alt:
    print("O modelo completo é melhor (R² maior).")
else:
    print("O modelo alternativo é melhor (R² maior).")

# (f) Análise de resíduos
res = regressaoMultipla.residuos(y, y_pred)
tabela_residuos = pd.DataFrame({
    "Observação": np.arange(1, len(y) + 1),
    "Valor observado (y)": y,
    "Valor ajustado (ŷ)": y_pred,
    "Resíduo (e)": res
}).round(4)
print("\nTabela de resíduos (todas as observações):")
print(tabela_residuos.to_string(index=False))

# (g) Modelo com intercepto zero
beta_zero = regressaoMultipla.regressao_linear_multipla(X, y, intercept=False)
y_pred_zero = regressaoMultipla.prever(X, beta_zero, intercept=False)
r2_zero = regressaoMultipla.coeficienteDeterminacao(y, y_pred_zero)
rmse_zero = regressaoMultipla.rmse(y, y_pred_zero)
rmse_completo = regressaoMultipla.rmse(y, y_pred)
print("\ng) Modelo com intercepto zero:")
print("R²:", round(r2_zero, 4))
print("RMSE:", round(rmse_zero, 4))
print("RMSE do modelo com intercepto:", round(rmse_completo, 4))
print("Interpretando: Forçar intercepto zero significa assumir que, se todas as variáveis forem zero, o resultado também será zero. Escolha o modelo com menor RMSE e maior R².")

# (h) Outras métricas de erro
mse = regressaoMultipla.mse(y, y_pred)
mae = regressaoMultipla.mae(y, y_pred)
mse_alt = regressaoMultipla.mse(y, y_pred_alt)
mae_alt = regressaoMultipla.mae(y, y_pred_alt)
print("\nh) Outras métricas para o modelo completo:")
print("MSE:", round(mse, 4), "MAE:", round(mae, 4))
print("Para o modelo alternativo:")
print("MSE:", round(mse_alt, 4), "MAE:", round(mae_alt, 4))

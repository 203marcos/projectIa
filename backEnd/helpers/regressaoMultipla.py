import numpy as np

def regressao_linear_multipla(X, y, intercept=True):
    if intercept:
        X = np.column_stack((np.ones(X.shape[0]), X))
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    return beta

def prever(X, beta, intercept=True):
    if intercept:
        X = np.column_stack((np.ones(X.shape[0]), X))
    return X @ beta

def residuos(y, y_pred):
    return y - y_pred

def coeficienteDeterminacao(y, y_pred):
    ss_res = np.sum((y - y_pred)**2)
    ss_total = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_total)
    return r_squared

def coeficienteDeterminacaoAjustado(y, y_pred, p):
    n = len(y)
    r2 = coeficienteDeterminacao(y, y_pred)
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

def mse(y, y_pred):
    return np.mean((y - y_pred)**2)

def rmse(y, y_pred):
    return np.sqrt(mse(y, y_pred))

def mae(y, y_pred):
    return np.mean(np.abs(y - y_pred))

def equacao_regressao(beta, nomes_variaveis):
    """
    Retorna a equação da regressão linear múltipla como string.
    beta: array de coeficientes (incluindo intercepto)
    nomes_variaveis: lista com os nomes das variáveis preditoras
    """
    termos = [f"{beta[0]:.4f}"]  # Intercepto
    for i, nome in enumerate(nomes_variaveis):
        termos.append(f"{beta[i+1]:+.4f}*{nome}")
    return "Y = " + " ".join(termos)
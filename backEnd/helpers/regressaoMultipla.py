import numpy as np

def regressao_linear_multipla(X, y, intercept=True):
    if intercept:
        X = np.column_stack((np.ones(X.shape[0]), X))
    return np.linalg.inv(X.T @ X) @ X.T @ y

def prever(X, beta, intercept=True):
    if intercept:
        X = np.column_stack((np.ones(X.shape[0]), X))
    return X @ beta

def residuos(y, y_pred):
    return y - y_pred

def r2(y, y_pred):
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res/ss_tot

def r2_ajustado(y, y_pred, p):
    n = len(y)
    return 1 - (1 - r2(y, y_pred)) * (n - 1) / (n - p - 1)

def mse(y, y_pred):
    return np.mean((y - y_pred)**2)

def rmse(y, y_pred):
    return np.sqrt(mse(y, y_pred))

def mae(y, y_pred):
    return np.mean(np.abs(y - y_pred))

def equacao(beta, variaveis):
    eq = f"{beta[0]:.2f}"
    for i, nome in enumerate(variaveis):
        eq += f" {beta[i+1]:+.2f}*{nome}"
    return "Y = " + eq

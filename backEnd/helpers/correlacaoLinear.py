import numpy as np
import plotly.express as px

def pearsonFunction(x,y):
  x_mean = np.mean(x)
  y_mean = np.mean(y)
  numerador = np.sum((x - x_mean) * (y - y_mean))
  denominador = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
  pearson = numerador / denominador
  return pearson

def coeficienteAngular(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerador = np.sum((x - x_mean) * (y - y_mean))
    denominador = np.sum((x - x_mean)**2)
    a = numerador / denominador
    return a

def coeficienteLinear(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    a = coeficienteAngular(x, y)
    b = y_mean - a * x_mean
    return b

def equacaoRegressao(x, y):
    # y com chapeu...
    a = coeficienteAngular(x, y)
    b = coeficienteLinear(x, y)
    return a, b

def residuos(x, y):
    a, b = equacaoRegressao(x, y)
    y_hat = a * x + b
    residuos = y - y_hat
    return residuos

def coeficienteDeterminacao(x, y):  
    ss_res = np.sum(residuos(x, y)**2)
    ss_total = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_total)
    return r_squared

def somaQuadradosResiduos(x, y):
    sqr = np.sum(residuos(x, y)**2)
    return sqr

def plot_regressao(x, y):
    """
    Plota o grafico, precisa do pandas,statsmodels
    """
    fig = px.scatter(x=x, y=y, trendline="ols", labels={"x": "x", "y": "y"})
    fig.show()
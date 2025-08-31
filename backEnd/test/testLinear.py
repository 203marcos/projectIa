import numpy as np
from helpers import correlacaoLinear

x = np.array([1, 2, 3])
y = np.array([1, 4, 8])

print("Teste para iniciar o projeto de IA, comecei pela aula 04 -> Regressão Linear \n ")

print("Coeficiente de Pearson:", correlacaoLinear.pearsonFunction(x, y))
print("Coeficiente Angular (a):", correlacaoLinear.coeficienteAngular(x, y))
print("Coeficiente Linear (b):", correlacaoLinear.coeficienteLinear(x, y))
print("Equação da Regressão (a, b):", correlacaoLinear.equacaoRegressao(x, y))
print(f"Equação da Regressão: y = {correlacaoLinear.coeficienteAngular(x, y)}x + {correlacaoLinear.coeficienteLinear(x, y)}")
print("Resíduos:", correlacaoLinear.residuos(x, y))
print("Coeficiente de Determinação (R²):", correlacaoLinear.coeficienteDeterminacao(x, y))
print("Soma dos Quadrados dos Resíduos (SQR):", correlacaoLinear.somaQuadradosResiduos(x, y))
correlacaoLinear.plot_regressao(x, y)
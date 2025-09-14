# Project: Arsenic Concentration Regression

This repository presents an implementation of **multiple linear regression** to analyze the relationship between arsenic concentration in nails and various predictors from a real dataset. The code is organized into separate files for clarity and modularity.

## File Structure

```
├── src/
│   └── main.py                # Main script: loads data, fits models, makes predictions, and prints metrics
├── helpers/
│   └── regressaoMultipla.py   # Functions for regression, prediction, residuals, and error metrics
└── data/
  └── Dataset Projeto IA.csv   # Dataset with participant information and measurements
```

## What is Multiple Linear Regression?

Multiple linear regression is a statistical technique used to model the relationship between a dependent variable and two or more independent variables. It estimates how each predictor influences the outcome, enabling predictions and analysis of variable importance.

- **Dependent variable:** Arsenic concentration in nails
- **Predictors:** Age, water used for drinking, water used for cooking, arsenic concentration in water

## Main Script Functionality (`src/main.py`)

1. **Loads the dataset** and selects relevant columns.
2. **Fits the multiple linear regression model** using `numpy`, with and without intercept.
3. **Predicts arsenic concentration in nails** for a specific example.
4. **Calculates evaluation metrics:** R², adjusted R², MSE, RMSE, and MAE.
5. **Compares the full model** with an alternative model using only arsenic concentration in water as a predictor.
6. **Prints residuals** for each observation in a table format.
7. **Compares models with and without intercept** and discusses practical interpretation.

## Regression Functions Functionality (`helpers/regressaoMultipla.py`)

- `regressao_linear_multipla`: Fits the model and returns coefficients.
- `prever`: Makes predictions with the fitted model.
- `residuos`: Calculates residuals (difference between observed and predicted).
- `r2`, `r2_ajustado`: Calculate R² and adjusted R² metrics.
- `mse`, `rmse`, `mae`: Calculate error metrics for model evaluation.

---

This project demonstrates how to implement and interpret multiple linear regression **from scratch**, without using ready-made libraries like `sklearn`. All calculations are performed with `numpy`. The code is modular and can be adapted for similar regression problems.

Author: Marcos Dias
<!-- ABOUT THE PROJECT -->

## About The Project
<div id="readme-top"></div>

![XGBoost Overview](https://upload.wikimedia.org/wikipedia/commons/6/69/XGBoost_logo.png)

# XGBoost (Extreme Gradient Boosting)
### Theory, Objective Function, and Training Pipeline

This document provides a **structured, conceptual overview of XGBoost**, a high-performance implementation of **gradient-boosted decision trees**.  
It explains the **boosting philosophy**, **regularized objective function**, and the **iterative training algorithm** used to build strong predictive models from weak learners.

XGBoost is widely used in **tabular data modeling**, **risk prediction**, **ranking systems**, and **large-scale production ML pipelines** due to its speed, accuracy, and regularization capabilities.

---

<b>Table 1 – Machine Learning Project Archetype</b>

| Type              | Sub Type                     | Concept                                                             |
|-------------------|------------------------------|----------------------------------------------------------------------|
| Machine Learning  | Supervised Learning           | Regression & Classification                                         |
| Machine Learning  | Ensemble Methods              | Boosting, Weak Learners, Additive Models                             |
| Machine Learning  | Optimization                  | Gradient Descent on Loss Function                                    |
| Machine Learning  | Regularization                | L1/L2 Penalties, Tree Complexity Control                              |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Overview

### What Is XGBoost?

XGBoost is an **additive ensemble model** that builds a sequence of decision trees, where **each new tree corrects the errors of the previous ensemble** by fitting to the gradient of the loss function.

Key characteristics:

- Tree-based weak learners  
- Gradient-based optimization  
- Explicit regularization  
- Highly parallelizable and scalable  

---

## Boosting Intuition

### Additive Model Formulation

The prediction at iteration \( t \) is:

![](https://latex.codecogs.com/png.latex?\hat{y}^{(t)}=\sum_{k=1}^{t}f_k(x))

Where:
- \( f_k \) is a decision tree  
- Each tree incrementally improves the model  

Unlike bagging, trees are built **sequentially**, not independently.

---

## Objective Function

XGBoost minimizes a **regularized objective**:

![](https://latex.codecogs.com/png.latex?\mathcal{L}=\sum_{i}l(y_i,\hat{y}_i)+\sum_{k}\Omega(f_k))

### Loss Term

Measures prediction error (e.g., squared error, log loss):

![](https://latex.codecogs.com/png.latex?l(y,\hat{y}))

### Regularization Term

Controls model complexity:

![](https://latex.codecogs.com/png.latex?\Omega(f)=\gamma T+\frac{1}{2}\lambda\sum_jw_j^2)

Where:
- \( T \) = number of leaves  
- \( w_j \) = leaf weights  
- \( \gamma \) penalizes tree size  
- \( \lambda \) penalizes large weights  

---

## Gradient & Hessian Approximation

XGBoost uses a second-order Taylor expansion of the loss:

![](https://latex.codecogs.com/png.latex?l\!\left(y_i,\hat{y}_i^{(t-1)}+f_t(x_i)\right)\approx l\!\left(y_i,\hat{y}_i^{(t-1)}\right)+g_i\,f_t(x_i)+\frac{1}{2}h_i\,f_t(x_i)^2)

Where:

![](https://latex.codecogs.com/png.latex?g_i=\left.\frac{\partial l\!\left(y_i,\hat{y}\right)}{\partial\hat{y}}\right|_{\hat{y}=\hat{y}_i^{(t-1)}}\;\text{(first-order gradient)})

![](https://latex.codecogs.com/png.latex?h_i=\left.\frac{\partial^2 l\!\left(y_i,\hat{y}\right)}{\partial\hat{y}^2}\right|_{\hat{y}=\hat{y}_i^{(t-1)}}\;\text{(second-order Hessian)})


This improves:

- Convergence speed  
- Split quality  
- Numerical stability  

---

## Tree Construction

### Split Gain Formula

A split is chosen by maximizing **gain**:

![](https://latex.codecogs.com/png.latex?\text{Gain}=\frac{1}{2}\left[\frac{G_L^2}{H_L+\lambda}+\frac{G_R^2}{H_R+\lambda}-\frac{(G_L+G_R)^2}{H_L+H_R+\lambda}\right]-\gamma)

Where:
- \( G \) = sum of gradients  
- \( H \) = sum of Hessians  

Splits that do not exceed \( \gamma \) are pruned.

---

## Training Pipeline

### 1. Initialize Predictions
Start with a constant prediction (e.g., mean for regression).

---

### 2. Compute Gradients
Evaluate gradients and Hessians for all samples.

---

### 3. Build Tree
- Greedy split selection  
- Gain-based pruning  
- Leaf weight optimization  

---

### 4. Update Ensemble

![](https://latex.codecogs.com/png.latex?\hat{y}^{(t)}=\hat{y}^{(t-1)}+\eta f_t(x))

Where:
- \( \eta \) = learning rate  

---

### 5. Repeat
Continue until:
- Maximum rounds reached  
- Validation loss stops improving  

---

## Regularization & Overfitting Control

XGBoost combats overfitting using:

- Learning rate (shrinkage)  
- Maximum tree depth  
- Minimum child weight  
- Column subsampling  
- Row subsampling  
- Explicit L1/L2 penalties  

---

## Applications

Common real-world uses:

- Credit risk & fraud detection  
- Tabular medical data modeling  
- Ranking & recommendation systems  
- Time-series feature-based prediction  
- Structured data competitions (e.g., Kaggle)  

---

## Key Takeaways

- XGBoost is **gradient descent in function space**  
- Trees are optimized using **second-order statistics**  
- Regularization is built directly into the objective  
- Especially effective on **structured/tabular data**  

---

## Acknowledgements

- Tianqi Chen & Carlos Guestrin, *XGBoost: A Scalable Tree Boosting System*  
- Jerome Friedman, *Greedy Function Approximation: A Gradient Boosting Machine*
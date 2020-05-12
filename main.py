import numpy as np
from scipy.linalg import norm
from sys import exit
from ADMM import ADMM
from prediction import new_W, new_Y

# load pre-processed datasets as numpy arrays
X =                      # feature matrix of K days
X_new =                  # feature matrix of the K+1 th day
Y =                      # target matrix
Y_new =                  # target vector of the K+1 th day
D =                      # distance matrix
K,M,N = X.shape
if not Y.shape = (N,K):
    print("X and Y are of incompatible shapes.")
    exit()
if not D.shape==(N,N):
    print("X and D are of incompatible shapes.")
    exit()


# input parameters
h = 1          # control the degree of inter-region spatial correlation
lam = 1        # control the contribution of intra-region temporal correlation
rou = 2        # penality in ADMM algorithm
gamma = 0.1    # learning rate in ADMM algorithm
eps = 10**(-5) # the significance level
lags = 2       # the number of time slots to look back for predicting new weights


# predict from X, Y, D
res = ADMM(X, Y, D, h, lam, rou, gamma, eps)
print("Find optimized weights after", res["iterations"], "iterations.")
W = res["optimized weights"]
W_new = new_W(W, X, Y, lags)
y = new_Y(W_new, X_new)
print(norm(y-Y_new))
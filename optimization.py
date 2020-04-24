import numpy as np
import random
from numpy.linalg import norm
from scipy.optimize import minimize
from sys import exit

# calculate 0.5*||W^k P||_1
def Spatio(G, W_k):
    # G is an N-by-N array with each element a non-increasing function of distance d_ij 
    # W_k is the N -by-M feature matrix of the kth time slot
        
    # check the inputs
    if not G.shape[0]==G.shape[1]:
        print("G = ", G)
        exit()
    if not G.shape[0]==W_k.shape[0]:
        print("G = ", G)
        print("W^k = ", W_k)
        exit()
        
    N = G.shape[0]
    
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += G[i,j] * norm(W_k[i,:]-W_k[j,:], 1)
            
    return(sum/2)
    
    
    
# calculate sum of ||W_n Q||_1
def Tempo(lam, W):
    # lam is a scalar
    # W is a sequence of K feature matrices, each associated with the kth time slot and of shape N-by-M
    
    K =
    N = 
    
    sum = 0
    for k in range(K-1):
        for n in range(N):
            sum += norm(W[k][n]-W[k+1][n], 1)
            
    return(lam * sum)
    
    
    
# compute the objective function
def obj_func(W, X, Y, lam, G):
    # X and W are of the same shape
    # W is a sequence of K feature matrices, each associated with the kith time slot and of shape N-by-M
    # Y is an N-by-K array
    
    # check the inputs
    if not W.shape==X.shape:
        print("W = ", W)
        print("X = ", X)
        exit()
    R = random.choice(X)
    if not R.shape[0]==Y.shape[0]:
        print("Y = ", Y)
        print("one of the feature matrices =", R)
        exit()
        
    K = 
    N = 
    
    sum = Tempo(lam, W)
    for k in range(K):
        S = 0
        for n in range(N):
            S += (X[k][n].dot(W[k][n]) - Y[n,k])**2
        sum += S + Spatio(G, W[k])
    
    return(sum)
    
    
    
def W_opt(X,Y,lam,G):
    iter = 0
    while iter<5:
        # initialize W randomly
        W_0
    
        # minimize the objective function
        result = minimize(obj_func, x0=W_0, args=(X,Y,lam,G), )
        iter += 1
        
        if result.success:
            break
            
    if not result.success:
        print("Optimization diverges.")
    
    return(result.x)
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import norm
from sys import exit

def obj_func(Phi, Y, D):

    # Y is the N-by-K target matrix (array)
    # D is the N-by-N "distance" matrix (array)
    # Phi = [Phi_0, Phi_1, ... , Phi_T] is the vector of parameters (list or ndarray)
    
    if not D.shape[0]==D.shape[1]:
        print("D =", D)
        exit()
    if not Y.shape[0]==D.shape[0]:
        print("Y =", Y)
        print("D =", D)
        exit()
    if Y.shape[1]<len(Phi):
        print("Y =", Y)
        print("T =", len(Phi)-1)
        exit()
        
    T = len(Phi) - 1
    N,K = Y.shape
    c = Phi[0] * np.ones((N,1))
    
    loss = 0
    for j in range(T,K):
        y = Y[:,j].reshape((N,1))
        v = y - c 
        for tau in range(1,T+1):
            y = Y[:, j-tau].reshape((N,1))
            v = v - Phi[tau] * D.dot(y)
        loss += norm(v)
    return(loss / (K-T))
    
    
    
# find the parameters Phi that minimize the object function of STAR    
def STAR_pm(Y, D, T):
    phi = np.random.normal(loc=0, scale=1, size=T+1)
    result = minimize(obj_func, x0=phi, args=(Y,D,), )
    if not result.success:
        print("No convergence. Try again.")
        exit()
    return(result.x)
    
    
    
# predict with STAR
def STAR_predict(Y, D, Phi):

    if (not D.shape[0]==D.shape[1]) or (not Y.shape[0]==D.shape[0]) or Y.shape[1]<len(Phi):
        print("Invalid Function Parameters.")
        exit() 
        
    N,K = Y.shape
    T = len(Phi) - 1
    
    Y_new = Phi[0] * np.ones((N,1))
    for tau in range(1,T+1):
        y = Y[:,K-tau].reshape((N,1))
        Y_new = Y_new + Phi[tau] * D.dot(y)
        
    return(Y_new)
    
    
    
# predict the final day from the previous K-1 days
# compare truth with prediction
def STAR_analysis(Y, D, T):
    if (not D.shape[0]==D.shape[1]) or (not Y.shape[0]==D.shape[0]):
        print("Invalid Function Parameters.")
        exit() 
    K = Y.shape[1]
    Y_true = Y[:,-1]
    Y = Y[:,:K-1]
    Y_pred = STAR_predict(Y, D, Phi=STAR_pm(Y,D,T)).flatten()
    return(norm(Y_pred - Y_true))

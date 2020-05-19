import numpy as np
from scipy.optimize import minimize
from scipy.linalg import norm
from functions import RMSE
from sys import exit
from collections import namedtuple

def obj_func(Phi, Y, D, h):

    # Y is the N-by-K target matrix (array)
    # D is the N-by-N distance matrix (array)
    # h controls the degree of spatial correlation
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
    
    # transform D
    for i in range(N):
        for j in range(N):
            if not D[i,j]==0:
                D[i,j] = float(D[i,j])**(-h)
    
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
def STAR_pm(Y, D, T, h):
    phi = np.random.normal(loc=0, scale=1, size=T+1)
    result = minimize(obj_func, x0=phi, args=(Y,D,h), )
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
# compare truth with prediction and output RMSE
def STAR_analysis(Y, D, T, h):
    if (not D.shape[0]==D.shape[1]) or (not Y.shape[0]==D.shape[0]):
        print("Invalid Function Parameters.")
        exit() 
    K = Y.shape[1]
    Y_true = Y[:,-1]
    Y = Y[:,:K-1]
    Y_pred = STAR_predict(Y, D, Phi=STAR_pm(Y,D,T,h)).flatten()
    return(RMSE(Y_pred - Y_true))
    
    
    
    
    
# pipeline everything above into a Class (STAR model)
class STAR:
    def __init__(self):
        print("A STAR model is constructed.")
    
    def fit(self, Y, D, h, T):
        self.coef = STAR_pm(Y, D, T, h)
        self.data = Y
        self.distance = D
        self.lags = T 
        self.spatio_degree = h
   
    def get_params(self):
        Coef = namedtuple("Coefficients", ["Phi_"+str(j) for j in range(1+self.lags)])
        return(Coef(*self.coef))
    
    def predict(self):
        self.pred = STAR_predict(self.data, self.distance, self.coef).flatten()
    
    def analysis(self):
        self.rmse = STAR_analysis(self.data, self.distance, self.lags, self.spatio_degree)
        
    def __del__(self):
        print("This STAR model is destructed.")
    
        
       
# test
Y = np.random.rand(9,100)
D = np.random.randint(0,5,(9,9))
h = 1
T = 2
Phi = STAR_pm(Y,D,T,h)
print(Phi)
model = STAR()
model.fit(Y,D,h,T)
phi = model.get_params()
print(phi)
model.predict()
model.analysis()
print(model.coef)
print(model.pred)
print(model.rmse)
    
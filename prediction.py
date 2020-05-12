import numpy as np
from scipy.optimize import lsq_linear
from sys import exit

# use existing W to predict a new matrix W^(K+1)
def new_W(W, X, Y, lags, Combine=False):
	# W: optimized weights: W.shape = (K,M,N)
	# X: feature matrix: X.shape = (K,M,N)
	# Y: target matrix: Y.shape = (N,K)
	# lags: the number of time slots to look back for regression
	
    if not W.shape==X.shape:
        print("Shapes of X and W do not match:")
        print("The dimension of W =", W.shape)
        print("The dimension of X =", X.shape)
        exit()
    
    K,M,N = X.shape
    
    if not Y.shape==(N,K):
        print("Shapes of Y and W are incompatible:")
        print("The dimension of W =", W.shape)
        print("The dimension of Y =", Y.shape)
        exit()
    
    if lags<=0 or lags>=K:
        print("lags is bad input.")
        exit()
    
    NEW = np.zeros([M,N])       # new matrix W^(K+1)
    for n in range(N):
        # find alpha by regression
        PARA = np.zeros([K-lags, lags])
        row = 0
        for k in range(lags,K):
            PARA[row,:] = X[k,:,n].dot(W[(k-lags):k,:,n].transpose())
            row += 1
        TARG = Y[n,lags:]
        res = lsq_linear(PARA, TARG)
        # the nth column of W^(K+1)
        NEW[:,n] = W[K-lags:,:,n].transpose().dot(res.x)
        
    if Combine:
        NEW = np.vstack((W, NEW[None]))

    return(NEW)
    


def new_Y(W_new, X_new):
    # X_new: the new feature matrix X^(K+1)
    # W_new: the new weights matrix W^(K+1)
    
    if not W_new.shape==X_new.shape:
        print("Shapes of feature matrix and weights matrix do not match.")
        exit()
    
    M,N = X_new.shape
    
    y = list()
    for n in range(N):
        y.append(X_new[:,n].dot(W_new[:,n]))
    y = np.array(y)
    
    return(y)
    

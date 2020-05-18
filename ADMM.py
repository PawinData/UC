import numpy as np
from numpy.random import rand, randint, normal
from scipy.linalg import norm
from time import process_time
from collections import namedtuple
from functions import generate_P, generate_Q, S



def ADMM(X, Y, D, h=1, lam=1, rou=2, gamma=0.01, eps=10**(-5)):
	# X is a 3D array: X.shape = (K,M,N)
	# Y is a 2D array: Y.shape = (N,K)
	# D is an N-by-N distance matrix
	# h is non-negative, controlling the degree of spatial correlation
	# lam is non-negative, controlling the contribution of intra-region temporal correlation
	# rou >= 0 penalizes the deviation of E from W^k*P and F from W_n*Q
	# gamma >= 0 is the learning rate
	# eps >= 0 is the threshold of significance
    
    t1 = process_time()
    
    K,M,N = X.shape
    P = generate_P(D, h)   # generate P and Q
    Q = generate_Q(K, lam)
    
    
    def L(W, E, F, U, V):     # rewrite the loss function
        loss = 0
        
        for k in range(K):
            for n in range(N):
                loss += (X[k,:,n].dot(W[k,:,n]) - Y[n,k])**2
                
        for k in range(K):
            loss += norm(E[k,:,:],1)/2
            
        for k in range(K):
            loss += norm(W[k,:,:].dot(P) - E[k,:,:] + U[k,:,:]) * rou / 2
            
        for n in range(N):
            loss += norm(F[:,:,n], 1)
            
        for n in range(N):
            loss += norm(W[:,:,n].transpose().dot(Q) - F[:,:,n] + V[:,:,n]) * rou / 2
        
        return(loss)    
        
    
    def grad_L(W, E, F, U, V, k, n):     # gradient column of loss function with respect to specific W_n^k
        col1 = X[k,:,n].dot(W[k,:,n]) - Y[n,k]
        col1 = 2 * col1 * X[k,:,n].transpose()
        
        col2 = W[k,:,:].dot(P) - E[k,:,:] + U[k,:,:]
        col2 = rou * col2.dot(P[n,:].transpose())
        
        col3 = W[:,:,n].transpose().dot(Q) - F[:,:,n] + V[:,:,n]
        col3 = rou * col3.dot(Q[k,:].transpose())
        
        return(col1 + col2 + col3)

    
    pre = 0     # initialize parameters
    W = normal(loc=0, scale=1, size=(K,M,N))
    E = normal(loc=0, scale=1, size=(K, M, N**2))
    U = normal(loc=0, scale=1, size=(K, M, N**2))
    F = normal(loc=0, scale=1, size=(M, K-1, N))
    V = normal(loc=0, scale=1, size=(M, K-1, N))
    now = L(W, E, F, U, V)
    
    num_iter = 0
    while norm(pre - now) >= eps and num_iter<1000*N*K:
        pre = now
        k = randint(0,K)
        n = randint(0,N) 
        W[k,:,n] = W[k,:,n] - gamma * grad_L(W, E, F, U, V, k, n)   # update W
        E[k,:,:] = S(W[k,:,:].dot(P)+U[k,:,:], 0.5/rou)       # update E,F,U,V
        F[:,:,n] = S(W[:,:,n].transpose().dot(Q)+V[:,:,n], 1/rou)
        U[k,:,:] = U[k,:,:] + W[k,:,:].dot(P) - E[k,:,:]
        V[:,:,n] = V[:,:,n] + W[:,:,n].transpose().dot(Q) - F[:,:,n]
        now = L(W, E, F, U, V)    # update the loss 
        num_iter += 1
        
    t2 = process_time()
    
    Results = namedtuple("Results", ["iterations", "Loss", "Weights", "time"])
    res = Results(num_iter, now, W, t2-t1)
    
    #results = {"iterations":num_iter, "optimized loss":now, "optimized weights":W, "time":(t2-t1)}
    
    return(res)


# Test
X = normal(loc=0, scale=1, size=(100,30,9))
Y = normal(loc=0, scale=1, size=(9,100))
D = rand(9,9)
res = ADMM(X,Y,D)
print(res)
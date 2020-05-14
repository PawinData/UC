import re
import random
import math
import pickle
import numpy as np
from sys import exit

# convert a date from string to integer (the kth day in 2020)
def str_to_day(DATE):
    # extract month and day from the string
    month = re.findall('^2020-([0-9]+)-', DATE)
    month = int(month[0])
    day = re.findall('^2020-[0-9]+-([0-9]+)', DATE)
    day = int(day[0])
    # how many days in each month of 2020
    calendar = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # compute the number of days in 2020 until the DATE
    DAY = day
    for mm in range(1,month):
        DAY += calendar[mm]
    return DAY


# convert a date from integer to string
def day_to_str(DAY):
     # how many days in each month of 2020
    calendar = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # compute month and day of a date
    month = 1
    day = DAY - calendar[1]
    while day>0:
        month += 1
        day -= calendar[month]
    day += calendar[month]
    # formulate the string
    if month<10:
        month = "0"+str(month)
    else:
        month = str(month)
    if day<10:
        day = "0"+str(day)
    else:
        day = str(day)
    return("2020-"+month+"-"+day)


# randomly walk to an adjacent county from the current county
def random_step(Now, AdjM):
    options = list()
    for node in AdjM:
        if AdjM[Now][node]==1:
            options.append(node)
    return(random.choice(options))


# randomly walk from A to B and count the number of crossing borders
def random_path(A, B, AdjM):
    Now = A
    steps = 0
    while True:
        Now = random_step(Now, AdjM)
        steps += 1
        if Now==B:
            break
    return(steps)


# find the shortest path between two counties stochastically
def shortest_path(AdjM, A, B):
    # AdjM is the adjacency dataframe
    if A==B:
        return(0)
    elif AdjM[A][B]==1:
        return(1)
    else:
        distance = list()
        for i in range(100*len(AdjM.index)):
            distance.append(random_path(A,B,AdjM))
        return(min(distance))

    
# check whether the dates are incessant or not
def check_missing(date_list):
    time = [str_to_day(dd) for dd in date_list]
    if time[-1]-time[0]+1==len(time):
        return(True)
    else:
        return(False)
        
        
# compute the squared magnitude of a vector
def RMSE(error_vector):
    M = 0
    for ele in error_vector:
        M += ele**2
    M /= len(error_vector)
    M = math.sqrt(M)
    return(M)
    
    
    
# cut out the dataframe within a certain time window
def cut_DF(DF, start, end):
    lst = list()
    Start = str_to_day(start)
    End = str_to_day(end)
    for element in DF.columns:
        if str_to_day(element)<Start:
            continue
        if str_to_day(element)>End:
            break
        lst.append(element)
    return(DF[lst])
    
    
    
# generate P from distance matrix and h 
def generate_P(D, h):
    # D: distance matrix
    # h: control the degree of spatial correlation
    if not D.shape[0]==D.shape[1]:
        print("D is not a distance matrix.")
        exit()
    N = D.shape[0]
    P = np.zeros([N, N**2])      # P is an N-by-N^2 matrix
    for i in range(N):
        for j in range(N):
            if not i==j:
                P[i, j + N*(i-1)] = float(D[i,j])**(-h)
                P[j, j + N*(i-1)] = -float(D[i,j])**(-h)
    return(P)
    
    
    
# generate Q 
def generate_Q(K, lam):
    Q = np.zeros([K, K-1])   # Q is a K-by-(K-1) matrix
    for k in range(K-1):
        Q[k, k] = lam
        Q[k+1,k] = -lam
    return(Q)
    
    
# soft thresholding operator
def S(A, alpha):
    # A is a matrix
    # alpha is a scalar threshold
    if alpha<0:
        print("alpha has to be non-negative.")
        exit()
    B = np.zeros(A.shape)
    rows, cols = A.shape
    for i in range(rows):
        for j in range(cols):
            ele = A[i,j]
            if ele > alpha:
                B[i,j] = ele - alpha
            elif ele < -alpha:
                B[i,j] = ele + alpha
            else:
                B[i,j] = 0
    return(B)
    
    
    
# obtain feature arrays within certain time window from path
def obtain_Features(path, start, end):
    D = pickle.load(open(path,"rb"))   # a dictionary of (date, feature dataframe)
    time_window = [day_to_str(day) for day in range(str_to_day(start), 1+str_to_day(end))]  # a list of dates
    X = np.array([D[date].to_numpy() for date in time_window])
    return(X)
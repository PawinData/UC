import matplotlib.pyplot as plt
import numpy as np
from random import choices
from collections import deque
from time import process_time
from pickle import dump, load

TimeSeries = load(open("Time_Series.p","rb"))

def Autocorrelation(time_series, lag):
    original = deque(time_series)
    new = original.copy()
    new.rotate(lag)
    avg = np.mean(original)
    autocorr = 0
    for i in range(len(original)):
        autocorr += (original[i] - avg) * (new[i] - avg)
    return autocorr/lag
    


Comp_Time = process_time()

acf = list()
for tau in range(1, 1+len(TimeSeries)):
    acf.append(Autocorrelation(TimeSeries, lag=tau))
    
Comp_Time += process_time() - Comp_Time
Comp_Time /= len(TimeSeries)

dump(acf, open("acf.p","wb"))
dump(Comp_Time, open("Comp_Time.p","wb"))
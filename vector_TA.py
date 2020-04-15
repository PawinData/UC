from statsmodels.tsa.statespace.varmax import VARMAX
from numpy.linalg import norm
import numpy as np
import pandas as pd

# treat the tempo-spatial data as multivariate time series
# use previous observations to predict the final day
# compare the results by squared root 


def vector_TA(DF, PRINT=True):
    data = list()	
    for date in DF.columns:
        data.append(list(DF[date]))
	
	# fit model
    model = VARMAX(data[:len(data)-1], order=(1,1))
    model_fit = model.fit(disp=False)
	
	# predict
    y_hat = model_fit.forecast()
	
    if PRINT:
        D = {"Prediction":y_hat[0], "Truth":data[-1]}
        df = pd.DataFrame(D, index=DF.index)
        print(df)
		
	# compute the maginitude of the difference between prediction and truth
    x = np.array(y_hat)
    x = x - np.array(data[-1])
    
    return(norm(x))
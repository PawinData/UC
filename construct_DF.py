import pandas as pd
import numpy as np
from functions import str_to_day, day_to_str

# load data about a list of counties in a state 
# reconstruct in such a manner that each row is essentially a time series for each county of 
# the number of new confirmed cases per 1 million population each day

def construct_DF(url, STATE, COUNTIES, INFO):
    df = pd.read_csv(url)
    df = df.loc[df["state"]==STATE]
    # extract data for a list of counties
    DATA = pd.DataFrame(df.loc[df['county']==COUNTIES[0]], index=None)
    for cnty in COUNTIES[1:]:
        DATA = DATA.append(df.loc[df["county"]==cnty], ignore_index=True)   
    
    # extract all the dates that are reported
    t = list(DATA["date"])
    t.sort()
    
    # reorganize the data for the TCP framework
    T = list()
    START = dict()
    for cnty in COUNTIES:
        data = DATA.loc[DATA["county"]==cnty]
        time = [str_to_day(dd) for dd in data["date"]]
        # record the date when the first case was confirmed in each county
        START[cnty] = time[0] 
        # number of cases per 1 million population   
        cases_count = [ele/(int(INFO[cnty]["Population"])*0.1**6) for ele in data["cases"]]
        # focus on daily new cases rather than total case count
        cases_count = [cases_count[0]] + [cases_count[i]-cases_count[i-1] for i in range(1,len(cases_count))]
        if time[0]>str_to_day(t[0]):
            cases_count = [0] * (time[0] - str_to_day(t[0])) + cases_count
        T.append(cases_count)

     # construct an array
     # each row is the time series of cases count for a county    
    TimeSeries = np.array(T)
    DF = pd.DataFrame(TimeSeries, index=COUNTIES, 
                      columns=[day_to_str(dd) for dd in range(str_to_day(t[0]),1+str_to_day(t[-1]))])
    return(DF)

import matplotlib.pyplot as plt
from functions import str_to_day, day_to_str

# plot the Temporal and Spatial structures of a DataFrame
# each row is a time series for a discrete location
# Spatial differences are measured against the Distance Matrix

def plot_Tempo_Spatio(DF, DistanceMatrix):

    START = dict()  # the day when the first case was confirmed in each county
    for cnty in DF.index:
        for date in DF.columns:
            if not DF[date][cnty]==0:
                START[cnty] = str_to_day(date)
                break
    
    t = [str_to_day(date) for date in DF.columns]
    H = dict()   # a histogram of pairwise delta t
    S = dict()   # sum of pairwise differences over all delta t
    '''
    for cnty in DF.index:               # loop through every county
        for t1 in range(START[cnty],1+t[-1]): 
            day1 = day_to_str(t1)            # for every two days
            for t2 in range(START[cnty],1+t[-1]):# compute the |diff| in number of new cases
                delta = abs(t1 - t2)
                if delta==0:
                    continue
                day2 = day_to_str(t2)
                H[delta] = H.get(delta,0) + 1    # count records (to compute average)
                # add up total |diff|
                S[delta] = S.get(delta,0) + abs(DF[day1][cnty] - DF[day2][cnty])
    '''
    for cnty in DF.index:
        for date1 in DF.columns:
            for date2 in DF.columns:
                if date1==date2:
                    continue
                delta = abs(str_to_day(date1) - str_to_day(date2))
                H[delta] = H.get(delta,0) + 1
                S[delta] = S.get(delta,0) + abs(DF[date1][cnty] - DF[date2][cnty])
            
    LST = list(H.keys())
    LST.sort()
            
            
    h = dict() # a histogram of pairwise distances
    s = dict() # sum of pairwise differences over all distances
    for date in DF.columns:
        for A in DF.index:
            for B in DF.index:
                if A==B:
                    continue
                d = DistanceMatrix[A][B]
                h[d] = h.get(d,0) + 1
                s[d] = s.get(d,0) + abs(DF[date][A] - DF[date][B])
     
    lst = list(h.keys())
    lst.sort()
    
    fig, axs = plt.subplots(1,2, figsize=(20,10))
    fig.suptitle("Tempo-Spatial Correlation", fontsize=25)

    # the subplot for Intra-Region Temporal Correlation
    axs[0].plot(LST, [int(S[delta])/int(H[delta]) for delta in LST])
    axs[0].set_title("Intra-Region Temporal Correlation", fontsize=20)
    axs[0].set_xlabel("$\Delta$ t", fontsize=20)
    axs[0].set_ylabel("$\Delta$ daily new cases", fontsize=20)

    # the subplot for Inter-Region Spatial Correlation
    axs[1].plot(lst, [int(s[delta])/int(h[delta]) for delta in lst], 'g')
    axs[1].set_title("Inter-Region Spatial Correlation", fontsize=20)
    axs[1].set_xlabel("$\Delta$ d", fontsize=20)
    axs[1].set_ylabel("$\Delta$ daily new cases", fontsize=20)

    plt.savefig("Tempo_Spatio.eps")
    plt.savefig("Tempo_Spatio.png")

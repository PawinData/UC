# UC
Modeling Temporal-Spatial Correlations for COVID-19 Prediction

This is the course project for **Urban Computing** (Spring 2020) at LIACS, Leiden University. We apply the TCP framework, originally proposed by [X. Zhao and J. Tang](https://doi.org/10.1145/3132847.3133024) to predict urban crime, to forecast the number of newly confirmed COVID-19 cases per one million population for each county in the San Francisco Bay Area every day and show that **TCP** almost surely outperforms the baseline, the Space-Time Auto-Regression (**STAR**) model, although STAR is often more robust and computationally convenient. The key idea is to look beyond the target itself and extract information from less significantly correlated, yet massive in volumn and convenient in accessibility features (e.g temperatures, unemployment, violations of social distancing e.t.c). Implementation and experiments are done with the [dataset](https://query.data.world/s/7ifvvpyy23sa2fciuvcygehakxlnnv) of US county-level daily case counts, released by *New York Times*, using Python.

This project has been added to Data Lake of [CoronaWhy](https://www.coronawhy.org/), a globally-distributed, volunteer-powered research organization trying to assist the medical community to answer key questions related to COVID-19.

1. Final table of TCP vs STAR performance analysis: [TCP_STAR.csv](https://github.com/PawinData/UC/blob/SFBA/TCP_STAR.csv)

2. To reproduce the results, run [main.ipynb](https://github.com/PawinData/UC/blob/SFBA/main.ipynb)

3. To check the implementation of TCP and STAR, go to [TCP.py](https://github.com/PawinData/UC/blob/SFBA/TCP.py) and [STAR.py](https://github.com/PawinData/UC/blob/SFBA/STAR.py). Optimization in TCP is carried out with the ADMM algorithm: [ADMM.py](https://github.com/PawinData/UC/blob/SFBA/ADMM.py)

4. Supporting functions can be found in [functions.py](https://github.com/PawinData/UC/blob/SFBA/functions.py) and [plot_Tempo_Spatio.py](https://github.com/PawinData/UC/blob/SFBA/plot_Tempo_Spatio.py)

5. To use the features integrated into our TCP framework, download [Features_raw.p](https://github.com/PawinData/UC/blob/SFBA/FEATURES_raw.p) or [Features_normal.p](https://github.com/PawinData/UC/blob/SFBA/FEATURES_normal.p). Pre-processing of the meteorological, demographic, and Foursquare features is included in the [Features](https://github.com/PawinData/UC/tree/SFBA/Features) folder.

6. Supporting datasets can be found in [AdjacencyMatrix.csv](https://github.com/PawinData/UC/blob/SFBA/AdjacencyMatrix.csv), [DistanceMatrix_shortestnetworks.csv](https://github.com/PawinData/UC/blob/SFBA/DistanceMatrix_shortestnetworks.csv), [DistanceMatrix_populous.csv](https://github.com/PawinData/UC/blob/SFBA/DistanceMatrix_populous.csv), and [INFO.csv](https://github.com/PawinData/UC/blob/SFBA/INFO.csv)

7. To review the preliminary analysis of this study, go to [Proposal.pdf](https://github.com/PawinData/UC/blob/SFBA/Proposal.pdf) and [Temporal_Spatial_validated.ipynb](https://github.com/PawinData/UC/blob/SFBA/Temporal_Spatial_validated.ipynb)


            
               |--- [TCP.py](https://github.com/PawinData/UC/blob/SFBA/TCP.py)
[main.ipynb](https://github.com/PawinData/UC/blob/SFBA/main.ipynb) ---|
               |--- [STAR.py](https://github.com/PawinData/UC/blob/SFBA/STAR.py)

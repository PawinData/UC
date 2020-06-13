# UC
Modeling Temporal-Spatial Correlations for COVID-19 Prediction

This is the course project for **Urban Computing** (Spring 2020) at LIACS, Leiden University. We apply the TCP framework, originally proposed to predict urban crime, to forecast the number of new COVID-19 confirmed cases per one million population for each county in the San Francisco Bay Area every day and show that **TCP** often outperforms the baseline, that is, the Space-Time Auto-Regression (**STAR**) model, although STAR is more robust and computationally convenient in most experiments. Implementation is done using Python.

This project has been added to [CoronaWhy Data Lake](https://www.coronawhy.org/), a globally-distributed, volunteer-powered research organization trying to assist the medical community to answer key questions related to COVID-19.

1. Final table of TCP vs STAR performance analysis: [TCP_STAR.csv](https://github.com/PawinData/UC/blob/SFBA/TCP_STAR.csv)

2. To reproduce the results, run [main.ipynb](https://github.com/PawinData/UC/blob/SFBA/main.ipynb)

3. To check the implementation of TCP and STAR, go to [TCP.py](https://github.com/PawinData/UC/blob/SFBA/TCP.py) and [STAR.py](https://github.com/PawinData/UC/blob/SFBA/STAR.py). 

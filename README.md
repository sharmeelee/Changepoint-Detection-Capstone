# Detection of Changepoints during COVID
Authors: Priyanka Bijlani, Sharmeelee Bijlani, Lakshmi Venkatasubramanian, Dhruv Arora, Divya Pandey
## Introduction
Meta's Infrastructure Data Science team has released a time-series package called KATS to analyze time-series datasets. The KATS package implements multiple changepoint detection algorithms and tries to identify points in a time-series which show a sudden or abrupt change. A changepoint is defined as a ‘persistent change’ in the time series rather than an anomaly or an outlier in the time series data. The goal of this project is to conduct research on time series data and apply the KATS package to multiple datasets in various contexts to assess and evaluate the performance of the time-series algorithms, and to provide recommendations to improve the algorithms from the applied research conducted.

### Data
The data we will utilize for performance validation is datasets used in the Turing Change Point Dataset Benchmark Study (https://github.com/alan-turing-institute/TCPD) and the Google Mobility Dataset (https://www.google.com/covid19/mobility/) with true labels in the time-series as known by public knowledge. 

### Directory Structure
```bash
|   LICENSE
|   README.md
|
+---Artifacts
|       Flyer.pdf
|       Infographics_capstone.pdf
|       test
|
+---Datasets
|   |   katsExploration-MinimumTemp.ipynb
|   |   notes
|   |
|   \---DP_Datasets
|           Brent Spot Price.csv
|           Cali Emissions.csv
|           Coal Power.csv
|           HH Spot Price.csv
|           Imports Crude Oil.csv
|           NA Emissions.csv
|           Nuclear Capacity.csv
|           Ren Gen TX.csv
|           test.txt
|           Wind Gen.csv
|           WTI Price FOB.csv
|
+---EDA
|       katsExploration-Bayesian.ipynb
|       katsExploration-RobustStatDetector.ipynb
|
+---Final Drafts
|       Appendix.ipynb
|       CovidStory.ipynb
|       FinalDraft2.ipynb
|       Final_Notebook.ipynb
|       GoogleMobility.ipynb
|       test.md
|       Turing_BOCP.ipynb
|       Turing_Cusum.ipynb
|       Turing_RSD.ipynb
|
\---TCPD
        Centralia 3.ipynb
        GDP_Japan.ipynb
        Global_Monthly_CO2.ipynb
        Homeruns.ipynb
        Iteration_1.ipynb
        LGA_passengers.ipynb
        Nile 10.ipynb
        Nile.ipynb
        Ozone.ipynb
        Quality_control_1.ipynb
```


### Program Functionality
1. **Exploring changepoint detection algorithms using TCPD benchmark study**:

     In this section, we evaluate each changepoint detection algorithm from the KATS package using the datasets from the Turing study. The purpose of this exercise is to assess the advantages and shortcomings of each algorithm in the KATS package. We provide an analysis of each algorithm and its parameters optimized to find the changepoints closest to the true changepoints and with high confidence. These insights will be used to determine which algorithm is best suited for Google Mobility data for detecting changepoints during Covid.

   **Based on our finding from each algorithm run on datasets of varying domains, sizes, and number of changepoints, we recommend the selection criteria below:** 

        | Timeseries          | CUSUM | BOCP | RS |
        |---------------------|-------|------|----|
        | Outliers            | x     |      | x  |
        | Few Datapoints      | x     |      | x  |
        | Known CP Direction  | x     |      |    |
        | Multiple CPs        |       | x    | x  |
        | Seasonality         |       | x    |    |
        | No Domain Knowledge | x     | x    |    |

2. **Applying changepoint algorithms to the Google Mobility data**:

     In this section, we apply the KATS algorithms to the Google Mobility dataset which has multiple timeseries with over 20,000 rows each. The purpose of applying the KATS changepoint algorithms to the Google Mobility dataset is to explore how the algorithms behave in a real data scenario where catalyst dates are known, but the changepoints are unknown. The time when a change is announced may differ than the time when the change is observed in effect. We start by exploring the Global Mobility Report for the United States which can be downloaded from https://www.google.com/covid19/mobility/. 

We attempt to evaluate the different algorithms by choosing 3 specific use cases here:
  - Ability to detect multiple changepoints using Washington state transit data  
  
      The CUSUM detector only detects one changepoint in each direction and thus is not suitable for a large timeseries with both drastic and subtle changepoints unless the timeseries is segmented into interest windows where an expected changepoint is to occur. Without this prior knowledge, one would have to scan the entire timeseries with multiple window and plot all the discovered changepoints requiring extra coding effort. Both the BOCP and RS detectors are better choices for timeseries data with multiple expected changepoints.
        
  - Ability to detect seasonal changepoints using NewYork state parks data

      The BOCP Detector performs the best on a timeseries with seasonality. RS Detector finds a changepoint in each season in an observable pattern.  Even though CUSUM detects a changepoint based on the interest_window, it is very hard to know the right window range unless we know the change point upfront which is not the case usually.
        
  - Ability to resist outliers while detecting changepoints using Florida grocery and pharmacy data. 
        
      The BOCP detector fails the assessment of being outlier resilient since it detects several outliers as changepoints which are false positives. The CUSUM detector with and without an interest window does not mislabel outliers as changepoints. RS detector also does not detect outliers as changepoints. Both prove to be better algorithms for timeseries that have outliers.


3. **Telling the Covid-19 story through changepoints**

  - Training input: users, movies, ratings
  - User input: User, movie
  - Outputs: rating
  - ML algorithm: Collaborative filtering 


## Running the Program
### Installation Instructions
Run the following commands in a linux terminal. 
Note: Python 3.8 required
```
git clone https://github.com/sharmeelee/MovieRecommender.git
```
```
cd MovieRecommender
```
```
python3 setup.py install
```
### Running the Use Cases
To run the program, you need to navigate within the directory to the MovieRecommender sub-folder where the use_cases.py file lives.
```
cd MovieRecommender
```
#### Use Case #1: No inputs
Running the use_cases.py file without any arguments is an example usage of the full functionality of the program. It outputs movie rating for the default user (user 100) along with 20 similar movie titles to the default movie (Sliding Doors) and top 10 movie recommendations for the default user. 
```
python3 use_cases.py
```
Expected Output:

![alt text](images/use_cases1-1.png)
![alt text](images/use_cases1-2.png)
#### Use Case #2: Input Movie Name
Running the use_cases.py file with one argument of a movie name returns movie ratings for the default user, 20 similar titles to the given movie name, and top 10 movie recommendataions for the default user. 
```
python3 use_cases.py "Toy Story"
```
Expected Output: 

![alt text](images/use_cases2.png)
#### Use Case #3: Input Movie Name and Number of Similar Items
Running the use_cases.py file with two arguments outputs predicted movie ratings by the default user, a number (set by user input) of similar movie titles to the given movie name, and top 10 movie recommendations for the default user. 
```
python3 use_cases.py "Toy Story" 10
```
Expected Output:

![alt text](images/use_cases3.png)
#### Use Case #4: Input Movie Name, UserID, and Number of Similar Items
Running the use_cases.py file with all three arguments outputs predicted movie ratings for the given user, a number (set by user input) of similar movie titles to the given movie name, and top 10 movie recommendataion for the given user ID.
```
python3 use_cases.py "Toy Story" 500 10
```
Expected Output:

![alt text](images/use_case4-1.png)
![alt text](images/use_case4-2.png)

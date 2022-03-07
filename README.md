# Detection of Changepoints during COVID
Authors: Priyanka Bijlani, Sharmeelee Bijlani, Lakshmi Venkatasubramanian, Dhruv Arora, Divya Pandey
## Introduction
Meta's Infrastructure Data Science team has released a time-series package called KATS to analyze time-series datasets. The KATS package implements multiple changepoint detection algorithms and tries to identify points in a time-series which show a sudden or abrupt change. A changepoint is defined as a ‘persistent change’ in the time series rather than an anomaly or an outlier in the time series data. The goal of this project is to conduct research on time series data and apply the KATS package to multiple datasets in various contexts to assess and evaluate the performance of the time-series algorithms, and to provide recommendations to improve the algorithms from the applied research conducted.

### Data
The data we will utilize for performance validation is datasets used in the Turing Change Point Dataset Benchmark Study (https://github.com/alan-turing-institute/TCPD) and the Google Mobility Dataset (https://www.google.com/covid19/mobility/) with true labels in the time-series as known by public knowledge. 

### Directory Structure
```
Datasets
   |-- DP_Datasets
   |   |-- Brent Spot Price.csv
   |   |-- Cali Emissions.csv
   |   |-- Coal Power.csv
   |   |-- HH Spot Price.csv
   |   |-- Imports Crude Oil.csv
   |   |-- NA Emissions.csv
   |   |-- Nuclear Capacity.csv
   |   |-- Ren Gen TX.csv
   |   |-- WTI Price FOB.csv
   |   |-- Wind Gen.csv
   |   |-- test.txt
   |-- katsExploration-MinimumTemp.ipynb
   |-- notes
EDA
   |-- katsExploration-Bayesian.ipynb
   |-- katsExploration-RobustStatDetector.ipynb
Final Drafts
   |-- Final_Notebook.ipynb
   |-- Turing_Cusum.ipynb
   |-- test.md
LICENSE
README.md
TCPD
   |-- Centralia 3.ipynb
   |-- GDP_Japan.ipynb
   |-- Global_Monthly_CO2.ipynb
   |-- Homeruns.ipynb
   |-- Iteration_1.ipynb
   |-- LGA_passengers.ipynb
   |-- Nile 10.ipynb
   |-- Nile.ipynb
   |-- Ozone.ipynb
   |-- Quality_control_1.ipynb
```


### Program Functionality
1. User will get a movie recommendation from the system based on their movie watch and rating history.
  - Training input: users, movies, ratings
  - User input: user name/id
  - Outputs: movie(s)
  - ML algorithm: Collaborative filtering (analyzes historical data)

2. User will be able to provide a movie name and get similar movies.
  - Training input: users, movies, ratings
  - User input: movie
  - Outputs: movie(s)
  - ML algorithm: Collaborative filtering 

3. User will be able to predict the rating of a given movie based on their rating history.
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

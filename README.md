# Detection of Changepoints during COVID-19 Using KATS
Authors: Priyanka Bijlani, Sharmeelee Bijlani, Lakshmi Venkatasubramanian, Dhruv Arora, Divya Pandey
## Introduction
Meta's Infrastructure Data Science team has released a time-series package called KATS to analyze time-series datasets. The KATS package implements multiple changepoint detection algorithms and tries to identify points in a time-series which show a sudden or abrupt change. A changepoint is defined as a ‘persistent change’ in the time series rather than an anomaly or an outlier in the time series data. The goal of this project is to conduct research on time series data and apply the KATS package to multiple datasets in various contexts to assess and evaluate the performance of the time-series algorithms, and to provide recommendations to improve the algorithms from the applied research conducted.

### Important Links
- Kats: https://facebookresearch.github.io/Kats/
- Kats Python package: https://pypi.org/project/kats/0.1.0/
- Facebook Engineering Blog Post: https://engineering.fb.com/2021/06/21/open-source/kats/
- Notebooks: https://github.com/sharmeelee/Changepoint-Detection-Capstone/tree/main/Notebooks

### Data
The data we will utilize for performance validation are datasets used in the Turing Change Point Dataset Benchmark Study (https://github.com/alan-turing-institute/TCPD) and the Google Mobility Dataset (https://www.google.com/covid19/mobility/) with true labels in the time-series as known by public knowledge.

### Directory Structure
```bash
|   LICENSE
|   README.md
|   requirements.txt
|   setup.py
|
+---Artifacts
|       Flyer.pdf
|       Poster
|
\---Notebooks
        Appendix.ipynb
        Detecting Changepoints During COVID-19 Using KATS.ipynb

```


### Program Functionality
1. **Exploring changepoint detection algorithms using TCPD benchmark study**:

     In this section, we evaluate each changepoint detection algorithm from the KATS package using the datasets from the Turing study. The purpose of this exercise is to assess the advantages and shortcomings of each algorithm in the KATS package. We provide an analysis of each algorithm and its parameters optimized to find the changepoints closest to the true changepoints and with high confidence. These insights will be used to determine which algorithm is best suited for Google Mobility data for detecting changepoints during Covid. We have composed our analysis and findings in the notebooks **Appendix.ipynb**.
     
   **Based on our finding from each algorithm run on datasets of varying domains, sizes, and number of changepoints, we recommend the selection criteria below:** 

    ![image](https://user-images.githubusercontent.com/29467617/157568369-beb29f0f-8fc3-4744-9b0c-5d54798f52a9.png)

2. **Applying changepoint algorithms to the Google Mobility data**:

     In this section, we apply the KATS algorithms to the Google Mobility dataset which has multiple timeseries with over 20,000 rows each. The purpose of applying the KATS changepoint algorithms to the Google Mobility dataset is to explore how the algorithms behave in a real data scenario where catalyst dates are known, but the changepoints are unknown. The time when a change is announced may differ than the time when the change is observed in effect. We start by exploring the Global Mobility Report for the United States which can be downloaded from https://www.google.com/covid19/mobility/. 

     We attempt to evaluate the different algorithms by choosing 3 specific use cases here and all the analysis is composed in the notebook **Detecting Changepoints During COVID-19 Using KATS.ipynb**:
     
      - **Ability to detect multiple changepoints using Washington state transit data**  
  
          Based on our finding from each algorithm, the CUSUM detector only detects one changepoint in each direction and thus is not suitable for a large timeseries with both drastic and subtle changepoints unless the timeseries is segmented into interest windows where an expected changepoint is to occur. Without this prior knowledge, one would have to scan the entire timeseries with multiple window and plot all the discovered changepoints requiring extra coding effort. Both the BOCP and RS detectors are better choices for timeseries data with multiple expected changepoints.
        
      - **Ability to detect seasonal changepoints using NewYork state parks data**

          Based on our finding from each algorithm, the BOCP Detector performs the best on a timeseries with seasonality. RS Detector finds a changepoint in each season in an observable pattern.  Even though CUSUM detects a changepoint based on the interest_window, it is very hard to know the right window range unless we know the change point upfront which is not the case usually.
        
      - **Ability to resist outliers while detecting changepoints using Florida grocery and pharmacy data**
        
          Based on our finding from each algorithm, the BOCP detector fails the assessment of being outlier resilient since it detects several outliers as changepoints which are false positives. The CUSUM detector with and without an interest window does not mislabel outliers as changepoints. RS detector also does not detect outliers as changepoints. Both prove to be better algorithms for timeseries that have outliers.


3. **Telling the Covid-19 story through changepoints**
        
      Changepoint detection is a great way to tell a story about historical events. While true changepoints provide context on when an event occured, such as policy change, detected changepoints mark when the change actually takes effect on the ground. This makes changepoint detection an apt way to describe the events during the COVID-19 pandemic. The goal of this section is to portray how COVID-19 affected trends in mobility as seen through true changepoints and detected changepoints. We analyze the timing of preventative actions during the pandemic and their after-effects on mobility in various contexts across the United States.
      
      We use the learnings from part 1 and 2 above to influence the choice of algorithms as below:
      - The key changepoints in the COVID-19 story for the United States can be best detected using the Robust Stat detector because the data is highly aggregated. Therefore, it does not contain as drastic seasonality. However, there are a few outliers that oppose the regular trend which should not be mislabeled as changepoints. Since there are over 700 days worth of data, it can be expected that there will be multiple changepoints.

      - For individual states, algorithm selection must be based on some domain knowledge of the timeseries. For example, states with constant climate can use the Robust Stat detector, but others with changing seasons would need to opt for BOCP detector or CUSUM with multiple interest windows.

      - In the case that there is no domain knowledge of the state, BOCP detector in its current form is a strong choice because there would be no need for parameter selection to detect multiple changepoints.

      - To find how specific rules or regulations and their near-term impact, CUSUM detector would be an ideal choice because an interest window as well as the direction of the changepoint can be specified before application. County level data in shorter time frames can be analyzed using the CUSUM detector.

### COVID-19 in the United States <a name="part3a"></a>

When the pandemic was officially announced in March 2020, there were a series of events over the course of the next two years, that occured to control the spread the of the COVID-19 virus in the United States. These preventative measures included stay-at-home orders, mask mandates, and vaccines. The list of events that affected the mobility are given below. We denote these as true changepoints.

| Dates          | Events                                                                                                                                           |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|      **3/15/2020** | **CDC issued guidance recommending against any gathering of 50 or more people for an eight-week period.**                                        |
|      **3/16/2020** | **President Trump issued new guidelines urging people to avoid social gatherings of more than ten people and to restrict discretionary travel.** |
|   **4/3/2020** | **On April 3, 2020, the CDC issued guidance recommending that non-medical face coverings be worn in public**                                     |
| **12/31/2020** | **Delta Variant found in Florida**                                                                                                               ||
| **12/31/2020** | **Vaccines available**                                                                                                                           |
|   **2/1/2021** | **Distribution of vaccines**                                                                                                                     |
|  **12/1/2021** | **Omicron variant**                                                                                                                              |


![image](https://user-images.githubusercontent.com/29467617/157128096-e69b28f6-fb77-4978-b3a7-76f7d36d1d00.png)

![image](https://user-images.githubusercontent.com/29467617/157128579-fd4ade12-ad4e-4f47-9a7e-7c8ac2719e43.png)

### Installation Instructions
Kats is on PyPI, so you can use pip to install it. 
Note: Python 3.8 required
```
pip install --upgrade pip
pip install kats
```
If you need only a small subset of Kats, you can install a minimal version of Kats with
```
MINIMAL_KATS=1 pip install kats
```
which omits many dependencies (everything in ```test_requirements.txt```). However, this will disable many functionalities and cause import kats to log warnings. See ```setup.py``` for full details and options.

### License
This work is licensed under the MIT license.

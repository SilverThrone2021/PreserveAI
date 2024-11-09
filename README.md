# PreserveAI

Note to Shreyas Kaps
--------------------
Here is my approach.

- I initially tried to fit a multiple-linear-regression model to this data (flux_CO2_CH4_Barrow_2012_2013.csv, soil_moisture_Barrow_2012_2013.csv) but the correlation coefficient (R^2) was close to zero. 
- My second approach was to use gradient boosting/XGBoost which showed promising results. Though it is not optimal, it has an R^2 value of -0.58 (More details in Side2.py).
    -> PCA analysis revealed one variable accounted for 99% of the variation. 
- My suggestion for you is to tidy up the data and normalize/preprocess it and make it suitable for regression. 

The heatmap below shows the relationship between each variable.

![image](https://github.com/user-attachments/assets/49f7116f-d7a5-4198-90d1-97fcfd1584c7)

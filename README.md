# PreserveAI

Note to Shreyas Kaps
--------------------
Code is hosted here for ease of access
[https://colab.research.google.com/drive/1RihusDh3-yjqIl0O_NR0kDdLb1J91Wbe?usp=sharing](https://colab.research.google.com/drive/1RihusDh3-yjqIl0O_NR0kDdLb1J91Wbe?usp=sharing)

- Make sure to download the two .csv files locally and upload them to your google drive (detailed instructions are provided in the Colab Notebook).
- Read/Follow instructions outlined in the notebook.
- Let me know if you have any errors running anything.
    => My email is sachinmahesh@berkeley.edu, Phone: +1 (510)-890-1760    

------------------------------------------------------------
Here is my approach.

- I initially tried to fit a multiple-linear-regression model to this data (flux_CO2_CH4_Barrow_2012_2013.csv, soil_moisture_Barrow_2012_2013.csv) but the correlation coefficient (R^2) was close to zero. 
- My second approach was to use gradient boosting/XGBoost which showed promising results. Though it is not optimal, it has an R^2 value of -0.58 (More details in Side2.py).
    -> PCA analysis revealed one variable accounted for 99% of the variation. 
- My suggestion for you is to tidy up the data and normalize/preprocess it. We should then look into creating a custom Neural Network to reduce MSE and achieve a higher R^2 value (0.9+).

- If this data cannot be utilized as intended, have a look at the following resources to estimate CH4 emissions based on Soil Volumetric Water Content:
    - https://www.researchgate.net/figure/The-dependence-of-methane-flux-on-soil-moisture-a-and-temperature-b_fig4_337245230
    - https://www.researchgate.net/figure/a-Relationship-between-methane-fluxes-and-soil-volumetric-water-content-indicating-that_fig3_338445145
    - https://search.dataone.org/view/doi%3A10.5440%2F1227684
    - https://portal.edirepository.org/
    - https://enveurope.springeropen.com/articles/10.1186/s12302-024-00943-4
    - https://bg.copernicus.org/articles/15/3143/2018/
    - https://www.sciencedirect.com/science/article/pii/S0167880923005376
    - https://www.nature.com/articles/s41558-023-01785-3
    - https://www.nature.com/articles/s41598-024-65300-0

------------------------------------------------------------

The heatmap below shows the relationship between each variable.

![image](https://github.com/user-attachments/assets/49f7116f-d7a5-4198-90d1-97fcfd1584c7)

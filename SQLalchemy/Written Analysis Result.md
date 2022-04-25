SQLAlchemy Homework - Surfs Up!
Precipitation Analysis
1.	Design a query to retrieve the last 12 months of precipitation data.
    The query results the last date in the dataset is 2017-08-23, twelve months from there is 2016-08-23

2.	Load the query results into a Pandas DataFrame and set the index to the date column.
    The DataFrame shows 2,230 rows and 1 column as the first column was set as index, thus it does count as a data column.

3.	Sort the DataFrame values by date.
    Sorted DataFrame shows in ascending order with date 2016-08-23 as the first row and 2017-08-23 as the last row

4.	Plot the results using the DataFrame plot method.
    Please see image in result_images folder, file name precipitation.png
 

Station Analysis
1.	Design a query to calculate the total number of stations.
    The query calculated 9 stations in the dataset.

2.	Design a query to find the most active stations.
o	List the stations and observation counts in descending order.
    [('USC00519281', 'WAIHEE 837.5, HI US', 2772),
    ('USC00519397', 'WAIKIKI 717.2, HI US', 2724),
    ('USC00513117', 'KANEOHE 838.1, HI US', 2709),
    ('USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 2669),
    ('USC00516128', 'MANOA LYON ARBO 785.2, HI US', 2612),
    ('USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 2202),
    ('USC00511918', 'HONOLULU OBSERVATORY 702.2, HI US', 1979),
    ('USC00517948', 'PEARL CITY, HI US', 1372),
    ('USC00518838', 'UPPER WAHIAWA 874.3, HI US', 511)]

o	Which station has the highest number of observations?
    The highest number of temperature observations (most active) station is: WAIHEE 837.5, HI US, station ID: USC00519281. Recorded 2,772 records

3.  Design a query to retrieve the last 12 months of temperature observation data (TOBS).
o	Filter by the station with the highest number of observations.
    Query results WAIHEE 837.5, HI US Station ID: USC00519281 is the station with the highest number of observations, recorded 2,772 records

o	Plot the results as a histogram with bins=12.
    Please see image in result_images folder, file name station-histogram.png


Temperature Analysis I
1.  Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December? 

2.  Identify the average temperature in June at all stations across all available years in the dataset. Do the same for     December temperature.
    Average temperature in June across all years from the dataset is: 74.94F.
    Average temperature in June across all years from the dataset is: 71.04F.
3. Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?
    P value is 4.19, no significant difference exists.
    Unpaired ttest was used because the June and December are distinct samples.


Temperature Analysis II
1.  The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


2.  Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").


3.  Plot the min, avg, and max temperature from your previous query as a bar chart.
o   Use the average temperature as the bar height.
o   Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
    Please see image in result_images folder, file name temperature.png


Daily Rainfall Average
1.  Calculate the rainfall per weather station using the previous year's matching dates.
    Please see image in result_images folder, file name daily-rainfall-df-df.png

2.  Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
    Please see image in result_images folder, file name daily-normals-df.png

3.  You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.


4.  Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
    [array([60.  , 71.75, 79.  ]),
    array([63.        , 71.44680851, 77.        ]),
    array([62.        , 71.91666667, 79.        ]),
    array([62.        , 70.52083333, 77.        ]),
    array([57.        , 70.29166667, 78.        ]),
    array([63.        , 69.86363636, 76.        ]),
    array([56.        , 68.27906977, 77.        ]),
    array([62.        , 69.15384615, 77.        ]),
    array([60.        , 69.39622642, 77.        ]),
    array([62.        , 68.90909091, 77.        ])]


5.  Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
    Please see image in result_images folder, file name daily-normals-df.png

6.  Use Pandas to plot an area plot (stacked=False) for the daily normals.
    Please see image in result_images folder, file name daily-normals.png
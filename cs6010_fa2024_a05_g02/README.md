# Assignment #05: Visualization with Matplotlib and Seaborn 

## Data Explore:
    1.  X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
    2. Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
    3. month - month of the year: "jan" to "dec" 
    4. day - day of the week: "mon" to "sun"
    5. FFMC - Fine Fuel Moisture Code (measure of how dry fine surface materials) index from the FWI system: 18.7 to 96.20
    6. DMC - Duff Moisture Code (measures the moisture content in the intermediate layers of forest floor organic matter) index from the FWI system: 1.1 to 291.3 
    7. DC - Drought Code (a weather index measuring long-term drying conditions) index from the FWI system: 7.9 to 860.6 
    8. ISI - Initial Spread Index index from the FWI system: 0.0 to 56.10
    9. temp - temperature in Celsius degrees: 2.2 to 33.30
    10. RH - relative humidity in %: 15.0 to 100
    11. wind - wind speed in km/h: 0.40 to 9.40 
    12. rain - outside rain in mm/m2 : 0.0 to 6.4 
    13. area - the burned area of the forest (in ha): 0.00 to 1090.84 
    (this output variable is very skewed towards 0.0, thus it may make
    sense to model with the logarithm transform). 

## Reflection
- We generated the heatmap 1 using `Seaborn`'s `heatmap` function, which allows us to visualize the correlation matrix of the dataset. The correlation matrix provides insights into the relationships between different variables.

- We tried to formed hypothesises about the data and try to prove them with figures, for intance:
 - Is there a correlation between temperature and the burned area of the forest.
 - Is there a correlation between relative humidity and the burned area of the forest.
 - Is there a correlation between wind speed and the burned area of the forest.
 - Is there a correlation between rainfall and the burned area of the forest.
 - Is there a correlation between the Fine Fuel Moisture Code (FFMC) and the burned area of the forest.
 - Is there a correlation between the Duff Moisture Code (DMC) and the burned area of the forest.
 - Is there a correlation between the Drought Code (DC) and the burned area of the forest.

- We tried to cut continuous numeric data into bins.
 
- In this assignment, we created figures using `MathPlotLib`, `Seaborn` and `Bokeh` library to visualize the data and answer our hypothesises. Figures generated using `Bokeh` are saved as `.html` files in the `data/processed` folder.

- Throughout this journey, I have learned how to ask insightful questions and use visualizations to explore the forest fires dataset, gaining a deeper understanding of the data. I became more familiar with using functions from `Seaborn` and `MathPlotLib` to create various plots, such as scatter plots, box plots, and heatmaps, which helped me answer questions about correlations, seasonal trends, and fire size distribution. Each visualization allowed me to uncover patterns in the data, such as the relationship between weather conditions and the extent of forest fires. I learned how to effectively transform and manipulate data for better visual representation, such as using logarithmic scales for better clarity. This experience has significantly improved my ability to use data visualization as a tool for data-driven storytelling and decision-making.

-  I found that `Bokeh` provided a more interactive and dynamic visualization experience, allowing users to zoom in, pan, and hover over data points to view more information. However, I also noticed that `Bokeh` can be more complex to use than `MathPlotLib` and `Seaborn`, especially for simple visualizations. Overall, I believe that both `MathPlotLib` and `Seaborn` are excellent libraries for creating static visualizations, while `Bokeh` is a powerful tool for creating interactive and dynamic visualizations.

## Reflection Questions
1. What do I believe I did well on this assignment?
- I did well in identifying key questions about the dataset and using appropriate visualizations to answer them. By leveraging `Seaborn` and `MathPlotLib`, I was able to explore trends, correlations, and seasonal patterns effectively. My ability to create clear, informative plots helped uncover important insights from the data.

- To use heatmap for categorical data, we converted categorical data into numerical data using `map()` function. This allowed us to calculate the correlation matrix and visualize it using a heatmap.
 
- We used logarithmic scales to better represent the data and make patterns more visible.

- We used `Bokeh` to create interactive visualizations. This was particularly useful for exploring multi-variable relationships and understanding.

2. What was the most challenging part of this assignment?
- The most challenging part of this assignemnt is creating `Bokeh` figures as these figures required more steps as compared to `MathPlotLib` and `Seaborn` figures.

- Also other challenging part was handling highly skewed data, particularly visualizing burned area distributions effectively. In this part, we used logarithmic scales to better represent the data and make patterns more visible.

- We successfully create scatter figures with correlation lines using `MathPlotLib`. Howerver, we were not able to do so when we tried to draw correlation lines along with scatter figures in figures `2. Impact of Temperature on Burned Area` and `6. Relative Humidity vs Burned Area` using `Bokeh` .

3. What would have made this assignment a better experience?
- More guidelines and code examples on how to use `Bokeh` library would make this assignment a bit easier and a better experience.

4. What do I need help with?
- I need help with mastering more advanced techniques in data visualization, especially for multi-variable relationships.

- Furthermore, I faced problems when trying to draw correlation lines in figures `2. Impact of Temperature on Burned Area` and `6. Relative Humidity vs Burned Area` 
## Reflection

In this assignment, we created a dataset using the `Faker` library in `python`. The dataset includes missing values (represented by None) and bad data (represented by strings) for various columns. The `missing values` and `bad data` are introduced randomly with a probability of `10%` and `5%`, respectively. Before doing the assignment, we would need to clean up the data (e.g: drop duplicates, sort the dataframe, etc) so that we have a cleaner view in the pivot table. Also handle any non-numeric and invalid values (e.g: negative values in the `Humidity (%)` column)

After the data being cleansed, we start to `pivot` the dataframe to get a summary of the `Humidity (%)` data. We also `melt` the pivot table to get a long format dataframe for the ease of model training. We convert categorical `Moon Phase` values to numerical encoding and convert `Temperature` Celcius to Fahrenheit using `apply()` and `map()` functions. We also create a multi-index dataframe with `City`, `Season` and `Date` as the indexes and `stack()` the dataframe to get a long format dataframe. Finally, we reshape the dataframe by unstacking the dataframe to a wide format.

For further information, we utilized several methods from the Faker library to generate attributes such as city names, seasons, dates, and a wide range of weather-related variables including temperature, humidity, wind speed, and barometric pressure. I customized the dataset by adding synthetic data points for each weather feature and introducing various levels of missing and incorrect values. For example, I generated realistic temperatures within a range of -20°C to 50°C, while also injecting erroneous values such as strings or out-of-bound numbers to simulate bad data conditions. This approach allowed for a more comprehensive and realistic dataset, suitable for practicing data cleaning and transformation techniques commonly used in Tidy Data workflows. The process involved writing Python scripts, running them in the Jupyter Notebook, and validating the generated data for consistency and realism. Through this process, I gained a deeper understanding of data generation methods and how they can be applied to software testing and data analysis workflows. This experience also enhanced my familiarity with key data manipulation functions, such as .melt(), .pivot(), and .apply(), preparing me for future projects involving complex datasets.

## Reflection Questions

### What do we believe we did well on this assignment?

We generated a dataset that includes missing values (represented by None) and bad data (represented by strings or negative values in columns that should only contain values greater than or equal to zero) for various columns and handle these missing/invalid values before tidy the data.

We used all functions in this assignment (`pivot()`, `melt()`, `apply()`, `map()`, `stack()`, `unstack()`) to tidy the data and get a summary of the data. We also use `agg()` functions to get a summary of the data.

### What was the most challenging part of this assignment?

The most challenging part was detecting/handling missing/invalid values in the dataset and check the uniqness of the data before pivoting and unstacking.

Also the other challenging part was ensuring the generated data was not only realistic but also consistent and useful for the intended testing purposes. Fine-tuning the Faker methods to consistently produce relevant data without introducing too much unpredictability required significant iteration and careful planning. Ensuring the dataset was both varied and meaningful for subsequent data manipulation was a delicate challenge.

### What would have made this assignment a better experience?

We might need more time to understand the concept of tidy data and play around with the functions (`pivot()`, `melt()`, `apply()`, `map()`, `stack()`, `unstack()`) to to get faniliar with them.

### What do we need help with?

We might need help in finding a good dataset to start with or how to generate a good dataset.

### What did we actually learn by doing this assignment? Why does it matter?

We learned that it's important to clean up the data (handle missing/invalid values) before doing any analysis. Sorting the dataframe also helps to make the pivot table looks clearer. Tidying/reshaping the dataframe also helps us to get a summary of the data and understand the data better.

We learned how to effectively use the Faker library to generate synthetic datasets for testing purposes. This skill is crucial for creating realistic test scenarios without compromising real user data. It enhances our ability to test software applications under various conditions, ensuring better reliability and performance in real-world usage.

## Weather Dataset

This dataset contains simulated weather data for various cities across the United States. The data is generated using the Faker library in Python and includes a range of weather-related features such as temperature, humidity, wind speed, barometric pressure, precipitation, cloud cover, visibility, dew point, heat index, wind chill, UV index, sunrise and sunset times, moonrise and moonset times, moon phase, and a brief weather description.

### Dataset Description

The dataset is stored as a list of lists, where each inner list represents a single weather observation. The columns of the dataset are as follows:

1. City: The name of the city for which the weather data is recorded.
2. Date: The date of the weather observation in the format `YYYY-MM-DD`.
3. Temperature (°C): The temperature in degrees Celsius.
4. Humidity (%): The relative humidity as a percentage.
5. Wind Speed (km/h): The wind speed in kilometers per hour.
6. Wind Direction: The direction of the wind (e.g., N, NE, E, SE, S, SW, W, NW).
7. Barometric Pressure (hPa): The barometric pressure in hectopascals.
8. Precipitation (mm): The amount of precipitation in millimeters.
9. Cloud Cover (%): The percentage of cloud cover.
10. Visibility (km): The visibility in kilometers.
11. Dew Point (°C): The dew point temperature in degrees Celsius.
12. Heat Index (°C): The heat index temperature in degrees Celsius.
13. Wind Chill (°C): The wind chill temperature in degrees Celsius.
14. UV Index: The UV index, ranging from 0 to 11.
15. Sunrise Time: The time of sunrise in the format `HH:MM:SS`.
16. Sunset Time: The time of sunset in the format `HH:MM:SS`.
17. Moonrise Time: The time of moonrise in the format `HH:MM:SS`.
18. Moonset Time: The time of moonset in the format `HH:MM:SS`.
19. Moon Phase: The current phase of the moon (e.g., New Moon, Waxing Crescent, First Quarter, Waxing Gibbous, Full Moon, Waning Gibbous, Last Quarter, Waning Crescent).
20. Weather Description: A brief description of the weather conditions.

The dataset includes missing values (represented by None) and bad data (represented by strings) for various columns. The missing values and bad data are introduced randomly with a probability of 10% and 5%, respectively.

### Data Generation

The dataset is generated using the Faker library in Python, which provides a wide range of utilities for generating fake data. The generation process includes the following steps:

1. Define a list of city names.
2. Define the column names for the dataset.
3. Generate 100 weather observations by randomly selecting values for each feature based on predefined ranges and distributions.
4. Introduce missing values and bad data (e.g., strings instead of numbers, values outside the expected range) for a subset of the observations to simulate real-world data quality issues.

### Usage

This dataset can be used for various purposes, such as data cleaning, exploratory data analysis, feature engineering, and machine learning model training and evaluation. It provides a realistic scenario where data quality issues need to be addressed, and appropriate preprocessing techniques need to be applied before further analysis or modeling.

Note: Since the data is randomly generated, the specific values and distributions may vary across different runs of the code.

Here's an example assignment that can be used to teach, evaluate, and practice the principles of Tidy Data in CS 6010, focusing on the concepts and techniques related to `.melt()`, `.pivot()`, `.pivot_table()`, `.apply()`, `.map()`, `.stack()`, and `.unstack()`:

1. **Data Exploration**: Load the 'weather_data.csv' file into a pandas DataFrame and explore the data using various techniques such as `head()`, `tail()`, `info()`, `describe()`, and `isnull().sum()`. Identify any missing values or invalid data in the dataset.

2. **Reshaping with .melt()**: Use the `.melt()` function to reshape the dataset from a wide format to a long format. Specify the 'Date' and 'level_0' (city) columns as the identifier variables, and all other columns as value variables.

3. **Handling Missing Values**: Identify the columns with missing values and decide on an appropriate strategy for handling them (e.g., dropping rows, filling with a specific value, or interpolating). Implement your chosen strategy using pandas functions like `dropna()`, `fillna()`, or `interpolate()`.

4. **Data Cleaning**: Identify any invalid or inconsistent data in the dataset (e.g., negative wind speeds, cloud cover values greater than 100). Use pandas functions like `.apply()` or `.map()` to clean and transform the data as needed.

5. **Pivoting with .pivot() and .pivot_table()**: Use the `.pivot()` function to reshape the long-format data back to a wide format, with 'Date' as the index and 'level_0' (city) as the columns. Alternatively, use the `.pivot_table()` function to create a summary table of the weather data, aggregating values by city and date.

6. **Grouping and Aggregation**: Use pandas grouping and aggregation functions like `groupby()` and `agg()` to calculate summary statistics (e.g., mean, median, max, min) for different weather variables, grouped by city or date.

7. **Stacking and Unstacking**: Use the `.stack()` and `.unstack()` functions to reshape the data in different ways, depending on your analysis needs. For example, you can stack the city columns to create a multi-index DataFrame, or unstack a specific column to create a pivot-like structure.

8. **Visualization**: Create visualizations (e.g., line plots, scatter plots, bar charts) to explore the relationships between different weather variables, or to compare weather patterns across cities or time periods.

9. **Advanced Techniques**: Explore more advanced techniques like `.apply()` with custom functions, `.map()` with lambda functions, or `.transform()` to perform complex data transformations or calculations.

10. **Tidy Data Principles**: Throughout the assignment, emphasize the principles of Tidy Data, such as having each variable in a column, each observation in a row, and each value in a cell. Discuss how the various reshaping and transformation techniques help achieve or maintain a tidy data structure.

This assignment covers a wide range of concepts and techniques related to Tidy Data, data reshaping, data cleaning, and data analysis using pandas. Students will gain hands-on experience working with a real-world weather dataset, addressing common challenges like missing values, invalid data, and data transformation.

This assignment covers the following concepts and techniques related to Tidy Data:

Understanding the principles of Tidy Data
Reshaping data from wide to long format using .melt()
Reshaping data from long to wide format using .pivot() and .pivot_table()
Applying functions along rows or columns using .apply() and .map()
Reshaping data by pivoting rows to columns or columns to rows using .stack() and .unstack()
Handling missing values and bad data using .isna(), .notna(), and .str.contains()
Each question provides a brief explanation of the concept or technique, followed by a coding exercise where students need to write Python code using the provided functions. The assignment also includes sample solutions for each question.

By completing this assignment, students will gain hands-on experience in reshaping and cleaning data using various pandas functions, which is essential for working with Tidy Data and preparing datasets for further analysis.

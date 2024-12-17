# Quote Scraper Script

## Summary

This Python script scrapes quotes and their corresponding author information from the website [Quotes to Scrape](http://quotes.toscrape.com). It collects:
- The quote text
- The author's name
- The author's date of birth
- The author's location of birth

The collected data is then saved in both CSV and Excel file formats for further use.

To do this, I performed those tasks:

- Scrapes quotes along with author details across multiple pages.
- Visits individual author pages to retrieve additional information (date of birth and place of birth).
- Saves the scraped data into structured formats: CSV and Excel files.

## Reflection Questions
1. The best part I have done in this assignment is scrapping with pagination and implement exceptions handling.
2. The most challenging part of this assignment is scrapping with pagination and exceptions handling.
3. So far scrapping the website is fun and educational.
4. I might need some help in developing exceptions handling (try - except) in python.
5. I learnt about request and beautifulsoup lib which provide me basic skills in data scrapping.

## Requirements

Before running the script, you need to install the following Python libraries:

- `pandas`: For creating and managing DataFrames and saving data into CSV and Excel.
- `requests`: For making HTTP requests to the website.
- `BeautifulSoup` (from `bs4`): For parsing the HTML content.
- `openpyxl`: For writing data into Excel files.

To install these libraries, run:

```bash
pip install pandas requests beautifulsoup4 openpyxl
```

## Output

* CSV File: The script saves the scraped data as `data.csv` in the `../data/processed/` directory.
* Excel File: The same data is saved as `data.xlsx` in the same directory.

## Data Columns:

* `author`: The name of the author.
* `qoute`: The quote text.
* `date_of_birth`: The author's date of birth.
* `place_of_birth`: The author's location of birth.
* `url`: The URL to the author's details page.

## How to Run

1. Install the required libraries.
2. Run the script in your Python environment.
3. After the script completes execution, you can find the saved data files (`data.csv` and `data.xlsx`) in the `../data/processed/` directory.

## Ensure the following:

* The `../data/processed/` directory exists before running the script. If it doesn't exist, either create it or modify the file paths in the script to suit your directory structure.

## License
This project is licensed under the MIT License.
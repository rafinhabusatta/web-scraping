# Web Scraping Project: Movie Titles from IMDb

This project performs web scraping of movie titles from IMDb based on a list of movie titles contained in an Excel spreadsheet. The goal is to extract relevant movie information directly from the IMDb website for educational and learning purposes.

## How to Use

1. **Available Files**:
   - The application includes an executable `.exe` file located in the `executables` folder. This file is the ready-to-use version of the application.
   - There is also an Excel spreadsheet containing movie titles in the **first column**. You can use any spreadsheet that has a list of movie titles in the first column.

2. **Steps to Run**:
   - Put the Excel spreadsheet containing the movie titles on the same folder of the `.exe`.
   - Run the `.exe` file found in the `executables` folder. The application will read the movie titles from the spreadsheet.
   - The scraper will search for information about each title on IMDb and return data such as:
     - Full title
     - Release year
     - Link to IMDB's movie page

3. **Customization**:
   - If you want to use a different spreadsheet, simply ensure that the movie titles are in the **first column** of the spreadsheet. The application will automatically read data from the first column.

4. **Dependencies**:
   - The project was developed using Python and the following libraries:
     - `requests`
     - `beautifulsoup4`
     - `pandas`
     - `openpyxl`

5. **Disclaimer**:
   - **Educational Use**: This project was created exclusively for educational and learning purposes. It is not intended for commercial use.
   - **Limitations**: The project relies on IMDb not blocking or altering its pages. In case of layout changes or policy updates on the website, the scraper may need adjustments.

6. **Results**:
   - The scraper will generate a new spreadsheet with the collected information, where each row will contain data about the movie corresponding to the title in the original spreadsheet.
   - If a title is not found on IMDb, the scraper will mark it as "not found" in the respective cell.

## Sample Output

| **Movie Title** | **Year** | **Link** |
|-----------------|----------|----------|
| Inception       | 2010     | https://www.imdb.com/pt/title/tt1375666/?ref_=fn_all_ttl_1
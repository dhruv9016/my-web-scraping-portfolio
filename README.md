# 📘 Book Scraper Project

This project scrapes book information such as *title, **price, and **rating* from the [Books to Scrape](https://books.toscrape.com/) website using Python.

## 🧠 Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas (for saving data to CSV)

## ⚙️ How It Works
1. The script sends a request to the website.
2. BeautifulSoup parses the HTML and extracts book titles, prices, and ratings.
3. The data is saved to a file named *books.csv* for easy viewing in Excel.

## 📂 Files in this Project
- book_scraper.py — The Python script that performs the scraping.
- books.csv — The output file containing the scraped data.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas

2. run the script:

  python book_scraper.py

3. After running, a file named books.csv will be created in your folder.


📂 Files in this Project

book_scraper.py — The Python script that performs the scraping.

books.csv — The output file containing the scraped data.



---

## 📊 Example Output (books.csv)

| Title               | Price   | Rating |
|----------------------|---------|--------|
| A Light in the Attic | £51.77  | Three  |
| Tipping the Velvet   | £53.74  | One    |
| Sharp Objects        | £47.82  | Four  



---

📖 About This Project

This mini-project is part of my journey to learn web scraping and data automation using Python.
It demonstrates how to extract data from websites, clean it, and export it to a CSV file for analysis.

The same concept can be used for:

Price monitoring

Product data collection

Market analysis

Automation scripts



---

✨ Author

Dhruv Vankar,
📧 harshdhruv2022@gmail.com
🌐 https://github.com/dhruv9016

# TikTok Scraper

A web scraper that extracts video data from TikTok using Playwright and BeautifulSoup, saving results in a CSV file for easy analysis.

## Features

- **Asynchronous Data Fetching**: Efficiently handles multiple requests to load and parse TikTok pages.
- **Cookie Management**: Automatically loads and saves cookies to maintain session state.
- **HTML Parsing**: Extracts structured data using BeautifulSoup.
- **CSV Output**: Compiles extracted data into a CSV file.
- **Folder Processing**: Parses multiple HTML files from a specified folder.

## Getting Started

### Prerequisites

- Python 3.x
- Required packages can be installed via pip:

```bash
pip install -r requirements.txt
```

### Usage
- Set up your proxy if necessary.
- Run the main.py and select the desired option to fetch and save data from TikTok
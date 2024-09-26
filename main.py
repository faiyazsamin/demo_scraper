import logging
from scraper.scraper import Scraper  # Importing the Scraper class
from scraper.parser import Parser  # Importing the Scraper class
from scraper.config import Config  # Importing configuration settings


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        filename='logs/scraper.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging is set up.")


def scrape(page_count):
    config = Config()
    for x in range(1, int(page_count)+1, 1):
        fetcher = Scraper(config)
        html_content = fetcher.fetch_page()
        with open(f"data/raw/tiktok_{x}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
    logging.info("Scraping completed successfully.")

def parse():
    # Load configuration
    config = Config()
    # Initialize the scraper
    parse_page = Parser(config)
    parse_page.parse(config.RAW_DATA_DIR)
def main():
    setup_logging()
    menu = input("Enter 1 to scrape, 2 to parse: ")
    if menu == "1":
        page_count = input("Enter the number of pages to scrape: ")
        scrape(page_count)
    elif menu == "2":
        parse()
    else:
        print("Invalid option. Please try again.")
        main()


if __name__ == '__main__':
    main()

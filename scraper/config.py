# scraper/config.py

class Config:
    BASE_URL = 'https://www.tiktok.com'
    COOKIES_FILE = 'data/cookies.json'
    RAW_DATA_DIR = 'data/raw'
    PROXY = None  # 127.0.0.1:8080
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }

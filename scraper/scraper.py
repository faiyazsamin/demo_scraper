import json
from playwright.sync_api import sync_playwright


class Scraper:
    def __init__(self, config=None):
        self.proxy = config.PROXY
        self.cookies_file = config.COOKIES_FILE
        self.base_url = config.BASE_URL
        self.browser = None
        self.context = None
        self.page = None

    def fetch_page(self):
        """Launch the browser and set up the context."""
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=False)
            self.context = self.browser.new_context(
                proxy={"server": self.proxy} if self.proxy else None,
                ignore_https_errors=True  # Ignore SSL errors
            )

            # Load cookies if they exist
            self.load_cookies()

            # Open a new page
            self.page = self.context.new_page()
            self.page.goto(self.base_url)
            self.page.wait_for_timeout(10000)  # Adjust time as needed
            self.save_cookies()
            html_content = self.page.content()
            return html_content

    def load_cookies(self):
        """Load cookies from a file."""
        try:
            with open(self.cookies_file, 'r') as file:
                cookies = json.load(file)
                self.context.add_cookies(cookies)
        except FileNotFoundError:
            pass  # Ignore if the cookies file does not exist

    def save_cookies(self):
        """Save cookies to a file."""
        cookies = self.context.cookies()
        with open(self.cookies_file, 'w') as file:
            json.dump(cookies, file)
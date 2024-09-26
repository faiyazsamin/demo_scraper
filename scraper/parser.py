import os

from bs4 import BeautifulSoup
import pandas as pd
import logging


class Parser:
    def __init__(self, config):
        self.data = []


    def parse(self, folder_name):
        """Parse HTML files in a folder and extract data."""
        try:
            # Iterate through all files in the specified folder
            for file_name in os.listdir(folder_name):
                # Construct full file path
                file_path = f"{folder_name}/{file_name}"

                # Process only HTML files
                if file_name.endswith('.html'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        soup = BeautifulSoup(file, 'html.parser')

                    items = soup.find_all(attrs={'data-e2e': 'recommend-list-item-container'})

                    for item in items:
                        data_e2e_elements = item.find_all(attrs={"data-e2e": True})

                        data_e2e_dict = {}
                        for element in data_e2e_elements:
                            data_e2e_value = element['data-e2e']
                            inner_text = element.get_text(strip=True)
                            data_e2e_dict[data_e2e_value] = inner_text

                        # Extract values safely with .get() to avoid KeyErrors
                        video_name = data_e2e_dict.get('video-desc', '')
                        video_user = data_e2e_dict.get('video-author-uniqueid', '')
                        video_like_count = data_e2e_dict.get('like-count', 0)
                        video_comment_count = data_e2e_dict.get('comment-count', 0)
                        video_share_count = data_e2e_dict.get('share-count', 0)

                        # Append extracted data to the list
                        self.data.append({
                            'video_name': video_name,
                            'video_user': video_user,
                            'video_like_count': video_like_count,
                            'video_comment_count': video_comment_count,
                            'video_share_count': video_share_count
                        })

            # Save all collected data to a CSV file
            self.save_data()
        except Exception as e:
            logging.error(f"Failed to parse: {e}")

    def save_data(self):
        """Save the scraped data to a CSV file."""
        df = pd.DataFrame(self.data)
        df.to_csv('data/output.csv', index=False)
        logging.info("Data saved to output.csv")

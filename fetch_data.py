import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

HEADERS = {"Flic-Token": os.getenv("FLIC_TOKEN")}
def fetch_paginated_data(api_url):
    page = 1
    all_data = []
    while True:
        response = requests.get(f"{api_url}&page={page}&page_size=1000", headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if not data:  # No more data
                break
            all_data.extend(data)
            page += 1
            time.sleep(1)  # Avoid hitting API rate limits
        else:
            print(f"Failed to fetch data: {response.status_code}")
            break
    return all_data

# Example API call

if __name__ == "__main__":
    data = fetch_paginated_data("https://api.socialverseapp.com/posts/view")
    print(f"Fetched {len(data)} records")

import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/blogs/what-is-web-scraping-and-how-to-use-it/"

def get_h2_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_headers = [header.get_text() for header in soup.find_all('h2')]
    return h2_headers

print(get_h2_headers(URL))
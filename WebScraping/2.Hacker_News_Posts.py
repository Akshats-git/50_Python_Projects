import csv
import requests
from bs4 import BeautifulSoup

URL="https://news.ycombinator.com/"

def fetch_top_post(URL):
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the top posts: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.select(".athing")
    top_posts = []

    for post in posts:
        title = post.select_one(".titleline a").text
        link = post.select_one(".titleline a")["href"]
        top_posts.append({"title": title, "link": link})

    return top_posts

def save_to_csv(posts, filename="top_posts.csv"):
    keys = posts[0].keys() if posts else ["title", "link"]
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(posts)

top_posts = fetch_top_post(URL)
save_to_csv(top_posts)
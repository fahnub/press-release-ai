import requests
from bs4 import BeautifulSoup
import json
import time


def fetch_title_and_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("div", class_="person-name mt0").get_text(strip=True)
        content_div = soup.find("div", class_="col s12 mt0")
        paragraphs = content_div.find_all("p")
        content = ""

        for paragraph in paragraphs:
            if not any(
                text in paragraph.get_text(strip=True)
                for text in ["Download press release", "Download Images", "Share:"]
            ):
                content += paragraph.get_text(strip=True) + "\n"

        print(f"Title: {title}\nContent: {content}")
        return {"title": title, "content": content}

    else:
        print(f"Failed to fetch {url}")
        return None


def fetch_data_from_links(file_path):
    data = []

    with open(file_path, "r") as file:
        links = file.read().splitlines()

        for link in links:
            article_data = fetch_title_and_content(link)

            if article_data:
                data.append(article_data)
            time.sleep(1)

    return data


file_path = "links.txt"
articles_data = fetch_data_from_links(file_path)

output_file = "articles.json"

with open(output_file, "w") as f:
    json.dump(articles_data, f, indent=4)

print("Data has been written to:", output_file)

import requests
from bs4 import BeautifulSoup

base_url = "https://azizidevelopments.com/en/news-pr?page="
keyword = "/en/news-pr/"
total_pages = 114


def fetch_specific_links_from_pages(base_url, keyword, total_pages):
    unique_links = set()

    with open("links.txt", "w") as file:
        for page in range(1, total_pages):
            url = f"{base_url}&page={page}"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.find_all("a", href=lambda href: href and keyword in href)

                for link in links:
                    href = link.get("href")

                    if href not in unique_links:
                        unique_links.add(href)
                        file.write(href + "\n")
                        print(href)

        else:
            print(f"Failed to retrieve page {page}.")


fetch_specific_links_from_pages(base_url, keyword, total_pages)

import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://quotes.toscrape.com"
current_url = "/page/1/"

all_quotes = []
page_number = 1

while current_url:
    full_url = base_url + current_url
    response = requests.get(full_url)

    print(f"Scraping page {page_number}: {full_url}")

    if response.status_code != 200:
        print("Failed to fetch page.")
        print("Status Code:", response.status_code)
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    for quote in quote_blocks:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        tag_elements = quote.find_all("a", class_="tag")
        tags = [tag.text for tag in tag_elements]

        all_quotes.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags),
            "Page": page_number,
        })

    next_button = soup.find("li", class_="next")

    if next_button:
        current_url = next_button.find("a")["href"]
        page_number += 1
    else:
        current_url = None

df = pd.DataFrame(all_quotes)

output_file = "data/all_quotes.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("\nPagination scraping completed successfully.")
print("Total quotes scraped:", len(all_quotes))
print("Total pages scraped:", page_number)
print("CSV file saved at:", output_file)
print("\nPreview:")
print(df.head())

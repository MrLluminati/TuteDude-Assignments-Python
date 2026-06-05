import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://quotes.toscrape.com/"

response = requests.get(url)

quotes_data = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    for quote in quote_blocks:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        tag_elements = quote.find_all("a", class_="tag")
        tags = [tag.text for tag in tag_elements]

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags),
        })

    df = pd.DataFrame(quotes_data)

    output_file = "data/quotes_page_1.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print("Scraping completed successfully.")
    print("Total quotes scraped:", len(quotes_data))
    print("CSV file saved at:", output_file)
    print("\nPreview:")
    print(df.head())
else:
    print("Failed to fetch webpage.")
    print("Status Code:", response.status_code)
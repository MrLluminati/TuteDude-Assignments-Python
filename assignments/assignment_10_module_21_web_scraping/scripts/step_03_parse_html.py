import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    page_title = soup.title.text
    first_heading = soup.find("h1").text.strip()
    quote_blocks = soup.find_all("div", class_="quote")

    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Page Title:", page_title)
    print("First Heading:", first_heading)
    print("Number of Quote Blocks Found:", len(quote_blocks))

    if quote_blocks:
        first_quote = quote_blocks[0]
        quote_text = first_quote.find("span", class_="text").text
        quote_author = first_quote.find("small", class_="author").text

        print("\nFirst Quote:")
        print("Quote:", quote_text)
        print("Author:", quote_author)
else:
    print("Failed to fetch webpage.")
    print("Status Code:", response.status_code)
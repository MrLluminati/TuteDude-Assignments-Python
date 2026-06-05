import requests


url = "https://quotes.toscrape.com/"

response = requests.get(url)

print("URL:", url)
print("Status Code:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))
print("Page Length:", len(response.text))

if response.status_code == 200:
    print("Webpage fetched successfully.")
else:
    print("Failed to fetch webpage.")
import requests
from bs4 import BeautifulSoup


def clean_price(price_text):
    """
    Convert price text like '₹1,299' or '1,299' into a number like 1299.0.
    """
    cleaned_price = price_text.replace("₹", "")
    cleaned_price = cleaned_price.replace(",", "")
    cleaned_price = cleaned_price.strip()

    return float(cleaned_price)


def compare_price(product_title, price_text, target_price, source):
    """
    Convert scraped price text into a number and compare it with target price.
    """
    try:
        current_price = clean_price(price_text)
    except ValueError:
        print("Scraped Price Text:", price_text)
        print("Price text could not be converted into a number.")
        return

    print("\nProduct Title:", product_title)
    print("Price Source:", source)
    print("Scraped Price Text:", price_text)
    print("Converted Numeric Price:", current_price)
    print("Target Price:", target_price)

    if current_price <= target_price:
        print("Result: Buy now. The product price is at or below your target price.")
    else:
        print("Result: Wait. The product price is above your target price.")


def check_amazon_price(product_url, target_price):
    """
    Try to fetch Amazon product page, extract product title and price,
    convert the price into a number, and compare it with target price.
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-IN,en;q=0.9",
    }

    print("Fetching product page...")
    print("URL:", product_url)

    response = requests.get(product_url, headers=headers)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Unable to fetch the product page.")
        print("Amazon may have blocked the request or the URL may be invalid.")
        run_sample_price_demo(target_price)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title_element = soup.find(id="productTitle")

    if title_element:
        product_title = title_element.get_text().strip()
    else:
        product_title = "Product title not found"

    price_element = soup.find("span", class_="a-price-whole")

    if not price_element:
        price_element = soup.find("span", class_="a-offscreen")

    if price_element:
        price_text = price_element.get_text().strip()
        compare_price(product_title, price_text, target_price, "Live Amazon page")
    else:
        print("\nProduct Title:", product_title)
        print("Price could not be extracted from the live Amazon page.")
        print("Amazon may have changed the page structure or blocked the request.")
        run_sample_price_demo(target_price)


def run_sample_price_demo(target_price):
    """
    Fallback demonstration used when Amazon blocks live scraping.
    This keeps the assignment logic visible:
    price text -> numeric conversion -> target comparison.
    """
    print("\nRunning beginner-level fallback demonstration...")
    print("Reason: Live Amazon page did not expose title/price in normal HTML.")

    sample_product_title = "Sample Amazon Product"
    sample_price_text = "₹49,999"

    compare_price(
        sample_product_title,
        sample_price_text,
        target_price,
        "Fallback sample price text"
    )


print("Amazon Product Price Checker")
print("----------------------------")

amazon_url = input("Enter Amazon product URL: ")
target = float(input("Enter your target price: "))

check_amazon_price(amazon_url, target)

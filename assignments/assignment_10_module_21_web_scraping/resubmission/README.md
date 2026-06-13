# Assignment 10 Resubmission: Product Price Checker

## Project overview

This is the revised resubmission for Assignment 10: Web Scraping.

The project is intentionally kept beginner-friendly. It demonstrates how to use Python, `requests`, and `BeautifulSoup` to attempt product page scraping and then perform price comparison logic.

## Mentor feedback addressed

The resubmission directly addresses the feedback requirement to:

- use a product page URL;
- extract price data where available;
- convert the price text into a numeric value;
- compare the converted price with a target price;
- print a clear result message.

## Files included

```text
resubmission/
├── NOTE_TO_MENTOR.txt
├── README.md
├── requirements.txt
├── screenshot_proofs/
│   └── resubmission_step_01_amazon_price_checker/
└── scripts/
    └── amazon_price_checker.py
```

## Dependencies

```text
requests
beautifulsoup4
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Main script

```text
scripts/amazon_price_checker.py
```

The script contains the following beginner-level functions:

### `clean_price(price_text)`

Removes the currency symbol and comma separators from price text, then converts it into a floating-point number.

Example:

```text
49,999 -> 49999.0
```

### `compare_price(product_title, price_text, target_price, source)`

Converts the price text into a number and compares it with the target price entered by the user.

### `check_amazon_price(product_url, target_price)`

Fetches the product page using `requests`, parses the page using `BeautifulSoup`, and tries to extract the product title and price.

### `run_sample_price_demo(target_price)`

Runs a visible fallback demonstration if the live page does not expose title or price in normal HTML. This is included because some product websites may block automated requests or change their page structure.

## How to run

From the `resubmission` folder, run:

```powershell
python .\scripts\amazon_price_checker.py
```

Then enter:

```text
Product URL
Target price
```

## Test performed

A product URL was entered with a target price of `50000`.

The script successfully:

- accepted the product URL;
- accepted the target price;
- sent a request to the product page;
- received status code `200`;
- handled the case where the live title/price were not exposed;
- ran the visible fallback demonstration;
- converted `49,999` into `49999.0`;
- compared `49999.0` with `50000.0`;
- printed the final result message.

## Output demonstrated

```text
Scraped Price Text: 49,999
Converted Numeric Price: 49999.0
Target Price: 50000.0
Result: Buy now. The product price is at or below your target price.
```

## Important note

Some websites may block automated scraping or return modified HTML. The script therefore includes simple error handling and a clearly labelled fallback demonstration. The fallback is not hidden and is used only to keep the beginner-level assignment logic visible when the live page does not expose normal product price HTML.

## Screenshot proofs

Screenshot proofs are available at:

```text
screenshot_proofs/resubmission_step_01_amazon_price_checker/
```

They show:

- script code;
- live product page request attempt;
- fallback price conversion;
- target price comparison;
- final terminal output.

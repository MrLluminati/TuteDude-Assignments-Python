# Assignment 12 - Automation using Selenium

This assignment contains two beginner-level Selenium programs.

## Programs

### 1. Google Search Automation

The first program:

- opens Google in Chrome
- maximizes the browser window
- searches for Python Selenium tutorial
- prints the page title and URL
- refreshes the page
- closes the browser

### 2. Amazon Data Extraction

The second program:

- opens Amazon India
- searches for wireless mouse
- finds multiple product cards
- prints five product names and prices
- finds the Today's Deals link
- opens the Deals page
- closes the browser

## Selenium Locators Used

- By.NAME
- By.ID
- By.CLASS_NAME
- By.LINK_TEXT
- By.XPATH

## Installation

Run:

python -m pip install -r requirements.txt

## Running the Programs

Run:

python scripts/01_google_search.py

python scripts/02_amazon_data.py

Note: Google may sometimes show an automated traffic page when Selenium performs a search. The browser automation and search steps still execute.

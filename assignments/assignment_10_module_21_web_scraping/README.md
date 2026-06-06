# Assignment 10: Module 21 - Web Scraping Module Implementation

This folder now contains both the original submitted version and the revised resubmission version of Assignment 10.

## Source PDF

```text
../../resources/source_pdfs/ASSIGNMENT 13.docx.pdf
```

## Assignment document note

The assignment document available to the learner broadly mentioned Web Scraping module implementation and submission of working project files. It did not expressly mention that the implementation must specifically scrape an Amazon product page, extract product price, convert the price into a numeric value, compare it with a target price, and print a comparison result.

After mentor feedback, the project is being revised to directly address the expected Amazon product price comparison requirement.

## Current folder structure

```text
assignment_10_module_21_web_scraping/
├── README.md
├── original_submission/
│   ├── data/
│   ├── requirements.txt
│   ├── screenshot_proofs/
│   └── scripts/
└── resubmission/
    ├── data/
    ├── NOTE_TO_MENTOR.txt
    ├── requirements.txt
    ├── screenshot_proofs/
    └── scripts/
```

## Folder purpose

### `original_submission/`

This folder preserves the first submitted version of Assignment 10.

The original submission included a complete beginner-friendly general web scraping project using:

- `requests`
- `BeautifulSoup`
- `pandas`
- webpage fetching
- HTML parsing
- quote scraping
- CSV export
- pagination scraping
- final testing screenshots

The original project scraped data from:

```text
https://quotes.toscrape.com/
```

It produced:

```text
original_submission/data/quotes_page_1.csv
original_submission/data/all_quotes.csv
```

### `resubmission/`

This folder contains the revised project prepared after mentor feedback.

The resubmission is being built as a beginner-level Amazon product price checker. It is intended to implement the specific feedback requirement:

- accept an Amazon product URL;
- accept a target price;
- fetch the Amazon product page using `requests`;
- parse HTML using `BeautifulSoup`;
- extract the product title and price where available;
- clean the price text;
- convert the price into a numeric value;
- compare the scraped price with the target price;
- print a clear result message.

## Important technical note

Amazon may sometimes block automated requests or change its HTML page structure. Therefore, the resubmission script will be kept beginner-friendly and will include basic error handling so that it prints a clear message if the product title or price cannot be extracted.

## Resubmission note

A formal note for the mentor has been added at:

```text
resubmission/NOTE_TO_MENTOR.txt
```

This note explains that the first submission was based on the broad assignment document, while the resubmission is being prepared according to the mentor's specific feedback.

## Resubmission progress checklist

- [x] Step R0: Preserve original submission and create resubmission folder
- [x] Step R0: Add formal note for mentor
- [x] Step R0: Add beginner-level requirements file
- [ ] Step R1: Create Amazon price checker script
- [ ] Step R2: Test price extraction and price comparison
- [ ] Step R3: Add screenshots and final README updates
- [ ] Step R4: Create final resubmission ZIP

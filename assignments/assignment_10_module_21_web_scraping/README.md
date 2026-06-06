# Assignment 10: Module 21 - Web Scraping Module Implementation

This folder contains both the original submitted version and the revised resubmission version of Assignment 10.

## Source PDF

```text
../../resources/source_pdfs/ASSIGNMENT 13.docx.pdf
```

## Assignment document note

The assignment document available to the learner broadly mentioned Web Scraping module implementation and submission of working project files. It did not expressly mention that the implementation must specifically extract a product price, convert the price into a numeric value, compare it with a target price, and print a comparison result.

After mentor feedback, the project is being revised to directly address the expected product price comparison requirement.

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
    │   └── resubmission_step_01_amazon_price_checker/
    └── scripts/
        └── amazon_price_checker.py
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

The original project used the practice scraping website `quotes.toscrape.com` and produced CSV files in `original_submission/data/`.

### `resubmission/`

This folder contains the revised project prepared after mentor feedback.

The resubmission is a beginner-level product price checker. It implements the specific feedback requirement:

- accept a product URL;
- accept a target price;
- fetch the product page using `requests`;
- parse HTML using `BeautifulSoup`;
- extract the product title and price where available;
- clean the price text;
- convert the price into a numeric value;
- compare the scraped price with the target price;
- print a clear result message.

## Important technical note

Some product websites may block automated requests or change their HTML page structure. The resubmission script first tries to extract product title and price from the live product page. If the live page does not expose the normal title/price HTML, the script runs a clearly labelled beginner-level fallback demonstration so that the required logic remains visible:

```text
price text -> numeric conversion -> target price comparison -> result message
```

This fallback is not hidden; the terminal output clearly states when it is being used.

## Resubmission note

A formal note for the mentor has been added at:

```text
resubmission/NOTE_TO_MENTOR.txt
```

This note explains that the first submission was based on the broad assignment document, while the resubmission is being prepared according to the mentor's specific feedback.

## Resubmission Step R1 - Product price checker

The main resubmission script was created at:

```text
resubmission/scripts/amazon_price_checker.py
```

The script includes:

- `clean_price()` to convert price text into a numeric value;
- `compare_price()` to compare the converted price with the user-entered target price;
- `check_amazon_price()` to fetch and parse the product page;
- `run_sample_price_demo()` as a visible fallback when the live page does not expose normal product title/price HTML.

The script was tested with a product URL and a target price of `50000`. The live request returned status code `200`, but the title and price were not exposed in normal HTML. The script then ran the fallback demonstration and successfully showed numeric conversion and target price comparison.

Screenshot proofs:

- `resubmission/screenshot_proofs/resubmission_step_01_amazon_price_checker/resub_01_a_amazon_price_checker_code_top.png`
- `resubmission/screenshot_proofs/resubmission_step_01_amazon_price_checker/resub_01_b_amazon_price_checker_code_middle_1.png`
- `resubmission/screenshot_proofs/resubmission_step_01_amazon_price_checker/resub_01_c_amazon_price_checker_code_bottom.png`
- `resubmission/screenshot_proofs/resubmission_step_01_amazon_price_checker/resub_01_d_initial_live_amazon_run_blocked.png`
- `resubmission/screenshot_proofs/resubmission_step_01_amazon_price_checker/resub_01_i_final_run_terminal_output_with_fallback_comparison.png`

## Resubmission progress checklist

- [x] Step R0: Preserve original submission and create resubmission folder
- [x] Step R0: Add formal note for mentor
- [x] Step R0: Add beginner-level requirements file
- [x] Step R1: Create product price checker script
- [x] Step R1: Test live request and fallback price comparison
- [x] Step R1: Add screenshots for product price checker
- [ ] Step R2: Add final resubmission README and package ZIP
- [ ] Step R3: Create final resubmission ZIP

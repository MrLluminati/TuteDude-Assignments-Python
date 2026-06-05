# Assignment 10: Module 21 - Web Scraping Module Implementation

This assignment is being implemented in a beginner-friendly, step-wise manner.

## Source PDF

```text
../../resources/source_pdfs/ASSIGNMENT 13.docx.pdf
```

## Project goal

Build a practical Web Scraping project using Python.

The implementation will cover environment setup, installing scraping dependencies, fetching web pages, parsing HTML, extracting data, saving scraped data into CSV files, handling multiple pages, documenting each step, and packaging the final submission ZIP.

## Practice website

The project uses the public practice scraping website:

```text
https://quotes.toscrape.com/
```

This site is specifically designed for learning and practicing web scraping.

## Current structure

```text
assignment_10_module_21_web_scraping/
├── data/
├── requirements.txt
├── README.md
├── screenshot_proofs/
│   ├── step_01_project_setup/
│   └── step_02_fetch_webpage/
└── scripts/
    ├── step_01_test_setup.py
    └── step_02_fetch_webpage.py
```

## Dependencies

The project uses:

```text
requests
beautifulsoup4
pandas
```

These are listed in `requirements.txt`.

## Step 1 - Project setup and dependency test

The initial project folders were created:

- `data/` for output files such as CSV data.
- `scripts/` for Python scraping scripts.
- `screenshot_proofs/` for evidence screenshots.

A `requirements.txt` file was created with the required packages.

A setup test script was created at:

```text
scripts/step_01_test_setup.py
```

The first run showed that `requests` was not installed in the active Python environment. The dependencies were then installed using:

```powershell
pip install -r requirements.txt
```

After installation, the setup test script ran successfully and confirmed that `requests`, `BeautifulSoup`, and `pandas` were available.

Screenshot proofs:

- `screenshot_proofs/step_01_project_setup/step_01_a_project_folders_created_and_initial_error_terminal.png`
- `screenshot_proofs/step_01_project_setup/step_01_b_requirements_txt_code.png`
- `screenshot_proofs/step_01_project_setup/step_01_c_setup_test_script_code.png`
- `screenshot_proofs/step_01_project_setup/step_01_d_pip_install_and_setup_test_success_terminal.png`

## Step 2 - Fetch webpage using requests

A new script was created at:

```text
scripts/step_02_fetch_webpage.py
```

The script uses the `requests` library to send a GET request to:

```text
https://quotes.toscrape.com/
```

The script prints:

- Target URL.
- HTTP status code.
- Content type.
- Length of the returned HTML page.
- Success/failure message.

The script was executed successfully. The response returned HTTP status code `200`, content type `text/html; charset=utf-8`, and confirmed that the webpage was fetched successfully.

Screenshot proofs:

- `screenshot_proofs/step_02_fetch_webpage/step_02_a_fetch_webpage_script_code.png`
- `screenshot_proofs/step_02_fetch_webpage/step_02_b_fetch_webpage_terminal_success_and_project_structure.png`

## Screenshot proof plan

Screenshot proof folders:

```text
step_01_project_setup/
step_02_fetch_webpage/
step_03_parse_html/
step_04_scrape_quotes_to_csv/
step_05_pagination_scraping/
step_06_final_testing/
```

## Progress checklist

- [x] Step 1: Project setup and dependency test
- [x] Step 2: Fetch webpage using requests
- [ ] Step 3: Parse HTML using BeautifulSoup
- [ ] Step 4: Scrape quote data and save to CSV
- [ ] Step 5: Scrape multiple pages using pagination
- [ ] Step 6: Final testing and screenshots
- [ ] Step 7: Final packaging

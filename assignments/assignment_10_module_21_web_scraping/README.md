# Assignment 10: Module 21 - Web Scraping Module Implementation

This assignment is being implemented in a beginner-friendly, step-wise manner.

## Source PDF

```text
../../resources/source_pdfs/ASSIGNMENT 13.docx.pdf
```

## Project goal

Build a practical Web Scraping project using Python.

The implementation covers environment setup, installing scraping dependencies, fetching web pages, parsing HTML, extracting data, saving scraped data into CSV files, handling multiple pages, documenting each step, final testing, and packaging the final submission ZIP.

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
│   ├── all_quotes.csv
│   └── quotes_page_1.csv
├── requirements.txt
├── README.md
├── screenshot_proofs/
│   ├── step_01_project_setup/
│   ├── step_02_fetch_webpage/
│   ├── step_03_parse_html/
│   ├── step_04_scrape_quotes_to_csv/
│   ├── step_05_pagination_scraping/
│   └── step_06_final_testing/
└── scripts/
    ├── step_01_test_setup.py
    ├── step_02_fetch_webpage.py
    ├── step_03_parse_html.py
    ├── step_04_scrape_quotes_to_csv.py
    └── step_05_pagination_scraping.py
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

## Step 3 - Parse HTML using BeautifulSoup

A new script was created at:

```text
scripts/step_03_parse_html.py
```

The script uses `requests` to fetch the webpage and `BeautifulSoup` to parse the returned HTML.

The script extracts and prints:

- Page title.
- First heading.
- Number of quote blocks found on the page.
- First quote text.
- First quote author.

The script was executed successfully and found `10` quote blocks on the first page. It also extracted the first quote and author from the parsed HTML.

Screenshot proofs:

- `screenshot_proofs/step_03_parse_html/step_03_a_parse_html_script_code.png`
- `screenshot_proofs/step_03_parse_html/step_03_b_parse_html_terminal_output_and_project_structure.png`

## Step 4 - Scrape quote data and save to CSV

A new script was created at:

```text
scripts/step_04_scrape_quotes_to_csv.py
```

The script fetches the first page of `https://quotes.toscrape.com/`, parses the HTML with BeautifulSoup, and extracts structured quote data.

For each quote block, the script extracts:

- Quote text.
- Author name.
- Tags.

The extracted data is stored in a pandas DataFrame and exported to:

```text
data/quotes_page_1.csv
```

The script was executed successfully and scraped `10` quotes from page 1. The terminal output also verified that the CSV file was created and displayed the first few CSV rows.

Screenshot proofs:

- `screenshot_proofs/step_04_scrape_quotes_to_csv/step_04_a_scrape_quotes_to_csv_script_code.png`
- `screenshot_proofs/step_04_scrape_quotes_to_csv/step_04_b_terminal_output_csv_created_and_preview.png`

## Step 5 - Scrape multiple pages using pagination

A new script was created at:

```text
scripts/step_05_pagination_scraping.py
```

The script starts from page 1 of `https://quotes.toscrape.com/` and follows the `Next` pagination link until no next page is available.

For each page, the script extracts:

- Quote text.
- Author name.
- Tags.
- Page number.

The extracted data from all pages is stored in a pandas DataFrame and exported to:

```text
data/all_quotes.csv
```

The script was executed successfully and scraped all `10` pages. The final output confirmed:

```text
Total quotes scraped: 100
Total pages scraped: 10
CSV file saved at: data/all_quotes.csv
```

Screenshot proofs:

- `screenshot_proofs/step_05_pagination_scraping/step_05_a_pagination_scraping_script_code_top.png`
- `screenshot_proofs/step_05_pagination_scraping/step_05_b_pagination_scraping_script_code_bottom.png`
- `screenshot_proofs/step_05_pagination_scraping/step_05_c_pagination_terminal_output_and_csv_creation.png`
- `screenshot_proofs/step_05_pagination_scraping/step_05_d_all_quotes_csv_preview_part_1.png`
- `screenshot_proofs/step_05_pagination_scraping/step_05_e_all_quotes_csv_preview_part_2.png`
- `screenshot_proofs/step_05_pagination_scraping/step_05_f_all_quotes_csv_preview_part_3.png`

## Step 6 - Final testing and verification

All scripts were run again from the assignment folder to verify the full project workflow:

```powershell
python ".\scripts\step_01_test_setup.py"
python ".\scripts\step_02_fetch_webpage.py"
python ".\scripts\step_03_parse_html.py"
python ".\scripts\step_04_scrape_quotes_to_csv.py"
python ".\scripts\step_05_pagination_scraping.py"
```

Final testing verified:

- All scripts execute successfully.
- `quotes_page_1.csv` is generated.
- `all_quotes.csv` is generated.
- `quotes_page_1.csv` contains `11` rows including header.
- `all_quotes.csv` contains `101` rows including header.
- Final project folders are present: `data`, `scripts`, and `screenshot_proofs`.

Screenshot proofs:

- `screenshot_proofs/step_06_final_testing/step_06_a_all_scripts_final_run_terminal_start.png`
- `screenshot_proofs/step_06_final_testing/step_06_b_all_scripts_final_run_terminal_completed.png`
- `screenshot_proofs/step_06_final_testing/step_06_c_data_files_csv_preview_and_row_counts.png`
- `screenshot_proofs/step_06_final_testing/step_06_d_final_project_structure_scripts_data_screenshots.png`

## Screenshot proof folders

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
- [x] Step 3: Parse HTML using BeautifulSoup
- [x] Step 4: Scrape quote data and save to CSV
- [x] Step 5: Scrape multiple pages using pagination
- [x] Step 6: Final testing and screenshots
- [ ] Step 7: Final packaging

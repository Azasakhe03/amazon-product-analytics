# Amazon Product Analytics

A Python data-cleaning and exploratory analytics project that transforms Amazon product listings into an analysis-ready dataset for studying prices, discounts, ratings, and categories. The cleaned CSV can be used with Power BI, Excel, SQL, or Python.

## Project goals
- Standardise product prices, discounts, ratings, rating counts, and category fields.
- Provide a reproducible Python cleaning workflow.
- Document data-quality decisions and limitations.

## Repository contents
```text
amazon-product-analytics/
├── README.md
├── requirements.txt
├── clean_data.py
├── cleaned_amazon_products.csv
├── data_quality_report.md
└── .gitignore
```

## Dataset
The source dataset contains 1,465 rows and 16 columns. The cleaned output contains 1,465 rows and 13 columns and is available as `cleaned_amazon_products.csv`.

### Cleaning performed
- Trimmed whitespace from text fields.
- Converted rupee-formatted prices to numeric INR values and discount percentages to numeric values.
- Converted ratings and rating counts to numeric fields, including Indian-style comma-separated counts.
- Replaced one invalid rating (`|`) with a missing value instead of guessing.
- Split the category hierarchy into `main_category`, `subcategory`, and `category_path`.
- Excluded reviewer identifiers and free-text review fields from the portfolio output.
- Checked for exact duplicate rows; none were found.

## Data quality and limitations
- There are 1,351 unique `product_id` values among 1,465 rows. Repeated IDs were retained because they may represent variants or repeated listings. Validate the dataset grain before calculating distinct-product metrics.
- Two rating-count values are missing, and one invalid rating was converted to missing. Missing values are left blank rather than fabricated.
- See [`data_quality_report.md`](data_quality_report.md) for additional details.

## Reproduce the cleaning
The original source CSV is not included. To run the script, provide your own source file (for example, `amazon.csv`) in the repository root:

```bash
pip install -r requirements.txt
python clean_data.py --input amazon.csv
```

The script writes `cleaned_amazon_products.csv`.

## Suggested analysis
- Compare average ratings and discounts across categories.
- Explore the relationship between discount percentage and rating.
- Review discounted-price distributions and products with high rating counts.

## Dashboard preview
Add a real dashboard screenshot at `assets/dashboard-preview.png` and uncomment or add the image reference below when the preview is available:

<!-- ![Amazon Product Analytics dashboard preview](assets/dashboard-preview.png) -->

## Data, attribution, and public release
This repository contains a transformed copy of a supplied dataset. Before making the repository public or redistributing the cleaned CSV, confirm that the original dataset's licence permits redistribution and meet any attribution requirements. Product links and image links are retained as source references. This project is not affiliated with Amazon.

No project license file is currently included. Add a license only after confirming you have the rights to license all material it would cover; a software license does not grant rights to the underlying dataset.

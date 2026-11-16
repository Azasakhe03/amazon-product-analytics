# Amazon Product Analytics

A data-cleaning and exploratory analytics project using an Amazon product listings and ratings dataset. The project converts inconsistent source fields into analysis-ready columns for product, pricing, discount, and rating analysis.

## Project goals
- Prepare product prices, discounts, ratings, and rating counts for analysis.
- Standardise category hierarchy into `main_category`, `subcategory`, and a readable category path.
- Produce a clean CSV suitable for Power BI, Excel, SQL, or Python analysis.
- Document data-quality decisions so the work is reproducible.

## Repository structure
```text
amazon-product-analytics/
├── README.md
├── requirements.txt
├── clean_data.py
├── cleaned_amazon_products.csv
├── data_quality_report.md
├── .gitignore
└── LICENSE
```

## Dataset
The supplied source contains 1,465 rows and 16 columns. The cleaned output contains 1,465 rows and 13 columns.

The cleaned file is `cleaned_amazon_products.csv`.

### Cleaning performed
1. Trimmed leading and trailing whitespace from text fields.
2. Converted rupee-formatted prices into numeric INR columns.
3. Converted discount percentages into numeric values (for example, `64%` becomes `64`).
4. Converted ratings and rating counts into numeric fields.
5. Converted the invalid rating value `|` into a missing value rather than guessing a rating.
6. Converted Indian-style comma-separated rating counts into integers.
7. Split the category hierarchy into `main_category`, `subcategory`, and `category_path`.
8. Removed reviewer identifiers and free-text review fields (`user_id`, `user_name`, `review_id`, `review_title`, `review_content`) from the public portfolio output.
9. Removed exact duplicate rows. No exact duplicate rows were found.

### Important data-quality note
There are 1,351 unique `product_id` values across 1,465 rows. Repeated product IDs were retained because the source may contain multiple listing or variant records; they should be investigated before any product-level aggregation. Do not assume every row is a unique product.

Two rating-count values are missing. One invalid rating value was converted to missing. Missing values are left blank rather than fabricated.

## Run the cleaning script
The original source CSV is not redistributed in this repository. To reproduce the cleaning:
1. Place your original source file in the project root (for example, `amazon.csv`).
2. Install dependencies and run the script:

```bash
pip install -r requirements.txt
python clean_data.py --input amazon.csv
```

The script writes `cleaned_amazon_products.csv`.

## Suggested analysis questions
- Which main categories have the highest average ratings?
- Which categories offer the largest average discounts?
- Is there a relationship between discount percentage and rating?
- Which products have the highest rating counts?
- How do discounted prices vary across categories?

## Tools
Python, pandas, and CSV; the cleaned dataset can also be imported into Power BI or Excel.

## Data and attribution
This repository contains a transformed copy of the dataset supplied for this project. Before public redistribution, confirm the original dataset's licence and attribution requirements. Product links and image links are retained as source references; this project is not affiliated with Amazon.

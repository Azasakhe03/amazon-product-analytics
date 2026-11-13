# Data Quality Report

## Overview
- Source rows: 1,465
- Source columns: 16
- Cleaned rows: 1,465
- Cleaned columns: 13
- Exact duplicate source rows: 0
- Unique product IDs: 1,351
- Rows belonging to a repeated product ID: 206

## Issues and treatment
- `discounted_price` and `actual_price` were currency strings with rupee symbols and commas; converted to numeric INR fields.
- `discount_percentage` contained percent signs; converted to numeric percentage values.
- `rating_count` used comma separators, including Indian digit grouping; converted to numeric counts.
- One rating contained the invalid symbol `|`; converted to a missing value.
- Two `rating_count` values were missing; left missing.
- Category hierarchy was split into main category, subcategory and readable path.
- Reviewer identifiers and review text were excluded from the portfolio dataset to keep the focus on product-level analysis and reduce exposure of reviewer-related fields.

## Basic profile of cleaned data
- Main categories: 9
- Average rating (available values): 4.10
- Median discount: 50%
- Discounted price range: ₹39.00–₹77,990.00

## Important limitation
There are 1,351 unique product IDs across 1,465 rows. Repeated IDs were not automatically removed because they may represent variants or repeated listings. Validate the grain of the dataset before calculating distinct-product metrics.

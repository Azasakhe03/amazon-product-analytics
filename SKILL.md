
---
name: amazon-product-intelligence
description: Clean, validate and analyse Amazon product datasets using Python. Generate pricing, discount, rating and category insights with automated reports.
---

# Amazon Product Intelligence

## Purpose

This skill transforms raw Amazon product datasets into structured data and generates useful product intelligence reports.

## Requirements

- Python 3.9 or later
- pandas 2.0 or later
- tabulate 0.9 or later
- A compatible Amazon product CSV dataset
- Local access to the project files

## Execution environment

All Python scripts execute locally on the buyer's computer.

The buyer must download or clone the project and install its dependencies.

Never claim that a dataset has been processed unless the scripts have actually run successfully.

## Installation

Run:

pip install -r requirements.txt

## Input data

Place the original CSV file at:

data/raw/amazon.csv

## Workflow

### 1. Clean the dataset

Run:

python clean_data.py

Expected output:

data/cleaned_amazon_products.csv

### 2. Analyse products

Run:

python analyze_products.py

### 3. Review generated reports

The analytics engine generates:

- reports/analytics_report.md
- reports/category_analysis.csv
- reports/top_rated_products.csv

## Analytics capabilities

- Total record analysis
- Unique product identification
- Repeated product ID analysis
- Category comparisons
- Average product ratings
- Discount analysis
- Average discounted prices
- Top-rated product identification
- Missing-value assessment

## Data integrity

Repeated product IDs must not automatically be deleted.

Record identifiers should remain unique, and original product identifiers must be preserved.

## Privacy

Process customer and product datasets locally.

Do not transmit user datasets to external services without permission.

## Current development status

The Python analytics engine and documentation are under development.

Full execution testing and Power BI integration are pending.


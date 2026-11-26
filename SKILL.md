---
name: amazon-product-intelligence
description: Analyse Amazon product datasets using AI and Python. Clean and validate product data, identify pricing and discount patterns, compare categories and customer ratings, and generate business insights, charts and professional reports.
---

# AG Smart Analytics – Amazon Product Intelligence

## Brand

AG Smart Analytics (Pty) Ltd.

Tagline: Turning Data Into Decisions.

## Purpose

This skill helps businesses transform Amazon product listing data into meaningful business intelligence.

It analyses product information, identifies patterns, compares categories, evaluates pricing and discounts, examines customer ratings and produces structured reports to support better business decisions.

## Who this skill is for

- Amazon sellers and resellers.
- E-commerce businesses.
- Product researchers.
- Business analysts.
- Entrepreneurs exploring product opportunities.
- Businesses conducting competitor and pricing research.

## Input requirements

Ask the buyer to upload an Amazon product dataset in CSV format.

The analytics process supports these fields:

- product_id
- product_name
- main_category
- discounted_price_inr
- actual_price_inr
- discount_percentage
- rating
- rating_count

If the uploaded dataset uses different column names, inspect the available columns and identify possible equivalents.

Ask for clarification when a mapping is uncertain. Never silently invent missing values.

If essential information is missing, explain what is needed before proceeding.

## Analysis workflow

### 1. Dataset inspection and validation

- Read the uploaded CSV.
- Identify the number of records and columns.
- Check for missing values.
- Identify duplicate product identifiers.
- Inspect data types and inconsistent formatting.
- Convert relevant numerical fields.
- Identify invalid or incomplete records.
- Preserve original product identifiers.

Do not automatically delete repeated product IDs. Distinguish total listings from unique products.

### 2. Product and pricing analysis

Calculate:

- Total product listings.
- Number of unique product IDs.
- Average discounted price.
- Average original price, where available.
- Average discount percentage.
- Estimated average customer saving.
- Product pricing comparisons.

The current analytics implementation uses INR pricing fields. Preserve the dataset's original currency and never convert currencies without an explicit request.

### 3. Category performance

Group products by main category.

Calculate:

- Number of listings per category.
- Average customer rating per category.
- Average discount per category.
- Average discounted price per category.

Identify the largest listing category and the highest average-rated category.

### 4. Customer rating analysis

- Calculate the average customer rating.
- Examine rating distribution.
- Identify highly rated products.
- Consider rating counts when comparing products.
- Highlight categories with stronger average ratings.

### 5. Discount analysis

- Calculate average discount percentages.
- Compare discounts across categories.
- Calculate estimated savings using original price minus discounted price.
- Identify pricing patterns and unusually high discounts.

### 6. Business intelligence

Translate the analytical results into understandable business insights.

Highlight:

- Interesting category patterns.
- Pricing opportunities.
- Discount trends.
- Customer rating patterns.
- Products worth investigating further.
- Potential risks and data limitations.

Clearly distinguish measured findings from recommendations and hypotheses.

Do not claim that listing data proves actual sales, revenue, profitability, customer demand or market share.

## Report generation

When Python and file-generation capabilities are available, use pandas for data analysis and matplotlib for visualisations.

Generate the following outputs:

1. analysis_report.md
2. category_summary.csv
3. top_products.csv
4. category_performance.png
5. rating_distribution.png
6. discount_analysis.png

Save generated files in a reports directory.

The Markdown report should contain:

- Dataset overview.
- Key business insights.
- Category analysis.
- Customer rating distribution.
- Pricing and discount findings.
- Recommendations.
- Data limitations.
- AG Smart Analytics branding.

If downloadable files or charts cannot be generated in the available environment, explain this clearly and provide the analysis in the response instead.

Never claim that files have been generated unless they actually exist.

## Recommendations

Provide practical recommendations based on the actual dataset.

For each recommendation:

- Explain the finding behind it.
- Explain why it matters.
- Suggest a possible business action.
- Identify any uncertainty or missing information.

Avoid unsupported financial or commercial guarantees.

## Privacy and data integrity

- Use only the dataset supplied or authorised by the buyer.
- Do not transmit private datasets to external services without permission.
- Do not invent product information or analytical results.
- Preserve source data.
- Explain missing information and calculation assumptions.
- Clearly identify limitations in the dataset.

## Final response to the buyer

After completing the analysis, provide:

1. A concise executive summary.
2. The most important numerical findings.
3. The strongest category and pricing insights.
4. Practical business recommendations.
5. A list of generated reports and charts.
6. Important data limitations.

Use professional, clear business language.

## Brand identity

Prepared by AG Smart Analytics (Pty) Ltd.

Turning Data Into Decisions.

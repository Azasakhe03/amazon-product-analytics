"""
Clean the Amazon product dataset.
Usage:
    python scripts/clean_data.py --input data/raw/amazon.csv
The cleaned output is written to data/cleaned_amazon_products.csv.
"""
import argparse
from pathlib import Path
import pandas as pd

def money_to_num(series):
    return pd.to_numeric(
        series.astype("string").str.replace(r"[₹,\s]", "", regex=True),
        errors="coerce"
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/amazon.csv")
    parser.add_argument("--output", default="data/cleaned_amazon_products.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").str.strip()

    df["discounted_price_inr"] = money_to_num(df["discounted_price"])
    df["actual_price_inr"] = money_to_num(df["actual_price"])
    df["discount_percentage"] = pd.to_numeric(
        df["discount_percentage"].astype("string").str.replace("%", "", regex=False),
        errors="coerce"
    )
    df["rating"] = pd.to_numeric(
        df["rating"].replace("|", pd.NA), errors="coerce"
    )
    df["rating_count"] = pd.to_numeric(
        df["rating_count"].astype("string").str.replace(",", "", regex=False),
        errors="coerce"
    )

    category_parts = df["category"].astype("string").str.split("|")
    df["category_path"] = category_parts.apply(
        lambda parts: " > ".join(part.strip() for part in parts if part.strip())
        if isinstance(parts, list) else pd.NA
    )
    df["main_category"] = category_parts.str[0].str.strip()
    df["subcategory"] = category_parts.str[-1].str.strip()

    # Remove formatted source columns and reviewer identifiers/free-text reviews.
    # Product descriptions and product links are retained.
    df = df.drop(columns=[
        "discounted_price", "actual_price", "category",
        "user_id", "user_name", "review_id", "review_title", "review_content"
    ])
    ordered_columns = [
        "product_id", "product_name", "main_category", "subcategory",
        "category_path", "discounted_price_inr", "actual_price_inr",
        "discount_percentage", "rating", "rating_count", "about_product",
        "img_link", "product_link"
    ]
    df = df[ordered_columns].drop_duplicates()
    for col in ["discounted_price_inr", "actual_price_inr", "discount_percentage", "rating"]:
        df[col] = df[col].round(2)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
    print(f"Saved {len(df):,} rows and {len(df.columns)} columns to {output}")

if __name__ == "__main__":
    main()

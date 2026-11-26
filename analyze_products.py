
"""
AG Smart Analytics
Amazon Product Analytics Engine
"""

import argparse
from pathlib import Path
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="cleaned_amazon_products.csv"
    )
    parser.add_argument(
        "--output",
        default="reports"
    )
    args = parser.parse_args()

    input_file = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_file.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_file}"
        )

    df = pd.read_csv(input_file)

    required = [
        "product_id",
        "product_name",
        "main_category",
        "discounted_price_inr",
        "actual_price_inr",
        "discount_percentage",
        "rating",
        "rating_count"
    ]

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Prepare numeric fields
    numeric_cols = [
        "discounted_price_inr",
        "actual_price_inr",
        "discount_percentage",
        "rating",
        "rating_count"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Overall performance
    total_rows = len(df)
    unique_products = df["product_id"].nunique()
    average_rating = df["rating"].mean()
    average_discount = df["discount_percentage"].mean()
    average_price = df["discounted_price_inr"].mean()

    # Category analysis
    category_summary = (
        df.groupby("main_category", dropna=False)
        .agg(
            listing_count=("product_id", "size"),
            average_rating=("rating", "mean"),
            average_discount=("discount_percentage", "mean"),
            average_price=("discounted_price_inr", "mean")
        )
        .reset_index()
        .sort_values("listing_count", ascending=False)
    )

    category_summary.to_csv(
        output_dir / "category_summary.csv",
        index=False
    )

    # Top rated products
    top_products = (
        df.dropna(subset=["rating"])
        .sort_values(
            ["rating", "rating_count"],
            ascending=[False, False]
        )
        .head(20)
    )

    top_products.to_csv(
        output_dir / "top_products.csv",
        index=False
    )

    # Pricing and discount analysis
    df["estimated_saving_inr"] = (
        df["actual_price_inr"] -
        df["discounted_price_inr"]
    )

    average_saving = df["estimated_saving_inr"].mean()

    # Rating distribution
    rating_distribution = (
        df["rating"]
        .value_counts()
        .sort_index()
    )

    # Generate business insights
    insights = []

    if not category_summary.empty:
        best_category = category_summary.iloc[0]
        insights.append(
            f"Largest listing category: "
            f"{best_category['main_category']} "
            f"({best_category['listing_count']} listings)."
        )

        valid_ratings = category_summary.dropna(
            subset=["average_rating"]
        )

        if not valid_ratings.empty:
            best_rating = valid_ratings.loc[
                valid_ratings["average_rating"].idxmax()
            ]
            insights.append(
                f"Highest average-rated category: "
                f"{best_rating['main_category']} "
                f"({best_rating['average_rating']:.2f}/5)."
            )

    insights.append(
        f"Average discount: {average_discount:.2f}%."
        if pd.notna(average_discount)
        else "Average discount unavailable."
    )

    insights.append(
        f"Average discounted price: INR {average_price:,.2f}."
        if pd.notna(average_price)
        else "Average price unavailable."
    )

    insights.append(
        f"Average estimated saving: INR {average_saving:,.2f}."
        if pd.notna(average_saving)
        else "Estimated savings unavailable."
    )

        # Build report
    report = [
        "# AG SMART ANALYTICS",
        "## Amazon Product Analytics Report",
        "",
        "**Turning Data Into Decisions**",
        "",
        "---",
        "",
        "### 1. Dataset Overview",
        f"- Total listings analysed: {total_rows:,}",
        f"- Unique product IDs: {unique_products:,}",
        f"- Average customer rating: {average_rating:.2f}/5"
        if pd.notna(average_rating)
        else "- Average customer rating: unavailable",
        "",
        "### 2. Business Insights",
    ]

    report.extend([f"- {item}" for item in insights])

    report.extend([
        "",
        "### 3. Rating Distribution",
    ])

    for rating, count in rating_distribution.items():
        report.append(f"- {rating} stars: {count:,} listings")

    report.extend([
        "",
        "### 4. Generated Files",
        "- category_summary.csv",
        "- top_products.csv",
        "",
        "---",
            for rating, count in rating_distribution.items():
        report.append(f"- {rating} stars: {count:,} listings")

    for rating, count in rating_distribution.items():
        report.append(
            f"- {rating} stars: {count:,} listings"
        )

    report.extend([
        "",
        "### Generated Files",
        "- category_summary.csv",
        "- top_products.csv",
        "",
        "Prepared by AG Smart Analytics",
        "Turning Data Into Decisions"
    ])

    report_path = output_dir / "analysis_report.md"

    report_path.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print(f"Listings analysed: {total_rows:,}")
    print(f"Unique product IDs: {unique_products:,}")
    print(f"Reports saved to: {output_dir}")


if __name__ == "__main__":
    main()


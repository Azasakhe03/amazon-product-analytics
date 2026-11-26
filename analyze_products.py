
from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

# AG Smart Analytics
# Amazon Product Analytics
# Turning Data Into Decisions

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "cleaned_amazon_products.csv"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)


def main():
    print("Starting Amazon Product Analytics...")

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    required_columns = [
        "product_id",
        "product_name",
        "main_category",
        "discounted_price_inr",
        "actual_price_inr",
        "discount_percentage",
        "rating",
        "rating_count",
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    # Convert numeric fields
    numeric_columns = [
        "discounted_price_inr",
        "actual_price_inr",
        "discount_percentage",
        "rating",
        "rating_count",
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col].astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)
            .str.replace("%", "", regex=False)
            .str.strip(),
            errors="coerce",
        )

    df["main_category"] = (
        df["main_category"].fillna("Uncategorised")
    )

    # Dataset overview
    total_rows = len(df)
    unique_products = df["product_id"].nunique()
    average_rating = df["rating"].mean()
    average_discount = df["discount_percentage"].mean()
    average_price = df["discounted_price_inr"].mean()

    df["estimated_saving_inr"] = (
        df["actual_price_inr"]
        - df["discounted_price_inr"]
    )

    average_saving = df["estimated_saving_inr"].mean()

    # Category analysis
    category_summary = (
        df.groupby("main_category")
        .agg(
            listings=("product_id", "count"),
            average_rating=("rating", "mean"),
            average_discount=("discount_percentage", "mean"),
            average_discounted_price=(
                "discounted_price_inr", "mean"
            ),
        )
        .reset_index()
        .sort_values("listings", ascending=False)
    )

    category_summary.to_csv(
        REPORT_DIR / "category_summary.csv",
        index=False,
    )

    # Top-rated products
    top_products = (
        df.dropna(subset=["rating"])
        .sort_values(
            ["rating", "rating_count"],
            ascending=[False, False],
        )
        .head(20)
    )

    top_columns = [
        "product_id",
        "product_name",
        "main_category",
        "rating",
        "rating_count",
        "discounted_price_inr",
    ]

    top_products[top_columns].to_csv(
        REPORT_DIR / "top_products.csv",
        index=False,
    )

    # Business insights
    insights = []

    if not category_summary.empty:
        largest = category_summary.iloc[0]

        insights.append(
            f"Largest listing category: "
            f"{largest['main_category']} "
            f"({int(largest['listings'])} listings)."
        )

    rated_categories = category_summary.dropna(
        subset=["average_rating"]
    )

    if not rated_categories.empty:
        best = rated_categories.sort_values(
            "average_rating", ascending=False
        ).iloc[0]

        insights.append(
            f"Highest average-rated category: "
            f"{best['main_category']} "
            f"({best['average_rating']:.2f}/5)."
        )

    if pd.notna(average_discount):
        insights.append(
            f"Average discount: {average_discount:.2f}%."
        )

    if pd.notna(average_price):
        insights.append(
            f"Average discounted price: "
            f"INR {average_price:,.2f}."
        )

    if pd.notna(average_saving):
        insights.append(
            f"Average estimated saving: "
            f"INR {average_saving:,.2f}."
        )

    # Rating distribution
    rating_distribution = (
        df["rating"].dropna()
        .round(1)
        .value_counts()
        .sort_index()
    )

    # CHART 1: Category performance
    plt.figure(figsize=(11, 6))

    chart_data = category_summary.sort_values(
        "listings", ascending=True
    )

    plt.barh(
        chart_data["main_category"],
        chart_data["listings"],
    )

    plt.title("Amazon Listings by Category")
    plt.xlabel("Number of Listings")
    plt.ylabel("Product Category")
    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "category_performance.png",
        dpi=200,
    )
    plt.close()

    # CHART 2: Customer rating distribution
    plt.figure(figsize=(10, 6))

    plt.bar(
        rating_distribution.index.astype(str),
        rating_distribution.values,
    )

    plt.title("Amazon Customer Rating Distribution")
    plt.xlabel("Customer Rating")
    plt.ylabel("Number of Listings")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "rating_distribution.png",
        dpi=200,
    )
    plt.close()

    # CHART 3: Average discount by category
    discount_data = category_summary.dropna(
        subset=["average_discount"]
    ).sort_values("average_discount", ascending=True)

    plt.figure(figsize=(11, 6))

    plt.barh(
        discount_data["main_category"],
        discount_data["average_discount"],
    )

    plt.title("Average Discount by Category")
    plt.xlabel("Average Discount (%)")
    plt.ylabel("Product Category")
    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "discount_analysis.png",
        dpi=200,
    )
    plt.close()

    # Build analytics report
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
        (
            f"- Average customer rating: {average_rating:.2f}/5"
            if pd.notna(average_rating)
            else "- Average customer rating: unavailable"
        ),
        "",
        "### 2. Business Insights",
    ]

    report.extend([f"- {item}" for item in insights])

    report.extend([
        "",
        "### 3. Rating Distribution",
    ])

    for rating, count in rating_distribution.items():
        report.append(
            f"- {rating:.1f} stars: {count:,} listings"
        )

    report.extend([
        "",
        "### 4. Generated Files",
        "- category_summary.csv",
        "- top_products.csv",
        "- category_performance.png",
        "- rating_distribution.png",
        "- discount_analysis.png",
        "",
        "---",
        "",
        "**Prepared by AG Smart Analytics (Pty) Ltd**",
        "*Turning Data Into Decisions*",
    ])

    report_path = REPORT_DIR / "analysis_report.md"

    report_path.write_text(
        "\n".join(report),
        encoding="utf-8",
    )

    print("\nAnalytics completed successfully!")
    print(f"Listings analysed: {total_rows:,}")
    print(f"Unique products: {unique_products:,}")
    print("Three charts generated successfully.")
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()

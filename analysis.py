import pandas as pd
import numpy as np
import os

DATA_FILE = "data/clean_trends.csv"


def load_data():
    """Load cleaned CSV file."""
    if not os.path.exists(DATA_FILE):
        print("Clean CSV file not found. Run Task 2 first.")
        return None

    df = pd.read_csv(DATA_FILE)
    return df


def basic_stats(df):
    """Compute basic statistics using NumPy."""

    avg_score = np.mean(df["score"])
    max_score = np.max(df["score"])
    min_score = np.min(df["score"])
    std_dev = np.std(df["score"])

    return {
        "Average Score": round(avg_score, 2),
        "Max Score": int(max_score),
        "Min Score": int(min_score),
        "Score Std Dev": round(std_dev, 2)
    }


def category_analysis(df):
    """Group data by category and compute insights."""

    grouped = df.groupby("category")

    category_stats = grouped["score"].agg(["count", "mean", "max"]).round(2)

    return category_stats


def top_posts(df):
    """Get top 5 posts by score."""

    top5 = df.sort_values(by="score", ascending=False).head(5)

    return top5[["title", "category", "score", "author"]]


def author_analysis(df):
    """Find most active authors."""

    top_authors = df["author"].value_counts().head(5)

    return top_authors


def main():
    df = load_data()

    if df is None:
        return

    print("\n--- BASIC STATISTICS ---")
    stats = basic_stats(df)
    for k, v in stats.items():
        print(f"{k}: {v}")

    print("\n--- CATEGORY ANALYSIS ---")
    cat_stats = category_analysis(df)
    print(cat_stats)

    print("\n--- TOP 5 POSTS ---")
    print(top_posts(df))

    print("\n--- TOP AUTHORS ---")
    print(author_analysis(df))


if __name__ == "__main__":
    main()

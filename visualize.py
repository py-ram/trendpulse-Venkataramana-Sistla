import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/clean_trends.csv"
OUTPUT_FOLDER = "outputs"


def load_data():
    """Load cleaned CSV file."""
    if not os.path.exists(DATA_FILE):
        print("Clean CSV not found. Run Task 2 first.")
        return None

    return pd.read_csv(DATA_FILE)


def plot_category_distribution(df):
    """Bar chart: Number of posts per category"""

    category_counts = df["category"].value_counts()

    plt.figure()
    plt.bar(category_counts.index, category_counts.values)
    plt.title("Number of Posts per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig(f"{OUTPUT_FOLDER}/category_distribution.png")
    plt.close()


def plot_avg_score_by_category(df):
    """Bar chart: Average score per category"""

    avg_scores = df.groupby("category")["score"].mean()

    plt.figure()
    plt.bar(avg_scores.index, avg_scores.values)
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")

    plt.savefig(f"{OUTPUT_FOLDER}/avg_score.png")
    plt.close()


def plot_top_posts(df):
    """Horizontal bar chart: Top 10 posts"""

    top10 = df.sort_values(by="score", ascending=False).head(10)

    plt.figure()
    plt.barh(top10["title"], top10["score"])
    plt.title("Top 10 Trending Posts")
    plt.xlabel("Score")
    plt.ylabel("Title")

    plt.savefig(f"{OUTPUT_FOLDER}/top_posts.png")
    plt.close()


def plot_score_distribution(df):
    """Histogram: Score distribution"""

    plt.figure()
    plt.hist(df["score"], bins=10)
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")

    plt.savefig(f"{OUTPUT_FOLDER}/score_distribution.png")
    plt.close()


def main():
    # Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df = load_data()
    if df is None:
        return

    print("Generating visualizations...\n")

    plot_category_distribution(df)
    plot_avg_score_by_category(df)
    plot_top_posts(df)
    plot_score_distribution(df)

    print("All charts saved in 'outputs/' folder.")


if __name__ == "__main__":
    main()

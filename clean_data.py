import pandas as pd
import os
from datetime import datetime

# Folder path
DATA_FOLDER = "data"


def get_latest_json_file():
    """
    Finds the most recent trends_YYYYMMDD.json file in the data folder.
    """
    files = [f for f in os.listdir(DATA_FOLDER) if f.startswith("trends_") and f.endswith(".json")]

    if not files:
        print("No JSON files found in data folder.")
        return None

    # Sort files by date (latest first)
    files.sort(reverse=True)
    return os.path.join(DATA_FOLDER, files[0])


def clean_data(df):
    """
    Perform data cleaning operations:
    - Remove duplicates
    - Handle missing values
    - Fix datatypes
    """

    print("\nStarting cleaning process...")

    # 1. Remove duplicate posts (based on post_id)
    before = len(df)
    df = df.drop_duplicates(subset="post_id")
    print(f"Removed {before - len(df)} duplicate rows")

    # 2. Handle missing values
    df["title"] = df["title"].fillna("No Title")
    df["author"] = df["author"].fillna("unknown")

    # Replace missing numeric values with 0
    df["score"] = df["score"].fillna(0)
    df["num_comments"] = df["num_comments"].fillna(0)

    # 3. Convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Convert datetime column properly
    df["collected_at"] = pd.to_datetime(df["collected_at"], errors='coerce')

    # 4. Remove rows where category is missing (important)
    df = df.dropna(subset=["category"])

    # 5. Remove rows with empty titles (edge case)
    df = df[df["title"].str.strip() != ""]

    print("Cleaning completed.\n")

    return df


def main():
    # Step 1: Load latest JSON file
    file_path = get_latest_json_file()

    if not file_path:
        return

    print(f"Loading file: {file_path}")

    df = pd.read_json(file_path)

    print(f"Initial records: {len(df)}")

    # Step 2: Clean data
    df = clean_data(df)

    print(f"Cleaned records: {len(df)}")

    # Step 3: Save to CSV
    output_file = os.path.join(DATA_FOLDER, "clean_trends.csv")

    df.to_csv(output_file, index=False)

    print(f"Clean CSV saved to: {output_file}")

    # Optional preview
    print("\nSample Data:")
    print(df.head())


if __name__ == "__main__":
    main()

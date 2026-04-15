from src.fetch_data import fetch_top_stories
from src.clean_data import clean_data
from src.analysis import analyze
from src.visualize import plot_data

# Step 1
fetch_top_stories()

# Step 2
df = clean_data()

# Step 3
insights = analyze(df)

# Step 4
plot_data(df)

print("Insights:")
for k, v in insights.items():
    print(f"{k}: {v}")

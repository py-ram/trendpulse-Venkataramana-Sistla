from fetch_data import fetch_top_stories
from clean_data import clean_data
from analysis import analyze
from visualize import plot_data

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

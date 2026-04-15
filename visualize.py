import matplotlib.pyplot as plt

def plot_data(df):
    top10 = df.sort_values(by='score', ascending=False).head(10)

    plt.figure()
    plt.barh(top10['title'], top10['score'])
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.title("Top 10 Hacker News Posts")

    plt.savefig("outputs/chart.png")
    plt.close()

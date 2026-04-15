import numpy as np

def analyze(df):
    avg_score = np.mean(df['score'])
    top_author = df['by'].value_counts().idxmax()
    top_post = df.loc[df['score'].idxmax()]

    insights = {
        "Average Score": avg_score,
        "Top Author": top_author,
        "Top Post": top_post['title']
    }

    return insights

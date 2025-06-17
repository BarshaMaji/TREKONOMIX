import pandas as pd

df = pd.read_csv("dataset.csv")
df.drop(columns=["trip_id", "Unnamed: 0"], errors="ignore", inplace=True)

def get_recommendations(location, budget, max_results=5):
    filtered = df[
        (df['location'].str.lower() == location.lower()) &
        (df['total_budget_on_season_INR'] <= budget)
    ]
    if filtered.empty:
        return None
    sorted_df = filtered.sort_values(by="total_budget_on_season_INR")
    return sorted_df.head(max_results).to_dict(orient="records")

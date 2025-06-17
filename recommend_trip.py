import pandas as pd

# Load and clean the dataset
df = pd.read_csv("dataset.csv")
df.drop(columns=["trip_id", "Unnamed: 0"], errors="ignore", inplace=True)

def get_recommendations(location, days, budget, max_results=5):
    """
    Returns a list of trip recommendations based on the user input.
    
    Parameters:
        location (str): Desired destination entered by the user
        days (int): Number of days (currently not used for filtering as dataset lacks 'no_of_days')
        budget (float): Budget in INR
        max_results (int): Maximum number of recommendations to return
    
    Returns:
        list[dict] or None: Recommended trip rows as dictionaries or None if nothing found
    """

    # Filter based on destination and budget (either on-season or off-season)
    filtered = df[
        (df['location'].str.lower() == location.lower()) &
        (
            (df['total_budget_on_season_INR'] <= budget) |
            (df['total_budget_off_season_INR'] <= budget)
        )
    ]

    # Return top results if available
    if filtered.empty:
        return None

    sorted_df = filtered.sort_values(by="total_budget_on_season_INR")
    return sorted_df.head(max_results).to_dict(orient="records")

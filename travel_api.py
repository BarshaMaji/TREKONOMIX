def get_travel_tip(location):
    tips = {
        "Goa": "Avoid peak December rush unless you enjoy crowds.",
        "Darjeeling": "October is best for clear views and low humidity.",
        "Jaipur": "Winter is ideal for sightseeing and avoiding heat."
    }
    return tips.get(location, "Explore local food, culture, and hidden gems.")

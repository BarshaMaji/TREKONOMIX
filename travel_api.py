def get_travel_tip(location):
    tips = {
        "Darjeeling": "Don't miss the sunrise at Tiger Hill.",
        "Goa": "Avoid peak season for cheaper stays and empty beaches.",
        "Jaipur": "Visit early morning to skip crowds and heat.",
        "Manali": "Pack warm clothes—even in summer it gets chilly.",
    }
    return tips.get(location, "Pack light, stay curious, and enjoy your journey!")

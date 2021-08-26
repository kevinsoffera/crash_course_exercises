def get_formatted_city(city, country, population = ""):
    """Generate a formatted city, country pair"""
    if population:
        formatted_city = f"{city}, {country}, population - {population}"
    else:
        formatted_city = f"{city}, {country}"
    return formatted_city.title()
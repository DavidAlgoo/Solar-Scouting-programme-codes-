def categorize_vehicle(emissions):
    if emissions <= 100:
        return "Low"
    elif emissions <= 150:
        return "Moderate"
    else:
        return "High"

# Example usage:
vehicle_emissions = [100, 150, 200,]
for emissions in vehicle_emissions:
    category = categorize_vehicle(emissions)
    print(f"Vehicle with emissions {emissions} grams is categorized as: {category}")


def categorize_vehicle(emissions):
    if emissions <= 100:
        return "Low"
    elif emissions <= 150:
        return "Moderate"
    else:
        return "High"

# Determine the category for a vehicle emitting 180 grams
emissions = 180
category = categorize_vehicle(emissions)
print(f"Vehicle with emissions {emissions} grams is categorized as: {category}")

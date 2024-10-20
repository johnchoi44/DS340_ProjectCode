import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers (mean radius)
    R = 6371.0
    distance = R * c
    return distance

# Get user input for the coordinates of two places
lat1 = float(input("Enter the latitude of the first place: "))
lon1 = float(input("Enter the longitude of the first place: "))
lat2 = float(input("Enter the latitude of the second place: "))
lon2 = float(input("Enter the longitude of the second place: "))

# Calculate the distance
distance = haversine(lat1, lon1, lat2, lon2)

# Output the distance
print(f"The distance between the two places is: {distance:.2f} kilometers.")

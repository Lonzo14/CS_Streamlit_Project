def businesses_in_radius(user_coord, radius, business_type, dataset):
    nearby_businesses = []

    for entry in dataset:
        if entry['type'] == business_type:
            business_coord = (entry['latitude'], entry['longitude'])
            distance = haversine_distance(user_coord, business_coord)
            
            if distance <= radius:
                nearby_businesses.append({
                    'name': entry['name'],
                    'coordinates': business_coord,
                    'review': entry['review']
                })

    return nearby_businesses

# Example usage
data = [
    {'name': 'Restaurant A', 'review': 'Excellent', 'type': 'Restaurant', 'latitude': 40.7128, 'longitude': -74.0060},
    {'name': 'Cafe B', 'review': 'Very Good', 'type': 'Cafe', 'latitude': 40.7328, 'longitude': -74.0160},
    {'name': 'Retail C', 'review': 'Good', 'type': 'Retail', 'latitude': 40.7528, 'longitude': -74.0260},
    # ... add more business data ...
]

user_coordinates = (40.7128, -74.0060)  # Example user coordinates
radius_km = 5  # 5 km radius
business_type = 'Restaurant'  # User-selected business type

# Get businesses of a specific type within the radius
businesses = businesses_in_radius(user_coordinates, radius_km, business_type, data)
businesses

#Output stage

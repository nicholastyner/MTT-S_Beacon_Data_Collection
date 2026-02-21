import math

earth_radius = 6371000 # meters

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    lat_difference = lat2_rad - lat1_rad
    lon_difference = lon2_rad - lon1_rad
    
    hav_theta = haversine(lat_difference) + math.cos(lat1_rad) * math.cos(lat2_rad) * haversine(lon_difference)
    theta = 2 * math.asin(math.sqrt(hav_theta))
    
    distance = theta * earth_radius
    
    return distance
    
def haversine(theta):
    return (math.sin(theta/2.0)) ** 2
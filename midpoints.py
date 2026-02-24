import math
import numpy as np

def midpoints(lat_tx, lon_tx, lat_rx, lon_rx, distance, num):
    
    midpoints = []
    
    earth_radius = 6371000 # meters
    
    # convert to radians
    lat_tx_rad = math.radians(lat_tx)
    lon_tx_rad = math.radians(lon_tx)
    lat_rx_rad = math.radians(lat_rx)
    long_rx_rad = math.radians(lon_rx)
    
    angular_distance = distance / earth_radius
    
    fractions = np.linspace(0, 1, num)
    
    for f in fractions:
        a = math.sin((1-f) * angular_distance) / math.sin(angular_distance)
        b = math.sin(f * angular_distance) / math.sin(angular_distance)
        x = a * math.cos(lat_tx) * math.cos(lon_tx) + b * math.cos(lat_rx) * math.cos(lon_rx)
        y = a * math.cos(lat_tx) * math.sin(lon_tx) + b * math.cos(lat_rx) * math.sin(lon_rx)
        z = a * math.sin(lat_tx) + b * math.sin(lat_rx)
        lat = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
        lon = math.degrees(math.atan2(y, x))
        midpoints.append([lat, lon])
    
    return midpoints
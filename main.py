import haversine_formula
import midpoints
import sunrise_sunset

# A&M
latitude_tx = 30.6187
longitude_tx = -96.3364

# UT Dallas
latitude_rx = 32.9859
longitude_rx = -96.7503

# number of midpoints
count_midpoints = 3

# calculating the distance between the points Haversine formula
distance = haversine_formula.calculate_distance(latitude_tx, longitude_tx, latitude_rx, longitude_rx)

# midpoints
midpoints = midpoints.midpoints(latitude_tx, longitude_tx, latitude_rx, longitude_rx, count_midpoints)

# sunrise sunset API
sunrise, sunset = sunrise_sunset.sunrise_sunset(latitude_tx, longitude_tx)

print(sunrise, sunset)
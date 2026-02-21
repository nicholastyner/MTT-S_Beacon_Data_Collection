grid_square = "EM10tp"
grid_square = grid_square[:2].upper() + grid_square[2:4] + grid_square[4:].lower()

lat_1 = (ord(grid_square[1]) - 65) * 10 - 90
lon_1 = (ord(grid_square[0]) - 65) * 20 - 180

lat_2 = 0
lon_2 = 0

lat_3 = 0
lon_3 = 0

if (len(grid_square) >= 4):
    lat_2 = (int(grid_square[3]))
    lon_2 = (int(grid_square[2])) * 2
if (len(grid_square) == 6):
    lat_3 = (ord(grid_square[5]) - 97) / 24.0
    lon_3 = (ord(grid_square[4]) - 97) / 12.0

lat =  lat_1 + lat_2 + lat_3
lon =  lon_1 + lon_2 + lon_3

print(lat)
print(lon)
def csv_headers(weather_dict):
    with open("output.csv", "w") as file:
        for key in weather_dict.keys():
            file.write(f"{key},")
        file.write("\n")
    
def to_csv(weather_dict):
    with open("output.csv", "a") as file:
        for value in weather_dict.values():
            file.write(f"{value},")
        file.write("\n")
def csv_headers(weather_dict):
    with open("output.csv", "w") as file:
        for midpoint in weather_dict.keys():
            if midpoint == "general":
                for key in weather_dict[midpoint].keys():
                    file.write(f"{key}")
            else:
                for key in weather_dict[midpoint].keys():
                    file.write(f"Point {midpoint}: {key},")
        file.write("\n")
    
def to_csv(weather_dict):
    with open("output.csv", "a") as file:
        for point in weather_dict.values():
            for value in point.values():
                file.write(f"{value},")
        file.write("\n")
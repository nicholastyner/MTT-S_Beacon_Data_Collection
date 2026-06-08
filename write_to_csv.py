def csv_headers(weather_dict):
    headers = []
    for midpoint in weather_dict.keys():
            if midpoint == "general":
                for key in weather_dict[midpoint].keys():
                    headers.append(key)
            else:
                for key in weather_dict[midpoint].keys():
                    headers.append(f"Point {midpoint}: {key}")
        
    with open("output.csv", "w") as file:
        file.write(",".join(headers) + "\n")
        
    
def to_csv(weather_dict):
    data = []
    
    for point in weather_dict.values():
            for value in point.values():
                data.append(str(value))
    
    with open("output.csv", "a") as file:
        file.write(",".join(data) + "\n")
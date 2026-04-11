import grid_square

def get_input():
    
    # Get prefered user input method
    valid_input = False
    print("Select how to input tx and rx locations",
          "(\"lat lon\" or \"grid square\"): ", end="")
    while(not valid_input):
        input_selection = input()
        if(input_selection == "lat lon"):
            input_is_lat_lon = True
            valid_input = True
        elif(input_selection == "grid square"):
            input_is_lat_lon = False
            valid_input = True
        else:
            print("Invalid input. Please select either \"lat lon\" or \"grid square\": ", end="")
    
    # Latitude longitude input method
    if(input_is_lat_lon):
        # latitude tx
        valid_input = False
        print("Enter latitude of transmit station: ", end="")
        while(not valid_input):
            try:
                latitude_tx = input()
                valid_input = True
            except:
                print("Invalid input. Please enter latitude of transmit station: ", end="")
                
        # longitude tx
        valid_input = False
        print("Enter longitude of transmit station: ", end="")
        while(not valid_input):
            try:
                longitude_tx = input()
                valid_input = True
            except:
                print("Invalid input. Please enter longitude of transmit station: ", end="")
        
        # latitude rx
        valid_input = False
        print("Enter latitude of receive station: ", end="")
        while(not valid_input):
            try:
                latitude_rx = input()
                valid_input = True
            except:
                print("Invalid input. Please enter latitude of receive station: ", end="")
                
        # longitude rx
        valid_input = False
        print("Enter longitude of receive station: ", end="")
        while(not valid_input):
            try:
                longitude_rx = input()
                valid_input = True
            except:
                print("Invalid input. Please enter longitude of receive station: ", end="")
    else:
        tx_grid_square = input("Input the transmit grid square: ")
        valid_input = False
        while(not valid_input):
            try:
                latitude_tx, longitude_tx = grid_square.calculate_grid_square(tx_grid_square)
                valid_input = True
            except:
                input("Invalid input. Please input a 2, 4, or 6 grid square: ")
        
        
        rx_grid_square = input("Input the receive grid square: ")
        valid_input = False
        while(not valid_input):
            try:
                latitude_rx, longitude_rx = grid_square.calculate_grid_square(rx_grid_square)
                valid_input = True
            except:
                input("Invalid input. Please input a 2, 4, or 6 grid square: ")
    
    return (latitude_tx, longitude_tx, latitude_rx, longitude_rx)
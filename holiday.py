'''
Calculate the user's total holiday cost, 
which includes the plane cost, hotel cost 
and car rental cost.
'''
#Defining the functions for plane cost.

def plane_cost(city_flight):
    flight_cost = { "london" : 500, "paris" : 600, "rome" : 700 }
    for keys in flight_cost.keys():
        if keys == city_flight:
            y = flight_cost[keys]
            y = int(y)
            print ("------------------------------------------------")
            print("The plain fair is :£ ",y)
        
    return y

#Defining the functions for hotel cost.

def hotel_cost(num_nights):
    h_cost = {"hotel1" : 150 }
    x = (h_cost["hotel1"] * num_nights)
    x = int(x)
    print ("------------------------------------------------")
    print(f"The hotel cost for {rental_days} days is :£ {x} ")
    return x

#Defining the functions for car rental.

def car_rental(rental_days):
    car_cost = { "car1": 200 }
    car_rental = (car_cost["car1"] * rental_days)
    z= int(car_rental)
    print(f"The car rental cost for {rental_days} days is :£ {z} ")
    print ("------------------------------------------------")
    return z

#Defining the functions for total holiday cost.

def holiday_cost(x,y,z):
    holiday_cost = x+y+z
    print("The total holiday cost is :£ ", holiday_cost)
    print ("------------------------------------------------")
    return holiday_cost

# Defining the main body of the function asking user input data

while True:
    try:
        city_flight = str(input("Which city you wish to fly to? (london/paris/rome)")).lower()
        num_nights = int(input("How many days you wish to stay in a hotel (1 to 30 days)?"))
        rental_days = int (input("How many days you wish to hire a car (1 to 3o days)?"))
        
        holiday_cost(plane_cost(city_flight),hotel_cost(num_nights),car_rental(rental_days))
        break
    except:
        print("An exception occured. please enter correct data as instructed")
        
    


            
    
    
        









#Programming the cafe file
#Creating a list with atleast four menu
menu = ["veg1", "veg2", "veg3", "veg4"]

#Creating the dictionary  which contain the stock value for each item on the menu
stock = {'veg1': 11, 
         'veg2': 10, 
         'veg3': 14, 
         'veg4': 10 }

#Creating another dictionary for the price for each item on the menu
price = {'veg1': 9, 
         'veg2': 7, 
         'veg3': 9, 
         'veg4': 11 }

#Declaring the total stock worth to 0 initially
total_stock_worth = 0

# Now looping through the menu list to access the coresponding stock and price values
for item in menu:
    item_value = (stock[item] * price[item]) # multiply the stock value with price
    #print (item_value)
    total_stock_worth =  total_stock_worth + item_value


#Printing out the result of calculation
print("-----------------------------------------------")
print(f"The calculated total stock worth is : £{total_stock_worth}")
print("-----------------------------------------------")




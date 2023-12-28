# Decalaring the variable to count and total to calculate the average
# The sub total of each input and the counter number has been displayed on purpose for clariry.

total = 0
count = 0
print("---------------------------------------------------------------")
user_input = int(input("Please enter a number \n :" ))

while True:
      print("----------------------------------")
      count +=1
      print("And this is Counter no : ", count)

      total += user_input
      print( "And sub total so far is : ", total)

      print("---------------------------------------------------------------")
      average = total/count

      user_input = int(input("Please enter a number again or (***Enter -1 to exit) \n :" ))

      if user_input == -1 : # applying the break condition
            
            print("The final total is :" ,total)
            print("The final counter is" ,count)

            average = total/count # Calculating the average.

            print("---------------------------------------------------------------")
            print("So the the average of the number entered is : ", average)
            print("---------------------------------------------------------------")
            break
      
      
    


# while True:
#     print("My friend name is andrew")
#     name = input( "Please enter your friends name: ").lower()
#     if name == "mikie":
#         break
# print (f" loop is exited with with friend{name}")

# num = 0
# while num <= 5:
#     num = num +2
#     print(num)

# total = 0
# user_input = int(input("Please enter a number \n " ))
# while user_input != -1:
#     total += user_input
#     user_input = int(input("Please enter a number \n"))
#     if user_input == -1:
#         print(total)
#         break

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

      if user_input == -1 :
            
            print("The final total is :" ,total)
            print("The final counter is" ,count)
            average = total/count
            print("---------------------------------------------------------------")
            print("So the the average of the number entered is : ", average)
            print("---------------------------------------------------------------")
            break
    


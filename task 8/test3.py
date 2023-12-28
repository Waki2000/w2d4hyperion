# # Declaring the varaibles
# word = "coffeeeee"
# word_len = len(word)
# symbol = "*"

# # Using only one for loop to declare the range (0,9) using the length of the word coffee + 3 extra e
# for i in range (word_len):
#                                 #Declaring the for loop within half the range <4 and adding "*" to string for each turn
#     if i < 4 :
#         print(symbol)
#         symbol= symbol + "*"    # So far it will display half the horizonta star pyramid

#     else:
#         print(symbol)           # This will carry over the last data saved in symbol varaible
#         symbol = symbol[:-1]    # :-1 will reverse the symbol variable pattern and deduct one star in each turn

    

# #print(i)
# print("*"*(i-1))
#------------------------------
# star = "*"
# for i in range (1,10):
#     if i < 5:
#         print(star)
#         star = star + "*"
#         #print("--", star)
#     else:
#        print(star)
#        star = star[:-1]
#        print("~~", star)

# word = "coffee"
# for letter in range(0,6) :
#     for i in word:
#         print(i, letter, i)
#         print(letter, i, i)

# numbers = [13,23,33,43,53,63]
# for i in numbers :
#      print(i)
# for item in enumerate (numbers):
#     print(item, numbers)
#
# count = 0
# while count < 3:
#  print(count)
#  count +=1
#the last digit is excluded. error creation. print number to 
# for num in range(100,106):
#     print(num)
# for num in range(0,3):
#     print(num)
#     num=66
#     print(num)
# fruits = ["apple", "banana", "cherry", "manago", "orange", "tomato"
#           , "grapes", "clementines"]
# count = 0
# for pot, fruit in enumerate (fruits):
#     print(f"{pot} -- {fruit} is a fruit")
#     #count += 1

#Example 2
# while True:
#     guess = input("Enter your guess (between )")

#     if not guess.isdigit() or int(guess) <= 0 or int(guess) >=100:
#         print("Invalid numbr")
#         continue
#     else:
#         guess = int(guess)

# Example 3
# choice = ''
# while choice != '3':
#     print("Menu: \n"
#           "1. option 1 \n"
#           "2. Option 2 \n"
#           "3. Exit \n")
#     choice = input("Enter your choice:")
#     #perform option 1

#Example 4    
user_input = ''

while user_input.upper() not in ["STOP", "EXIT", "END"]:
    print ("Hello")
    user_input = input()

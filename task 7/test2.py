#for item in iterable object:ican write thing so quickly 
#can a while loop iterate over a string, I think it can but for loop is more efficient
# kitten =0
# question = input(" kitten world domination yes/no")

# while question =="yes":
#     kitten +=1

# numbers = [1,2,3,4,5]
# sum=0

# for item in numbers:
#     sum = sum + item

# print(sum)

# numbers = [1,2,3,4,5]
# sum=0
# index=0

# while index < len (numbers):
#     sum = sum + num
#     print(sum)
#===============================

# for i in range (1,10):
#     print(i)
#     i+=1

# print("dfdfd", i)
#-------------------------------

# while True:
#     print("Please pick an opton: \n1 - Deposit \n2 - withdrw \n3 - check balance \n4 - exit \n:")
#     user_input = int(input("Please pick an opton: \n1 - Deposit \n2 - withdrw \n3 - check balance \n4 - exit \n:"))
#     if user_input ==1:
#         pass
#     elif user_input ==2:
#         pass
#     elif user_input ==3:
#         pass
#     elif user_input ==4:
#         break
#     else:
#         print(" inncorect option enteredhh")
        #=====================================================
pass1 = "try123"
attempt = 0
max =3 

while attempt <=3 : 
    usrpass = input("Enter the password")
    if usrpass == pass1:
        print(" granted access")
        break
    else:
        print ("incorrect pass")

    attempt += 1
print("access denied for multiple try")


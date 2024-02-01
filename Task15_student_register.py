# Write a program that allows a user to register students for an exam venue

with open ("reg_form.txt", "r+") as file:                                       # Open the file for reading and writing
    file.seek(0)                                                                # pointing the cursor at the begining
    file.write("Student ID " + "      " + "Student Signature \n\n")
    number_of_student = int(input ("how many students are registering?"))       # Asking How many student are registering?
file.close()                                                                    # Closing the file

file = open ("reg_form.txt", "a+")                                              # Reopening the file in appending mode

for students in range (0, number_of_student):                                   # Running Loop to enter the next student ID number
    id_number = int(input ("Enter the next student id number please \n"))
    file.write(f" {id_number}             .....................\n ")            # Appending each ID to the file just created
    file.write(f"\n")
file.close()
# part A : Program that reads in a string and makes each alternate "charecter" into an upper case and lower case

string = 'I am learning to code' # Declaring the example string
final_string = ""       # Declaring the final string for the required output

    # Declaring the for loop to count the lenth of the string and then idexing it into odd and even using modulus
    # By Indexing those divided by 2 = 0 will convert to uppercase, (otherwise will convert to lower case).

for i in range (len(string)):
    if i % 2  == 0:
        final_string += string[i].upper()   
    else:
        final_string += string[i].lower()
        
print(f" \n 'I am learning to code' all Charecters now becomes : ' {final_string} ' as instructed. \n") # Final output displaying the alternate characters

#----------------------------------------------------------------------------------------------------------------------------------
# part B : With the same string make each alternative "word" lower and upper case

string2 = string.split()    # Converting the string into a list of words : ie: ['I', 'am', 'learning', 'to', 'code']
string3 = ""                # Declaring eampty string3 to store the values for the final output  

for i in range(len(string2)): # Instead of each charectar it will count the words as each index and for this case length is (0,5)

    if i % 2 == 1:
        string3 += string2[i].upper()
        string3 += " "                      # adding space each time between each converted words
    else:
        string3 += string2[i].lower()
        string3 += " "
       
print(f" 'I am learning to code' all 'WORDS' now becomes :::: ' {string3}' as instructed.\n") # Final output displaying the alternate characters
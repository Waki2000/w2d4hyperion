# Declaring the varaibles
word = "coffeeeee"
word_len = len(word)
symbol = "*"

# Using only one for loop to declare the range (0,9) using the length of the word coffee + 3 extra e
for i in range (word_len):
                                #Declaring the for loop within half the range <4 and adding "*" to string for each turn
    if i < 4 :
        print(symbol)
        symbol= symbol + "*"    # So far it will display half the horizonta star pyramid

    else:
        print(symbol)           # This will carry over the last data saved in symbol varaible
        symbol = symbol[:-1]    # :-1 will reverse the symbol variable pattern and deduct one star in each turn
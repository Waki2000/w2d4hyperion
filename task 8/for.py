# word = "coffee"
# for billy in word:
#     print(billy)
#     print(word)
# valu =10
# for x in range(0, valu+1, 3):
#     print(x)
word = "coffee"
wordlen1 = len(word)
final_word = ""
final_word = (word[::-1])
wordlen2 = len(final_word)

print(word)
print(final_word)
for x in range(wordlen2): #word len is 
    print("*"*x)
    print(x)
    
    #print (final_word)
    if x % 2 == 0:
        final_word += word[x]
        #print(word[x])
       # print("---", final_word)
    else:
        final_word += word[x]
        #print(final_word)
#print(" final word", final_word)

#num = "*"
# for i in range(1,7):
#     if i==1:
#         print(num)
#     elif i == 2:
#         print(num*2)
#     elif i == 3:
#         print(num*3)
#     elif i == 4:
#         print(num*4)
#     elif i == 5:
#         print(num*5)
#     else:
#         num = num - 1
#         print(num)

# for i in range (1,6):
#     if i >= 0 and i <=5:
#         print("*"*i)

# for i in range (-5,0):
#     print(i)
#     print("*"*i)
       
     
    
    

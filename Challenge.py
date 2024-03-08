# function 1 : adding prefix

def add_prefix_un(word):
    word = "un" + word      #adding the prefix to the word
    print(word)

add_prefix_un("manageable")

# Add prefixed to word groups

def make_words_group (prefix,word1,word2,word3):
    prefix = prefix
    word1 = prefix+word1
    word2 = prefix+word2
    word3 = prefix+word3
    print(prefix,word1,word2,word3)

make_words_group("pre", "dog", "cat", "fat")

# Remove a suffix from a word

def remove_suffix_ness (word):
    word = word[:-4] # Removing the last 4 character from the word
    print(word)

remove_suffix_ness("Happyness")

# Extract and Transform a word

def adjective_to_verb(sentence, index):
    sentence = sentence.split()         #spliting the word into a list to be called by index
    sentence = sentence[index]+"en"     # calling the specific word by index and adding string
    print(sentence)

adjective_to_verb("I need to make tha bright", -1)
adjective_to_verb('It got dark as the sun set',2)
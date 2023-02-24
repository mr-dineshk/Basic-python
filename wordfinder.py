print("\n***Word Finder***\n")
sen = input("Enter the sentence: ")
word = input("Enter the word: ")

def search(a, b): #function
    if b in a:
        return("Word found !")
    else:
        return("Word not found !")

print(search(sen, word)) #call function

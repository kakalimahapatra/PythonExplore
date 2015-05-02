# Name - Kakali Mahapatra
#Exploring String in Python

def main():
    
    # 1. Ask user to enter a phrase
    phrase = input("Enter a phrase: ")
    print("The pharse entered by the user is: " +phrase)

    # 2.Print the phrase as a Title
    titlephrase = phrase.title()
    print("The phrase as a title is: ")
    print(titlephrase)

    # 3.Change all the spaces in the original phrase to '-' and display
    x = phrase.replace (" ", "_")
    print("The phrase when the spaces replaced by _ becomes: ")
    print(x)


    # 4.split the original phrase in to list and display
    a = phrase.split()
    print("Splititng the phrase into list: ")
    print(a)

    # 5.Create a new phrase that contains the words in the original phrase in reverse order and display
    b = a[::-1]
    c = " ".join(b)
    print("Displaying the reverse order of the phrase: ")
    print(c)

main()


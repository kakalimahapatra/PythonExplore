    # Name - Kakali Mahapatra
    # letters, digits and space calculation program



def main():

    inputString = input("Enter an input string: ")
    inputStringTuple = [str(ch)for ch in str(inputString)]

    noOfIntegers = 0
    noOfUpperCase = 0
    noOfLowerCase = 0
    noOfWhiteSpace = 0

    for ch in inputStringTuple :
        if ch.isdigit():
            noOfIntegers = noOfIntegers+1
        elif ch.islower():
            noOfLowerCase = noOfLowerCase+1
        elif ch.isupper():
            noOfUpperCase = noOfUpperCase+1
        elif ch.isspace():
            noOfWhiteSpace = noOfWhiteSpace+1

    print("The sting contains" + str(noOfIntegers) + " digits, " + str(noOfUpperCase) + " upper-case letters, " + str(noOfLowerCase) + " lower-case letters, and " + str(noOfWhiteSpace) + " space characters")

if __name__ == "__main__":
    main()

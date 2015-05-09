    # Name - Kakali Mahapatra
    # Program to calculate leap year

def main():

    inputString = input("Enter a year: ")
    inputYear = int(inputString)

    if inputYear%4 == 0:
        print ("This is a leap year")
    else:
        print ("This is not a leap year")

#if __name__ == "__main__":
main()

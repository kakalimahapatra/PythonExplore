    # Name - Kakali Mahapatra
    # Student ID - 84803
    # Credit Card validation program



class CreditCardValidation:

    # Global variables
    creditCardTuple = []
    sumOfEvenPosition = 0
    sumOfOddPosition = 0
    digitSum = 0
    cardNumber = ""
    cardType = ""


    def enterCreditCardNumber(self):

        CreditCardValidation.cardNumber = input("Enter your card number: ")
        CreditCardValidation.creditCardTuple = [int(ch)for ch in str(CreditCardValidation.cardNumber)][::-1]

        lengthOfCard = CreditCardValidation.creditCardTuple.__len__()


        # Check for card type
        firstDigit = CreditCardValidation.creditCardTuple[lengthOfCard-1]
        secondDigit = CreditCardValidation.creditCardTuple[lengthOfCard-2]

        if(firstDigit==4):
            CreditCardValidation.cardType = "Visa"
        elif(firstDigit==5):
            CreditCardValidation.cardType = "MasterCard"
        elif(firstDigit==6):
            CreditCardValidation.cardType = "Discover"
        elif(firstDigit==3 and secondDigit==7):
            CreditCardValidation.cardType = "American Express"
        else:
            print("This is an invalid card number")
            exit()

        # Check for valid length which should be between 13 and 16
        if(lengthOfCard < 13 or lengthOfCard > 16):
            print("This is an invalid card number")
            exit()

        
    def sumOfEvenPosition(self):
        CreditCardValidation.sumOfEvenPosition = sum(sum(divmod(d*2, 10))for d in CreditCardValidation.creditCardTuple[1::2])

    def getDigitSum(self):
        CreditCardValidation.digitSum = CreditCardValidation.sumOfEvenPosition + CreditCardValidation.sumOfOddPosition

    def sumOfOddPosition(self):
        CreditCardValidation.sumOfOddPosition = sum(CreditCardValidation.creditCardTuple[0::2])

    def isValid(self):

        if CreditCardValidation.digitSum % 10 == 0:
            print("This is a good " + str(CreditCardValidation.cardType) + " card number")
        else:
            print("This is an invalid " + str(CreditCardValidation.cardType) + " card number")
        
   
def main():

    cc = CreditCardValidation()
    cc.enterCreditCardNumber()
    cc.sumOfEvenPosition()
    cc.sumOfOddPosition()
    cc.getDigitSum()
    cc.isValid()

main()
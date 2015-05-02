    # Name - Kakali Mahapatra
    # Student ID - 84803
    # Credit Card validation program



class CreditCardValidation:

    def __init__(self):
        self.cardNumber=""
        print ("Constructor")
        
    def enterCreditCardNumber():
        print ("Inside credit card enter")
        self.cardNumber = input("Enter your crd number: ")
        r = [int(ch)for ch in str(cardNumber)][::-1]
        
    def sumOfEvenPosition():
        sumOfEvenPosition = sum(sum(divmod(d*2, 10))for d in r[1::2])
        return sumOfEvenPosition

    def getDigitSum():
        digitSum = sumOfEvenPosition + sumOfOddPosition
        return digitSum

    def sumOfOddPosition():
        sumOfOddPosition = sum(r[0::2])
        return sumOfOddPosition

    def isValid():

        if digitSum % 10 == 0:
            print("The card" + cardNumber + "valid")
        else:
            print("The card" + cardNumber + "invalid")
        
   
   # def main():

cc = CreditCardValidation()
cc.enterCreditCardNumber()
cc.sumOfEvenPosition()
cc.sumOfOddPosition()
cc.getDigitSum()
cc.isValid()
    #main()
        

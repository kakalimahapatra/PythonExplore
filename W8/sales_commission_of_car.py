    # Name - Kakali Mahapatra
    # Program to calculate sales commission for cars


def main():

    print ("This program computes car sale commission for Acme Auto")

    carSalePrice = input("Enter car sale price: ")
    if float(carSalePrice) <= 0 or float(carSalePrice) > 300000.00 :
        print ("Invalid car sale price. It must be greater than 0 and cannot exceed 300000.00")
        exit(0)


    carAge = input("Enter 'N' for New or 'U' for Used car:  ")
    if carAge!="N" and carAge!="U":
        print ("Invalid code for car type. It must be 'N' or 'U'.")
        exit(0)


    carType = input("Enter 'E' for Economy or 'L' for Luxury car:  ")
    if carType!="E" and carType!="L":
        print ("Invalid code for car class. It must be  'E' or 'L'.")
        exit(0)


    salesExperience = eval(input("Enter salesperson years of employment:  "))
    if salesExperience < 0:
        print ("Invalid sales years, must be greater than or equal to 0")
        exit(0)


    # Calculate base commission

    baseCommission = 0
    if carAge=="N" and carType=="E" :
        baseCommission = float(carSalePrice)*2.8/100
    elif carAge=="N" and carType=="L" :
        baseCommission = float(carSalePrice)*3.4/100
    elif carAge=="U" and carType=="E" :
        baseCommission = float(carSalePrice)*3.2/100
    elif carAge=="U" and carType=="L" :
        baseCommission = float(carSalePrice)*3.5/100


    # Add years of experience commission
    baseCommissionFormated = float("{0:.2f}".format(baseCommission))
    finalCommission = 0

    if salesExperience >= 4 and salesExperience <= 8 :
        finalCommission = baseCommissionFormated + 150.00
    elif salesExperience >= 9 and salesExperience <= 16 :
        finalCommission = baseCommissionFormated + 280.00
    elif salesExperience >= 17:
        finalCommission = baseCommissionFormated + 350.00
    else:
        finalCommission = baseCommissionFormated

    print("The sale commission is : $" + str(finalCommission))


if __name__ == "__main__":
    main()

# Chapter #6-Assignment #5
# Programmer: Denise Tranberg
# Date: 10/3/2017
#
# Program Title: 4 programs using functions.
#
# 1) Write a function that takes 5 int arguments and returns the largest of the 5.
# 2) Write a Python program to perform the task of temperature conversion from Celsius to Fahrenheit.
#   Note that given C as the degree of temperature in Celsius, the corresponding degree F in Fahrenheit equals 1.8*C + 32.0.
#   For example 50 degree Celsius should be 122 degree Fahrenheit.
# 3) Continually prompt the user for an integer.  Constrain the user’s input to integers between 1 and 50,000.
#   You can assume that the user will enter an integer and not a string or floating point number.
#   Make sure you have a way of exiting the function.
# 4) Write a function that calculates that computes the balance of a bank account with a given initial balance and interest rate,
#   after a given number of years. Assume interest is compounded yearly.

################################################################################################
#
################################################################################################



def main():

    def Largest():  # This function compares 5 numbers entered, and prints out the largest of them.
        num = 0
        for lane in range(5):
            entry = int(input("Please enter an interger:"))
            if entry > num:
                num = entry
        print ("The largest number entered was: ",num)
    Largest()

    def CelFarConversion(): # This function converts an input in Celcius to Farenheit

        temp=float(input("\n\n\nPlease enter a temperature in Celcius (C): "))
        farht=(temp*1.8)+32.0
        print ("When given temperature of ",temp,"in Celcuius, the temperature in Farenheit is: ",farht)
        print (temp,"C =",farht,"F")
    CelFarConversion()

    def PickANumber(): # this function allows you to enter intergers between 1-50,000, until you want to quit.
        quit='no'
        while quit!='yes':
            number=int(input("\n\n\nPlease enter a whole number between 1 and 50,000"))
            if number<1 or number>50000:
                print ("That number is outside the range of 1-50,000")
            else:
                quit=input("Would you like to quit? (yes/no)")

    PickANumber()


    def BankBalance(): # This function calculates the ending bank balance given beginning balance, # years saved & interest rate.
        beginningBalance=float(input("\n\n\nPlease enter your starting balance:"))
        interestRate=float(input("Please enter your interest rate in decimal format (i.e. 2%=.02):"))
        numYears=int(input("Please enter how many years: "))
        movingBalance=beginningBalance
        for compound in range(numYears):
            movingBalance=movingBalance+(movingBalance*interestRate)
        print ("\n\nBeginning Balance:  $",beginningBalance)
        print ("Interest rate of:  ",(interestRate*100),"%")
        print ("The number of years saved is:  ",numYears)
        print ("The final balance of the account is   $",round(movingBalance,2))

    BankBalance()


main()
# Topic 4 - Assignment#3_P3.23
# Programmer: Denise Tranberg
# Version: 1
# Date: 9/11/17
#
# •• P3.23 The original U.S. income tax of 1913 was quite simple.
# The tax was
# • 1 percent on the first $50,000.
# • 2 percent on the amount over $50,000 up to $75,000.
# • 3 percent on the amount over $75,000 up to $100,000.
# • 4 percent on the amount over $100,000 up to $250,000.
# • 5 percent on the amount over $250,000 up to $500,000.
# • 6 percent on the amount over $500,000.
# There was no separate schedule for single or married taxpayers.
#
#Write a program that computes the income tax according to this schedule.

# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 154). Wiley. Kindle Edition.
#
##############################################################################################
##                                  Declare/Initialize
###############################################################################################
levelOne=.01  # up to 49,999
levelTwo=.02  # 50,000 to 74,999
levelThree=.03  # 75,000 to 99,999
levelFour=.04  # 100,000 to 249,999
levelFive=.05  # 250,000 to 499,999
levelSix=.06  # 500,000 and over

##############################################################################################
##                                    INPUT
###############################################################################################

annualIncome=int(input("Please enter your annual income:"))
print ("\nThank you! Your annual income is ",annualIncome)
##############################################################################################
#
#                                  Calculate & Print
#
##############################################################################################
def Tax_Expence_Calculator():
    runningTaxable = 0
    runningTax = 0
    if annualIncome>=500000:
        overFiveHundred=annualIncome-499999
        levelSixTax=(overFiveHundred*levelSix)
        runningTax=runningTax+levelSixTax
        runningTaxable=499999
        #print ("Level6tax:",levelSixTax,"runningTaxable",runningTaxable)
    if runningTaxable>=250000:
        levelFiveTax=((runningTaxable-250000)*levelFive)
        runningTax=runningTax+levelFiveTax
        runningTaxable=249999
        #print ("Level5tax:",levelFiveTax,"runningTaxable",runningTaxable)
    if runningTaxable>=100000:
        levelFourTax=((runningTaxable-100000)*levelFour)
        runningTax=runningTax+levelFourTax
        runningTaxable=99999
        #print ("Level4Tax:",levelFourTax,"runningTaxable",runningTaxable)
    if runningTaxable>=75000:
        levelThreeTax=((runningTaxable-75000)*levelThree)
        runningTax=runningTax+levelThreeTax
        runningTaxable=74999
        #print ("Level3Tax:",levelThreeTax,"runningTaxable",runningTaxable)
    if runningTaxable>=50000:
        levelTwoTax=((runningTaxable-50000)*levelTwo)
        runningTax=runningTax+levelTwoTax
        runningTaxable=49999
        #print ("Level2Tax:",levelTwoTax,"runningTaxable",runningTaxable)
    if runningTaxable==49999:
        levelOneTax=((runningTaxable)*levelOne)
        runningTax=runningTax+levelOneTax
        #print ("Level1Tax-calculated",levelOneTax,"runningTaxable",runningTaxable)
    else:
        levelOneTax=annualIncome*levelOne
        runningTax=levelOneTax
        #print ("Level1Tax-only",levelOneTax)

    print ("\nTotal Tax bill   $",round(runningTax,2))

Tax_Expence_Calculator()


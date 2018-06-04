# Topic 3
# Assignment#2-P2.6
# Programmer: Denise Tranberg
# Date:09/08/2017
# Version:1.0
#
######################################################################
# 				Program Description
######################################################################
# •• P2.6 Write a program that prompts the user for a measurement in meters
#     and then converts it to miles, feet, and inches.
#
# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 81). Wiley. Kindle Edition.
######################################################################
#                        Variable List and Initialization
######################################################################

meterInches=39.3700787
meterFeet=3.2808399
meterMiles=0.00062137119

######################################################################
#                      Calculate and Print the Answer
######################################################################


numMeters=input ("Please enter the number of meters that you would like converted to inches, feet and miles:")
numMeters=float(numMeters)

numInches=(numMeters*meterInches)
numFeet=(numMeters*meterFeet)
numMiles=(numMeters*meterMiles)

print ("\nThe number of meters you have entered is:",numMeters,"\n")
print (numMeters,"meters =",numInches,"inches")
print (numMeters,"meters =",numFeet,"feet")
print (numMeters,"meters =",numMiles,"miles")



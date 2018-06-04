# Topic 4 - Convert measurements
# Programmer: Denise Tranberg
# Version: 1
# Date: September 12, 2017#
#
# ••• P3.26 Unit conversion. Write a unit conversion program that asks the users
# from which unit they want to convert (fl. oz, gal, oz, lb, in, ft, mi) and
# to which unit they want to convert (ml, l, g, kg, mm, cm, m, km).
# Reject incompatible conversions (such as gal → km). Ask for the value to be converted,
# then display the result: Convert from? gal Convert to? ml Value? 2.5 2.5 gal = 9463.5 ml
#
# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 155). Wiley. Kindle Edition.


##############################################################################################
#
#                                  Declare/Initialize
#
##############################################################################################

oneFlOunce=29.5735      # ml
oneGal=3.78541          # Liter
oneOunce=38.3495        # grams
onePound=.453592        # Kg
oneInch=25.4            # mm
oneFoot=.3048           # meter

##############################################################################################
#
#                                  Input
#
##############################################################################################

print ("""What units of measurement would you like to compare?

fluid ounce (floz)  to  Milliliter (ml)
gallon      (gal)   to  Liter (lit)
ounce       (oz)    to  grams (g)
pound       (lb)    to  Kilogram (kg)
inch        (in)    to  millimeter (mm)
foot        (ft)    to  meter (m)
""")
def Generate_Input():
    global convertFrom
    global convertTo
    global convertNum
    convertFrom=input("Please enter the abbreviation(xxx) of the unit you would like to convert from: ").lower()
    convertNum=float(input("Please enter how many to convert"))
    convertTo=input("Please enter the abbreviation (xxx) of the unit you would like to convert to: ").lower()

Generate_Input()

if convertFrom=="floz" and convertTo!="ml":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()
if convertFrom=="gal" and convertTo!="lit":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()
if convertFrom=="oz" and convertTo!="g":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()
if convertFrom=="lb" and convertTo!="kg":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()
if convertFrom=="in" and convertTo!="mm":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()
if convertFrom=="ft" and convertTo!="m":
    print ("\nYou must compare like measurements, please try again!\n")
    Generate_Input()

##############################################################################################
#
#                                  Computations
#
##############################################################################################

if convertFrom=="floz":
   answer=oneFlOunce*convertNum
if convertFrom=="gal":
    answer=oneGal*convertNum
if convertFrom=="oz":
    answer=oneOunce*convertNum
if convertFrom=="lb":
    answer=onePound*convertNum
if convertFrom=="in":
    answer=oneInch*convertNum
if convertFrom=="ft":
    answer=oneFoot*convertNum

##############################################################################################
#
#                                  Output
#
##############################################################################################

print ("\nYou have chosen to convert ",convertNum,convertFrom,"to ",answer,convertTo)


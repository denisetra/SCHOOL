# Topic 3
# Assignment#2-P2.7
# Programmer: Denise Tranberg
# Date:09/08/2017
# Version:1.0
#
######################################################################
# 				Program Description
######################################################################
# • P2.7 Write a program that prompts the user for a radius and then prints •
# The area and circumference of a circle with that radius •
# The volume and surface area of a sphere with that radius
#
# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 81). Wiley. Kindle Edition.
##area=pi*r**2
##circumference=pi*diameter
##circumference=2*pi*radius
##pi=3.14159265358979323846
######################################################################
#                        Variable List and Initialization
######################################################################

PI=3.14159265358979323846


######################################################################
#                      Calculate and Print the Answer
######################################################################

circleRadius=input("Plese enter the radius of a circle")
circleRadius=float(circleRadius)

circumCircle=PI*(circleRadius*2)
areaCircle=PI*(circleRadius**2)

print ("\nThe radius that you entered was:",circleRadius,"\n")
print ("The circumference of the circle, given a radius of",circleRadius,"is",circumCircle)
print ("The area of a circle, given a radius of",circleRadius,"is",areaCircle)



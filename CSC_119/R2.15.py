import math

num=23456

lastNumber=num%10
firstNumber=num//10**(int(math.log(num,10)))
stNum=[]
##First method relies on math to figure out the first and last.
print ("\n\nThe starting number is: ",num,"\n")
print ("The first character in the number is: ",firstNumber)
print ("The last character in the number is: ",lastNumber)

##Following method converts the int into a string, and then prints based on the position of the character in the string.
stNum=str(num)
print ("******ALTERNATE METHOD******")
print ("The first character in the number is: ",stNum[0])
print ("The last character in the number is: ",stNum[-1])



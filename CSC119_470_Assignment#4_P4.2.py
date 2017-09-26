# Chapter #4 - P4.2-Manipulate integers
# Programmer: Denise Tranberg
# Date: 9/18/2017
Version: 1.2
#
# Program Title: Manipulate Integers
#
#  •• P4.2 Write programs that read a sequence of integer inputs and print
#  a. The smallest and largest of the inputs. b. The number of even and odd inputs.
#  c. Cumulative totals. For example, if the input is 1 7 2 9, the program should print 1 8 10 19.
#  d. All adjacent duplicates.
#
#  For example, if the input is 1 3 3 4 5 5 6 6 6 2, the program should print 3 5 6.
#
# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 230). Wiley. Kindle Edition.

#######################################################################################################
#                                define variables
#######################################################################################################

numList=[]
highNum=0
lowNum=100000000000000000
cumNum=0
cumList=[]
dupList=[]
oddList=[]
evenList=[]
tempNum=0
#######################################################################################################
#                                body of program
#######################################################################################################

numInts=int(input("Please enter the number of intergers that you would like on your list:"))

for entries in range(numInts):
    char=int(input("Please enter a positive whole number: "))
    numList.append(char)
for entry in numList:
    if entry>highNum: #checking for highest number in list
        highNum=entry
    if entry<lowNum: #checking for lowest number in list
        lowNum=entry
    cumNum=cumNum+entry
    cumList.append(cumNum) #making a cumulative list
    if entry==tempNum:
        dupList.append(entry) #checking for adjacent duplicates
    tempNum=entry
    if entry%2==0:
        evenList.append(entry)
    if entry%2==1:
        oddList.append(entry)

########################################################################################################
#                                  Output
########################################################################################################

print ("\nThe highest number in the list is: ",highNum)
print ("The lowest number in the list is: ",lowNum)
print ("The cumulative totals list is here: ",cumList)
print ("The list of adjacent duplicates is: ",set(dupList))
print ("The count of odd numbers in list is: ",len(oddList))
print ("The count of even numbers in list is: ",len(evenList))


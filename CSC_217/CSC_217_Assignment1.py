
# Grading Averages
# Programmer: Denise Tranberg
# Date Created:  6/6/2018
# Date of Final Update:
#
######################################################################################

# Write a program that will ask the user to input 5 test grades and input into a list.
# Values must be between 0 and 100
# Program will compute the average of the point value.
# Program will ask user for name.
#
# define the following functions
##Following need to be included:
# math, variables, if statements, nexted if, loops (for/while), strings, tupples, lists/dictionaries
# files/exceptions, input, looping, branching, min, mzx and average.

#####################################################################################
#
#                                   Declaring Variables
#
#*************************************************************************************

global listGrades           # make the list available both in and out of a function
listGrades=[]               # As user provides grades, input into listGrades
numGrades=5                 # Total number of grades to be entered.
letNumGrades={}             # Create dictionary
lisNumGrades=[]             # Create list to keep the grades in
stats=()                    # Create a tupple to keep name/color

######################################################################################
#
#                       Main Program and Explanation
#
######################################################################################

def whileReady():           # Function to illustrate while loop
    answer='n'
    temp='n'
    while answer=='n':
        if temp=='y':
            break
        temp=input('Are you ready to do some math? (y/n): ')
        if temp=='n':
            whileReady()

whileReady()

def useLessTupple():        #  Function to illustrate tupples
    global stats
    name=str(input("What is your name?: "))
    color=str(input("What is your favorite color?: "))
    stats=(name,color)
useLessTupple()

def InputGrade():           #  Function to take the user input of grades

    try:                    #  Introducing exceptions on value of entry
        grade=int(input('Please enter your first grade as an  integer between 0 an 100: '))
        if grade <0 or 100<grade:
            raise ValueError

    except ValueError:
        print ('Please enter a whole number between 0 and 100')

    if 0 <= grade <= 100:           #  If value entered in range, add to list
        listGrades.append(grade)
    if 0>grade or grade>100:        # If value entered is not in range, return to input prompt
        InputGrade()

for imput in range(numGrades):      # Iterate using range to get 5 ints.
    InputGrade()

lowestNumber=min(listGrades)                        # Find smallest entry in list
highestNumber=max(listGrades)                       # Find largest entry in list
adverageNumber=(sum(listGrades)/len(listGrades))    # Calculate average of grades


def LetterGrades2():                # Set up nested loop to categorize number to letter grade.
    for num in listGrades:
        if num>=92:
            numLet='A'
        elif num>=84:
            numLet='B'

        elif num>=73:
            numLet='C'

        elif num>=65:
            numLet='D'

        else:
            numLet='F'

        ttlGrade=[numLet,num]
        lisNumGrades.append(ttlGrade)       # append list with letter/number asociation

LetterGrades2()

def LetterDictionary():             # Created dictionary that associates number to letter.
    for item in lisNumGrades:
        letNumGrades.update({item[1]:item[0]})
LetterDictionary()

print ('\n\n',stats[0],', Thank you for using us today.  ')
print (stats[1],' is the most AMAZING color on the face of the planet!')
print ('\nThe lowest grade that you earned was: ',lowestNumber)
print ('\nThe highest grade that you earned was: ',highestNumber)
print ('\nYour average score was: ',adverageNumber)

print ('Here is your list of grades: ')
for entry in lisNumGrades:
    print (entry)

#print ('\nHere is a list of your scores: ', lisNumGrades)

def CreateOutputFile():
    file=open('Outputfile.txt','w+')
    name=stats[0]
    color=str(stats[1])
    file.write('Hello ')
    file.write(name)

    file.write ('\nYour favorite color is: ')
    file.write(color)

    file.write('\n\nYour grades are as follows: ')
    for entry in lisNumGrades:
        file.write (str(entry))

    numbers=(str(lowestNumber)+'/'+str(highestNumber)+'/'+str(adverageNumber))
    file.write('\n\n(minimum/maximum/average)   ')
    file.write(numbers)
    # file.write(str(lowestNumber))
    # file.write ('/')
    # file.write (str(highestNumber))
    # file.write ('/')
    # file.write (str(adverageNumber))
    file.write('\n\nThank you and have a wonderful day')
    file.close()


CreateOutputFile()






######################################################################################
# End of Program - What does this do?
#
#####################################################################################


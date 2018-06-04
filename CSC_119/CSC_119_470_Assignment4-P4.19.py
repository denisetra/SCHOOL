# Chapter #4 - 4.19-Compute average grades
# Programmer: Denise Tranberg
# Date: 09/20/2017
#
# Program Title: Compute average grade
#
# Explaination:

# Problem Statement
# Write a program that can be used to compute the average exam grade for multiple students.
# Each student has the same number of exam grades.
#
# ********************** P4.19 ***************************************************************
# Modify the examaverages.py program from Worked Example 4.1
# so it will also compute the overall average exam grade.
#*********************************************************************************************

# Horstmann, Cay S.; Necaise, Rance D.. Python for Everyone,
#     2nd Edition (Page 233). Wiley. Kindle Edition.

################################################################################################
#                               variables
################################################################################################

compListGrades=[]
compGradeScore=0
moreGrades = "Y" # Initialize moreGrades to a non-sentinel value.

################################################################################################
#
################################################################################################


#ch04 / worked_example_1 / examaverages.py
#This program computes the average exam grade for multiple students.

# Obtain the number of exam grades per student.
numExams = int(input("How many exam grades does each student have?"))

# Compute average exam grades until the user wants to stop.
while moreGrades == "Y":

    # Compute the average grade for one student.
    print("Enter the exam grades.")
    total = 0

    for i in range(1, numExams + 1):
        score = int(input("Exam %d: " % i))  # Prompt for each exam grade.
        total = total + score
        compListGrades.append(score)
        compGradeScore=compGradeScore+score

    average = total / numExams
    print("The average is %.2f" % average)

    # Prompt as to whether the user wants to enter grades for another student.
    moreGrades = input("Enter exam grades for another student (Y/N)?")
    moreGrades = moreGrades.upper()

compScoresNum=len(compListGrades)
avgGrade=round(compGradeScore/compScoresNum,2)

print ("\nThe average grade for all students is: ",avgGrade)



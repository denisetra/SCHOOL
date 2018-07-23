#!/bin/bash
#========================================================
# Script Name: phoneadd
# By: Your initials here
# Date: Today’s date
# Purpose: A shell script that sets up a loop to add
# new employees to the corp_phones file.
# Command Line: phoneadd
#
#========================================================
trap "rm ~/tmp/* 2> /dev/null; exit"0123
phonefile=~/source/corp_phones
looptest=y
while test "$looptest" = "y"
do
	clear
	tput cup 1 4; echo "Corporate Phone List Additions"
	tput cup 2 4; echo "=============================="
	tput cup 4 4; echo "Phone Number: "
	tput cup 5 4; echo "Last Name :"
	tput cup 6 4; echo "First Name :"
	tput cup 7 4; echo "Middle Init :"
	tput cup 8 4; echo "Dept# :"
	tput cup 9 4; echo "Job Title :"
	tput cup 10 4; echo "Date Hired :"
	tput cup 12 4; echo "Add Another? (y)es or (q)uit: "
	tput cup 4 18; read phonenum
	if test $phonenum = "q"
	then
		clear ; exit
	fi

	# Check to see if the phone number already exists
	while grep "$phonenum" $phonefile > ~/tmp/temp
	do
		tput cup 19 1 ; echo "This number has already
		been assigned to: "
		tput cup 20 1 ; tr ':' ' ' < ~/tmp/temp
		tput cup 21 1 ; echo "Press ENTER to
		continue... "
		read prompt
		tput cup 4 18 ; echo " "
		tput cup 4 18 ; read phonenum
		if test $phonenum = "q"
		then
		clear ; exit
		fi
	done
	tput cup 5 18 ; read lname

	while test "$lname" = "-"
	do
		tput cup 4 18 ; echo " "
		tput cup 4 18 ; read phonenum
		if test "$phonenum" = "q"
		then
			clear ; exit
		fi
		tput cup 5 18 ; read lname
	done
	tput cup 6 18 ; read fname
	while test "$fname" = "-"
	do
		tput cup 5 18 ; echo " "
		tput cup 5 18 ; read lname
		if test "$lname" = "q"
		then
			clear ; exit
		fi
		tput cup 6 18 ; read fname
	done
	tput cup 7 18 ; read midinit
	while test "$midinit" = "-"
	do
		tput cup 6 18 ; echo " "
		tput cup 6 18 ; read fname
		if test "$fname" = "q"
		then
			clear ; exit
		fi
		tput cup 7 18 ; read midinit
	done
	tput cup 8 18 ; read deptno
	while test "$deptno" = "-"
	do
		tput cup 7 18 ; echo " "
		tput cup 7 18 ; read midinit
		if test "$midinit" = "q"
		then
			clear ; exit
		fi
		tput cup 8 18 ; read deptno
	done
	tput cup 9 18 ; read jobtitle
	while test "$jobtitle" = "-"
	do
		tput cup 8 18 ; echo " "
		tput cup 8 18 ; read deptno
		if test "$deptno" = "q"
		then
			clear ; exit
		fi
		tput cup 9 18 ; read jobtitle
	done
		tput cup 10 18; read datehired
		while test "$datehired" = "-"
		do
		tput cup 9 18 ; echo " "
		tput cup 9 18 ; read jobtitle
		if test "$jobtitle" = "q"
		then
			clear ; exit
		fi
		tput cup 10 18 ; read datehired
	done
	#Check to see if last name is not blank before you
	#write to disk
	if test "$lname" != ""
	then
		echo"$phonenum:$lname:$fname:$midinit:$deptno:$jobtitle:$datehired" >> $phonefile
	fi
	tput cup 12 33 ; read looptest
	if test "$looptest" = "q"
	then
		clear ; exit
	fi
done






candyBar=.75
cornChips=1.85
gum=.90
nickles=0
dimes=0
quarters=0
dollars=0

item=input ("What are you buying? (candyBar, cornChips, gum): ")
billValue=("What is the value of your bill ? (i.e. 5.00, 1.00)")
billValue=float(billValue)


changeRequired=billValue-item
if changeRequired>=1.00:
    dollars = (changeRequired / 1.00) % 0
    changeLeft_1 = changeRequired - dollars

    if changeLeft_1 >= .25:
        quarters = (changeLeft_1 / .25) % 0
        changeLeft_2 = (changeLeft_1 - (quarters * .25))
        if changeLeft_2 >=.1:
            changeLeft_3 = (changeLeft2 / .1) % 0
            remainder=changeLeft_3%5
            if remainder==1:
                nickles = 1

print ("Your change is :",dollars," dollars;  ",quarters,"  quarters;  ",dimes,"  dimes;  ",nickles," nickles ! ")



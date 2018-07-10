# Name: Denise Tranberg
# Date Started: 7/9/18
# Date completed: 7/9/18
#
#
# Chapter 9  Assignment # 2
# P9.4 Design and Code
# Due July 15
#
# Implement a class Address.  An address has a house number, a street, an optional
# apartment number, a city, a state and a postal code.  Define the constructor
# such thatan object can be created in one of two ways: with an apartment numberor without.
# Supply a print method that prints the address with the street on one line and hte city,
# state and postal code on the next line.  Supply a method def comesBefore(self, other)
# that tests whether this address comes before other when compared by postal code.

######################################################################################################


class Address:

    def __init__(self,houseNum,streetName,city,state,postalCode,other,apptNum=None):
        ## Input of all data, including NULL entry for apptNum
        self.houseNum = houseNum
        self.streetName = streetName
        self.apptNum = apptNum
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.other=other

    def printAddress(self): ## Method to print out address information
        print(address.houseNum, address.streetName,"\n",
              address.city, address.state, address.postalCode)
        if address.apptNum is not None:
            print ("\nAppartment# ",address.apptNum)

    def comesBefore(self):  ## Method to compare zip codes
        if address.postalCode>address.other:
            print ("\nThis zip code(",address.postalCode,"), comes after the other zip code(",address.other,").")


## First Address with appartment#
address=Address(3333,"OtherZip","Lakewood", "Colorado",80222,11111,"65C")
address.printAddress()
address.comesBefore()

## Second Address without appartment#
print ("\n\n")
address=Address(1111,"Hill Way", "Lakewood", "Colorado", 80228,10101)
address.printAddress()
address.comesBefore()






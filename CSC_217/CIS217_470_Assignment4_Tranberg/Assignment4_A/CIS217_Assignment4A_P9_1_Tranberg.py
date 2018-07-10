## Denise Tranberg
## Start Date: 7/9/18
## End Date:7/9/18
## Chapter 9, Assignment # 1
## P9.1 Design and Code
## Due 7/15/18

#  We want to add a button to the tally counter in section 9.2 that allows an operator to undo an accidental button click.
#   Provide a method "def undo(self) that simulates such a button.
#   As an added precation, make sure that the operator cannot click the undo button more often than the click button.




##
#  This module defines the Counter class.
#

## Models a tally counter whose value can be incremented, viewed, or reset.
#
class Counter :
    ## Gets the current value of this counter.
    #  @return the current value
    #
    def getValue(self) :
        return self._value

    ## Advances the value of this counter by 1.
    #
    def click(self) :
        self._value = self._value + 1


    ## Resets the value of this counter to 0.
    #
    def reset(self) :
        self._value = 0


    def undo(self):
        if self._value ==0:
            print ("Can't have negative clicks, skipping...")
        else:
            self._value >=1
            self._value = self._value - 1




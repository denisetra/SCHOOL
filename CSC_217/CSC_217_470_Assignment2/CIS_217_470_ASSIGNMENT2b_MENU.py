# Programmer: Denise Tranberg
# Date Created:  6/21
# Date of Final Update:6/21
#
######################################################################################

#  Create a GUI program, Order Up!, that presents the user with a simple restaurant menu,
#   which list items and prices.  Let the user select different items and then show the user
#   the total bill.


#####################################################################################
#
#                    Declaring Variables / Import Modules
#
#*************************************************************************************

from tkinter import *

#menuPrices={"eggs":2.00,"bacon":4.00,"sausage":4.00,"orange juice":3.00}


######################################################################################
#
#                       Main Program and Explanation
#
######################################################################################


class Application(Frame):
    """GUI application that creates a story based on user input. """
    def __init__(self,master):
        """Initialize Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets to create the menu"""

        # create instruction label
        Label(self, text="Welcome to Order Up!").grid(row=0, column=0, columnspan=2, sticky=W)

        # create instruction label
        Label(self, text="Please choose what you would like to eat.").grid(row=1, column=0, columnspan=2, sticky=W)

        # create separation line
        Label(self, text="***************************************************").grid(row=2, column=0, columnspan=3, sticky=W)

        # create eggs check button
        self.is_eggs=BooleanVar()
        Checkbutton(self,text="eggs(2 each)             $2.00",variable=self.is_eggs).grid(row=3,column=0,sticky=W)

        # create bacon check button
        self.is_bacon=BooleanVar()
        Checkbutton(self,text="bacon (3 pieces)         $4.00",variable=self.is_bacon).grid(row=4,column=0,sticky=W)

        # create sausage check button
        self.is_sausage=BooleanVar()
        Checkbutton(self,text="sausage (2 links)        $4.00",variable=self.is_sausage).grid(row=5,column=0,sticky=W)

        # create orange_juice check button
        self.is_oj=BooleanVar()
        Checkbutton(self,text="Orange juice (6 oz)      $3.00\n",variable=self.is_oj).grid(row=6,column=0,sticky=W)


        # create a submit button
        Button(self, text="Click to total up purchases", command=self.food_eaten).grid(row=8, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=15, wrap=WORD) #Define size of text window
        self.story_txt.grid(row=10, column=0, columnspan=4) #Define position of text window
        self.story_txt.config(bg='black', fg='yellow') # playing with color

    def food_eaten(self):
        """fill text box list of foods eaten and total price"""
        # get values from GUI

        foodList = ""
        foodCost=0
        if self.is_eggs.get():
            foodList += "eggs           $2.00\n"
            foodCost+=2
        if self.is_bacon.get():
            foodList += "bacon          $4.00\n"
            foodCost += 4
        if self.is_sausage.get():
            foodList += "sausage        $4.00\n"
            foodCost += 4
        if self.is_oj.get():
            foodList += "OrangeJuice    $3.00\n"
            foodCost += 3
        foodCost = ('%.2f' % foodCost)

        # Create the output to screen of foodlist
        story = ("\nThank you for joining us here at Order Up!\n\nThe foods that you ate are as follows:\n\n\n"+foodList+"\nThe total amount owed is: $"+foodCost)
        # display the summary
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Order Up Menu")
app = Application(root)
root.mainloop()
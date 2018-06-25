from livewires import games, color
SCREEN_WIDTH=640
SCREEN_HEIGHT=480

# main
my_screen=games.Screen(SCREEN_WIDTH,SCREEN_HEIGHT)

wall_image=games.load_image("C:\\Users\dtranb001\Documents\PERSONAL\SCHOOL_2018\Assignment3\\brickwall.jpg",transparent=False)
my_screen.set_background(wall_image)

games.Text(screen=my_screen, x=500, y=30, text=":Score: 199999", size=50, color=color.black)
#games.Text(my_screen, 500, 30,":Score: 199999", 50, color.black)

my_screen.mainloop()
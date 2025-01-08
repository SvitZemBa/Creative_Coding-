import turtle as tu
import random
import argparse

SEASON_EASTER = "easter"
SEASON_XMAS = "xmas"

# I used the argparse library to parse command line arguments, 
# with which I control the program's behavior. The argument "--season" 
# can be used to specify "xmas" for a Christmas tree, "easter" for an Easter tree, 
# or any other value for the crazy mode. 
# If no argument is specified, the program runs in Easter mode by default.

# Create an argument parser
parser = argparse.ArgumentParser(description="Arguments for the tree drawer")
parser.add_argument("--season", type=str, help="xmas or easter", default=SEASON_EASTER)
args = parser.parse_args()

# turtle invisible 
tu.speed(0)
tu.hideturtle()

#Before, I didn’t use the class Drawable, but later I added it as an exercise for inheritance 
class Drawble:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    def draw (self, x,y):
        raise NotImplementedError ("Draw method must be implemented!")
    

#class draws Xmastree, inherits class Drawble
#variable "height" stored as "size" attribute in class Drawble
#Xmastree draw method itself was writen with the help of ChatGPT
class XTree(Drawble):
    def __init__(self, height, color):
        super().__init__(height*2.3, color)
       
        
    def draw(self, x, y):
        print (f"Xmax tree height: {self.size} color: {self.color} position: {x}-{y}")
        # Draw the tree layers
        def draw_triangle(color, size):
            tu.fillcolor(color)
            tu.begin_fill()
            for _ in range(3):
                tu.forward(size)
                tu.left(120)
            tu.end_fill()

        layer_height = self.size // 3

        # Draw each triangle layer
        for i in range(3):
            size = self.size - i * layer_height
            tu.penup()
            tu.goto(-size // 2 + x, i * (layer_height + self.size/10) + y)
            tu.pendown()
            draw_triangle(self.color, size)

class Tree(Drawble):
    def __init__(self,height, color):
        super().__init__(height, color)
    
    def draw(self, x, y):
        print (f"Tree height: {self.size} color: {self.color} position: {x}-{y}")
    
        # Draw the tree layers
        def draw_circle(color, size):
            tu.fillcolor(color)
            tu.begin_fill()
            tu.circle(size)
            tu.end_fill()

        layer_height = self.size // 4

        # Draw each circle layer
        for i in range(3):
            size = self.size/2.5 + i * layer_height
            tu.penup()
            tu.goto(x, i * (layer_height + self.size/4) + y)
            tu.pendown()
            draw_circle(self.color, size)


#class draws Xmas toys, inherits class Drawble
#variable "radius" stored as "size" attribute in class Drawble
class Treetoy(Drawble):
    def __init__(self, radius, color):
        super().__init__(radius,color)
    
    def draw(self, x, y):
        print (f"treetoy radius: {self.size} color: {self.color} position: {x}-{y}")
        tu.penup()
        tu.goto(x,y)
        tu.color(self.color)
        tu.pendown()
        tu.begin_fill()
        tu.circle(self.size)
        tu.end_fill()
        tu.penup()

class Egg(Drawble):
    def __init__(self, size, color):
        super().__init__(size, color)

    def draw(self, x, y):
        tu.penup()
        tu.goto(x,y)
        tu.color(self.color)
        tu.pendown()
        tu.begin_fill()
        tu.fillcolor(self.color)
        tu.left(45)
        for _ in range(2):
        #chatGPT helped me with this part, but I changed size and fix the problem with the angle 
            tu.circle(self.size, 90)  # Top half of the egg (smaller arc)
            tu.circle(self.size/2, 90)   # Bottom half of the egg (larger arc)
        tu.end_fill()
        tu.right(45)

drawables=[XTree, Tree, Treetoy, Egg]
color_list=["blue", "pink", "purple", "red", "yellow", "orange", "navy"]
ornament_list=[]
random.seed()

if (args.season == SEASON_EASTER):
    tree = Tree(200,"green")
    for i in range (10):
        #for-ukrainian translation протягом
        #list is also a class. Append is a method of this class,
        #that adds new element to the end of the list
        #
        size = random.random()*20+15
        color = random.choice(color_list)
        #Question - how to call documentation?
        ornament_list.append(Egg(size, color))

#below is the same logic with different classes and instances
elif (args.season == SEASON_XMAS):
    tree = XTree(200,"green")
    for i in range (10):
        ornament_list.append(Treetoy(random.random()*20+15, random.choice(color_list)))
#because above I created list of classes "drawables=[XTree, Tree, Treetoy, Egg]"
# here I can randomly choose instance of wich class will be created for tree and ornament        
else:
    tree = random.choice(drawables)(200, random.choice(color_list))
    random_ornament = random.choice(drawables)
    for i in range (10):
        ornament_list.append(random_ornament(random.random()*20+15, random.choice(color_list)))


def onclick(x, y):
    random.choice(ornament_list).draw(x,y)

try:
    tree.draw(0,-250)
except Exception as e:
    print(f"An error occurred: {e}")
    raise e

# Bind the onclick event to the handle_onclick function
tu.onscreenclick(onclick)
# Listen for events
tu.listen()

# Keep the window open
tu.done()

#type "--season=xmas" to call xmas mode
#type "--season=easter" to call easter mode
#type "--season=anything you want" to call crazy mode
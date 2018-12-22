from turtle import *
from shapes import *
from random import randint

import webbrowser

class Santa():
    """ 
    Creates a "Santa" class - purely for illustrating creating your own class :)
    """
    
    ## fixed variable
    HOME = "North Pole"
    
    def __init__(self, color, num_of_gifts, jolliness = 3, favorite_song = 'https://www.youtube.com/watch?v=76WFkKp8Tjs'):
        """ 
        Constructor function for the Santa class
        """
        self.color = color
        self.num_of_gifts = num_of_gifts
        self.jolly = jolliness
        self.song = favorite_song
        
        
    def add_gift(self, new_gifts):
        """
        Method that adds scalar 'new_gifts' to attribute 'num_of_gifts'
        """
        self.num_of_gifts += new_gifts
        
    def give_gift(self):
        """
        Method that decreases attribute 'num_of_gifts' by 1 and increases attribute 'jolly' by 1.
        """
        if self.num_of_gifts > 0:
            self.num_of_gifts -= 1
            self.jolly += 1
        else:
            print('There are no more gifts left!')
          
    def be_jolly(self):
        """
        Method that prints string "Ho!" for range(jolly) and prints "Merry Christmas"
        """
        for it in range(self.jolly):
            print("Ho! ")
        print("Merry Christmas!")    
    
    def play_song(self):
        """
        Method that opens weblink given by attribute 'song'
        """
        webbrowser.open(self.song) 
    
    def draw_hat(self):
        """
        Method that draws a santa hat using an instance of the "Turtle" class, with color given by attribute 'color'
        """
        ### Example taken from https://www.101computing.net/chirstmas-tree/
        
        myPen = Turtle()
#         myPen.shape("turtle")
        myPen.speed(25)

        window = turtle.Screen()
        window.bgcolor("#FFFFFF")

        draw_circle(myPen, "#69D9FF", 0, -200, 200)

        draw_triangle(myPen, self.color, -100, -80, 200)
        draw_circle(myPen, "white", 0, 70, 30)

        for it in range(0, 200, 20):
          draw_circle(myPen, "white", -90+it, -100, 20)

        myPen.hideturtle()
        done()


class Christkind(Santa):    
    """ 
    Creates a "child" class of the "parent" Santa class - purely for illustrating creating your own class :)
    """
    
    HOME = "Heaven"
    
    def __init__(self, num_of_gifts, favorite_song = 'https://www.youtube.com/watch?v=76WFkKp8Tjs'):
        """ 
        Constructor function for the Christkind class - note that Christkind has less attributes than Santa!
        """
        self.num_of_gifts = num_of_gifts
        self.song = favorite_song
        
    
    
    
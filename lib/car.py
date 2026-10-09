from lib.tyre import *

class Car:
    # User-facing properties:
    #   tyres (position of tyre object): many Tyre objects

    def __init__(self):
        self.left = Tyre()
        self.right = Tyre()
        self.rear_left = Tyre()
        self.rear_right = Tyre()
        

    def current_readings(self):
        result = {
            'left' : self.left.get_current(),
            'right': self.right.get_current(),
            'rear_left': self.rear_left.get_current(),
            'rear_right': self.rear_right.get_current()
        }
        return result
        # Parameters:
        #   none
        # Returns:
        #   a list of current readings for each position of tyre
        #   
        # Side-effects:
        #   none
        pass # No code here yet
    
    def view_all_history(self):
        # Parameters:
        #   none
        # Returns:
        #   historical readings for each position of tyre
        # Side-effects:
        #   none
        pass # No code here yet

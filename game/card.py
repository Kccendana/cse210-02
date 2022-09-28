import random


class Card:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number deck of card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.points = 0

    def deal(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Die): An instance of Card.
        """
        self.value = random.randint(1, 13)
        #self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0
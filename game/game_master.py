from game.card import Card

class Game_master():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self): # Completed by HB

        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Card()
            self.dice.append(die)

    def start_game(self): # Completed by HB

        while self.is_playing:
            self.get_inputs()
            self.do_updates() # ADD FUNCTION FOR do_updates HB
            self.do_outputs() # ADD FUNCITON FOR do_outputs HB

    def get_inputs(self): # Completed by HB

        roll_dice = input('Do you want to roll? [y/n]: ')
        self.is_playing = roll_dice(roll_dice == 'y')

import tkinter
import numpy as np

from Modules.DrawCard import players_cards
from functools import partial


def sourceFunction(name):
    cards = players_cards[name]
    print(f'Cards for player {name} \nare {cards}')

num_players = len(players_cards)

# Global Button configuration variables
button_width = 20  
button_height = 2  
button_colour = 'darkred'
text_colour = 'white'

# Root dimensions based on the number of players and button dimensions
root_height = 400
root_width = 200

# Initialize the root window
root = tkinter.Tk()
root.title('CHOOSE A PLAYER TO GO NEXT')
root.config(bg='darkgrey')

# Center the window
centerWidget(root, root_width, root_height)

# Create and pack buttons for each player
for player_name in players_cards.keys():
    func = partial(sourceFunction, name=player_name)
    button = tkinter.Button(root, command=func, text=f'{player_name} \nCards', font = ('Consolas', 14), bg = button_colour, fg = text_colour)
    button.config(width=button_width, height=button_height)
    button.pack(fill= 'both',  expand= True) 

# Start the main loop
root.mainloop()

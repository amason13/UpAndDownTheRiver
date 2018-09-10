# UpAndDownTheRiver

Up and down the river is a 4+ person card game played similar to whist in which people must win tricks to earn points.

Rules:
In any given round, players are dealt cards face down and a trump card is turned over to establist which suit is the trump suit. 
Each player then simultaneously declares how many tricks (from 0 - num_cards) they will win in this round, based on the strength of their hand.
The player to the left of the dealer leads initially, with players obliged to follow suit if they can. The highest card of the lead suit -
or highest trump card if any have been played - wins the trick, and the winning player leads out next. After all the dealt cards have been played,
players tally up their tricks earnt. If a players has earnt as many tricks as they claimed, they get 10 points plus 5 points for each trick. 
Otherwise, they get 0 points. The next round then begins with players getting one less card than previously and this is repeated until a round is played with 1 card. 
This is the 'down the river' part of the game. Now the round of 1 card is repeated and players go back up the river - getting an extra card 
with each subsequent round. Ultimately, the winner is the person with the most points. 

I have created a simple version of the game which uses treys poker hand evaluator. The computer players are either random players taking actions and 
declaring tricks at random or greedy players playing their best possible card and declaring tricks at random from [num_cards/2, num_cards] so don't 
expect to face much competition! 

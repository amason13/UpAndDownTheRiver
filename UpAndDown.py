import numpy as np
from treys import Deck, Card
        
class UpAndDown():
    
    def __init__(self,n_player=4):
        
        self.deck = Deck()
        self.trumpCard = 0
        self.trumps = 0
        self.leadSuit = 0
        self.n = 52//n_player-1
        self.playerList = []
        self.playerOrder = []
        self.playedCards = []
        self.leadPlayer = None
        
    def next_round(self):
        
        self.update_player_list()
        self.leadPlayer = self.playerList[0]
        self.trumpCard = 0
        self.trumps = 0
        self.playedCards = []
        self.leadSuit = 0
        self.deck.shuffle()
        for player in self.playerList:
            player.trickCount = 0
        
    def update_trumps(self):
        
        self.trumps = Card.get_suit_int(self.trumpCard)
        
        
    def update_lead_suit(self):
        if self.playedCards==[]:
            pass
        else:
            self.leadSuit = Card.get_suit_int(self.playedCards[0])
        
        
    def update_player_list(self):
        
        newList=self.playerList
        player = newList.pop(0)
        newList.append(player)
        self.playerList = newList
        self.playerOrder = self.playerList
        
    def deal_cards(self):
        for player in self.playerList:
            for i in range(self.n):
                player.cards.append(self.deck.draw())
            
            player.cards.sort(reverse=True)
        
        
    def available_moves(self,player):
        
        if self.leadPlayer == player:
            return player.cards
        else:
            lsCards = []
            for card in player.cards:
                if Card.get_suit_int(card)==self.leadSuit:
                    lsCards.append(card)
            if lsCards == []:
                return player.cards
            else:
                return lsCards
        
    def eval_trick_winner(self):
        
        trumps = []
        for card in self.playedCards:
            if Card.get_suit_int(card) == self.trumps:
                trumps.append(card)
        trumps.sort(reverse=True)
        
        
        if len(trumps)>0:
            bestCard=trumps[0]
            
        else:
            leadSuits=[]
            for card in self.playedCards:
                if Card.get_suit_int(card) == self.leadSuit:
                    leadSuits.append(card)
                leadSuits.sort(reverse=True)
                bestCard=leadSuits[0]
        
        winnerIndex = self.playedCards.index(bestCard)
        winner = self.playerOrder[winnerIndex]
        winner.trickCount += 1
        print('\n',winner.name,' wins the trick with ',Card.print_pretty_card(bestCard))
        self.leadPlayer = winner
        self.playedCards=[]
        
            
    def update_player_order(self):

        start = self.playerOrder.index(self.leadPlayer)
        order = []
        for i in range(len(self.playerOrder)):
            j = start%len(self.playerOrder)
            order.append(self.playerOrder[j])
            start+=1
        self.playerOrder = order
        
    def play_round(self):
        self.deck.shuffle()
        self.trumpCard = self.deck.draw()
        self.update_trumps()
        self.deal_cards()
        
        for player in game.playerList:
            player.cards.sort(reverse=True)
            
        print('\n The trump card is ', Card.print_pretty_card(self.trumpCard))
        print('\n Your cards are: ', Card.print_pretty_cards(self.playerList[self.playerList.index(p1)].cards))
            
        for player in self.playerList:
            player.makeClaim()
        for player in self.playerList:
            print('\n',player.name, ' claims ', player.claim, ' tricks.')
        
        for i in range(self.n):
            for player in self.playerOrder:
                player.play_card()
                self.update_lead_suit()
                
                if self.playedCards == []:
                    pass
                elif len(self.playedCards)>1:
                    print('\n',Card.print_pretty_cards(self.playedCards))
                else:
                    print('\n',Card.print_pretty_card(self.playedCards[0]))
            
            self.eval_trick_winner()
            self.update_player_order()
            
        for player in self.playerList:
            player.score_player()
            
        print('\n After the round of ',self.n,' cards, the scores are:')
        for player in self.playerList:
            print(player.name,' : ',player.score)
            
        


        
        
class RandomPlayer():
    def __init__(self, game, name):
        self.game = game
        self.cards = []
        self.trickCount = 0
        self.claim = 0
        self.score = 0
        self.name = name
        
    def reset(self):
        self.cards=[]
        self.claim=0
        self.trickCount=0
        
    def makeClaim(self):
        self.claim = np.random.randint(len(self.cards))
        
    def play_card(self):
        valids = self.game.available_moves(self)
        a = np.random.randint(len(self.game.available_moves(self)))
        c = valids[a]
        game.playedCards.append(c) 
        self.cards.remove(c)
        
    def score_player(self):
        if self.claim == self.trickCount:
            self.score += 10 
            self.score += 5*self.trickCount
    
class GreedyPlayer():
    def __init__(self, game, name):
        self.game = game
        self.cards = []
        self.trickCount = 0
        self.claim = 0
        self.score = 0
        self.name = name
        
    def reset(self):
        self.cards=[]
        self.claim=0
        self.trickCount=0
        
    def makeClaim(self):
        self.claim = np.random.randint(len(self.cards)/2,len(self.cards))
        
    def play_card(self):
        valids = self.game.available_moves(self)
        a = 0
        c = valids[a]
        game.playedCards.append(c)
        self.cards.remove(c)
        
    def score_player(self):
        if self.claim == self.trickCount:
            self.score += 10 
            self.score += 5*self.trickCount
    
class HumanPlayer():
    def __init__(self,game,name):
        self.game = game
        self.cards = []
        self.trickCount = 0
        self.claim = 0
        self.score = 0
        self.name = name

    def reset(self):
        self.cards=[]
        self.claim=0
        self.trickCount=0
        
    def makeClaim(self):
        print('\n How many tricks do you claim?')
        self.claim = int(input())
        
    def play_card(self):
        
        valids = self.game.available_moves(self)
        print('\n Which card do you want to play? Choose a number 1 -',len(list(valids)))
        for i in range(len(valids)):
            print(i+1, ' : ', Card.print_pretty_card(valids[i]))
        a = int(input())
        c = valids[a-1]
        game.playedCards.append(c)
        self.cards.remove(c)

    def score_player(self):
        if self.claim == self.trickCount:
            self.score += 10 
            self.score += 5*self.trickCount
        
    
game = UpAndDown(7)

p1 = HumanPlayer(game,'Ash')
p2 = GreedyPlayer(game,'Greedy Gill')
p3 = RandomPlayer(game,'Mr Unpredictable')
p4 = RandomPlayer(game,'Erratic Erin')
p5 = GreedyPlayer(game,'Fat Tony')
p6 = RandomPlayer(game,'Randy Andy')
p7 = GreedyPlayer(game,'Best Move Mike')

game.playerList = [p1,p2,p3,p4,p5,p6,p7]
game.playerOrder = game.playerList

print('\n Down the river we go...')
while game.n>1:
    game.play_round()
    game.next_round()
    game.n-=1

game.play_round()
game.next_round()

print('\n Up the river we go...')
while game.n<52//len(game.playerList):
    game.play_round()
    game.next_round()
    game.n+=1

print('\n Final scores are: ')
for player in game.playerList:
    print(player.name, ' : ', player.score)

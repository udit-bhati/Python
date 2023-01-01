import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.card = []
        self.values = 0
        self.aces = 0

    def add_card(self, single_card):
        self.card.append(single_card)
        self.values += values[single_card.rank]
        if single_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces > 0:
            self.values -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Please enter an integer.")
        else:
            if chips.bet > chips.total:
                print(f"Sorry! You don't have enough chips. You have {chips.total}")
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' : ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" Hidden Card")
    print('',dealer.card[1])  
    print("\nPlayer's Hand:", *player.card, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.card, sep='\n ')
    print("Dealer's Hand =",dealer.values)
    print("\nPlayer's Hand:",*player.card, sep='\n ')
    print("Player's Hand =",player.values)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:

    print("Welcome to BlackJack.")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.values > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.values <= 21:

        while dealer_hand.values < 17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.values > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.values > player_hand.values:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.values < player_hand.values:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
    
    print("\nPlayer stand at",player_chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' : ")
    
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Thank You for Playing Blackjack")
        break
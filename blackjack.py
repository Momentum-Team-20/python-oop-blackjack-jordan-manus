# Write your blackjack game here.
import random

SUITS = ['♤', '♧', '❤️', '♢']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
VALUE = []


class Card:
    def __init__(self, suit, rank, value=None) -> None:
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'
    

class Deck:
    def __init__(self) -> None:
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                if card.rank == 'A':
                    card.value = 11
                elif card.rank in range(2, 11):
                    card.value = rank
                else:
                    card.value = 10
                self.cards.append(card)
                print(card)
        print(f'There are  {len(self.cards)} in this deck')

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        print(f'players name is: {self.name}')

    def __str__(self) -> str:
        return self.name
    
    def look_at_hand(self):
        '''shows cards in hand to player'''
        for x in self.hand:
            print(x)

    def calc_hand_value(self):
        '''return the total value of the hand'''
        sum = 0
        for card in self.hand:
            sum += card.value
        sum = self.if_ace(card, sum)
        print(f'the sum is: {sum}')

    def if_ace(self, card, sum):
        '''changes value of Ace from 11 to 1 if over 21'''
        print('inside the if_ace')
        for card in self.hand:
            if sum > 21 and card.rank == 'A': 
                sum -= 10
        print(f'this is the new sum: {sum}')
        return sum


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__('Dealer')
        print(f'dealers name is: {self.name}')
        print(f'the dealers hand is: {self.hand}')


class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(input('What is your name? '))
        self.dealer = Dealer()
        self.deal_cards()

    def deal_cards(self):
        '''Deal 2 cards each to the player(s) and dealer. '''
        while len(self.player.hand) < 2 and len(self.dealer.hand) < 2:
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            card = self.deck.cards.pop()
            self.dealer.hand.append(card)
            print(f'{self.player} has {self.player.hand} and {self.dealer} has {self.dealer.hand}')

    def hit(self):
        '''Deal 1 card to the selected player'''
        for card in self.deck.cards:
            if card.rank == 'A':
                self.player.hand.append(card)

# ace_of_spades = Card('spade', 'A', (1, 11))
# print(ace_of_spades)

# four_of_clubs = Card('club', 4, 4)
# print(four_of_clubs)
# deck = Deck()

new_game = Game()
breakpoint()

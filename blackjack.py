# Write your blackjack game here.
import random

SUITS = ['♤', '♧', '❤️', '♢']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K']
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
                    card.value = (1, 11)
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

    def hit(self, player):
        '''Deal 1 card to the selected player'''
        pass
        

# ace_of_spades = Card('spade', 'A', (1, 11))
# print(ace_of_spades)

# four_of_clubs = Card('club', 4, 4)
# print(four_of_clubs)
# deck = Deck()

new_game = Game()
breakpoint()
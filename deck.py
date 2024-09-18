import os

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
        return f"{self.suit} {self.value}"
        
    
class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards
        
    def show_all(self):
        for card in self.cards: 
            print(f"{card}")

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards left to deal")
        
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]  # Remove dealt cards from the deck
        
        return dealt_cards
    
    @staticmethod
    def make_deck():  
        cards = [] 
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
       
        for suit in suits:
            for value in values: 
                cards.append(Card(suit, value)) 
                
        return cards


os.system('cls' if os.name == 'nt' else 'clear')

cards = Deck.make_deck()

deck = Deck(cards)

# dealt_card = deck.deal(51)
# print(dealt_card[0])


deck.show_all()
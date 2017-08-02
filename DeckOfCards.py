#Create Class Card
from random import randint

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.FindName()
        self.FindColor()

    def FindColor(self):
        if self.suit == "diamond" or self.suit == "heart":
            self.color = "red"
        else:
            self.color = "black"
        return self

    def FindName(self):
        if self.value > 1 and self.value < 11:
            self.name = self.suit + str(self.value)
        elif self.value == 1:
            self.name = self.suit + "Ace"
        elif self.value == 11:
            self.name = self.suit + "Jack"
        elif self.value == 12:
            self.name = self.suit + "Queen"
        elif self.value == 13:
            self.name = self.suit + "King"
        return self

c1 = Card("clubs",1)
# print c1.name

#Create Class Deck
class Deck(object):
    def __init__(self):
        self.deck= []
        self.resetDeck()
    def resetDeck(self):
        suits = ["diamond", "heart", "spade", "club"]
        for suit in suits:
            for val in range(1,14):
                self.deck.append(Card(suit,val))
        return self

    #shuffle first, then dealtwo
    def shuffle(self):
        shuffled_deck = []
        while(len(self.deck) > 0): # for i in self.deck:
            pull = randint(0, len(self.deck) - 1)
            shuffled_deck.append(self.deck[pull])
            del self.deck[pull]
        self.deck = shuffled_deck
        return self
    def cutDeck(self):
        cut = randint(0,51)
        print cut
        tophalf = self.deck[:cut]
        bottomhalf = self.deck[cut:]
        self.deck = bottomhalf + tophalf
        return self
    def dealtwo(self):
        hand = []
        hand.append(self.deck[0])
        hand.append(self.deck[1])
        self.deck.remove(self.deck[0])
        self.deck.remove(self.deck[1])
        return hand

d1 = Deck()
d1.shuffle()
for card in d1.deck:
    print card.name
d1.cutDeck()
for card in d1.deck:
    print card.name
print "Deck Size Before Deal: " + str(len(d1.deck))
myhand = d1.dealtwo()
print "Hand Printed"
for card in myhand:
    print card.name
print "The current Deck"
for card in d1.deck:
    print card.name
print "Deck Size NOW: " + str(len(d1.deck))
# print d1.deck




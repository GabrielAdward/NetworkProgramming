from Cards import Card
import random


class CardDeck:
    def __init__(self):
        self.reset()
        
    def shuffle(self):
        random.shuffle(self.cardDeck)

    def getCard(self):
        topCard = len(self.cardDeck)-1
        drawnCard = self.cardDeck[topCard]
        self.cardDeck.pop()
        return drawnCard

    def size(self):
        return len(self.cardDeck)

    def reset(self):
        self.cardDeck = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cardDeck.append(Card(i, j))
        return self.cardDeck


deck = CardDeck()
deck.shuffle()
while deck.size() > 0:
 card = deck.getCard()
 print("Card {} has value {}".format(card.getSuit(), card.getValue()))

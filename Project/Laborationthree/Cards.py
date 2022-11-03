from multiprocessing import Value


class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
           if self._value == 1:
               return "Ace"
           elif self._value == 2:
               return "Two"
           elif self._value == 3:
               return "Three"
           elif self._value == 4:
               return "Four"
           elif self._value == 5:
               return "Five"
           elif self._value == 6:
               return "Six"
           elif self._value == 7:
               return "Seven"
           elif self._value == 8:
               return "Eight"
           elif self._value == 9:
               return "Nine"
           elif self._value == 10:
               return "Ten"
           elif self._value == 11:
               return "Jack"
           elif self._value == 12:
               return "Queen"
           elif self._value == 13:
               return "King"

    def getSuit(self):
            if self._suit == 1:
                return "Clubs"
            elif self._suit == 2:
                return "Diamonds"
            elif self._suit == 3:
                return "Hearts"
            elif self._suit == 4:
                return "Spades"

    def __str__(self):
        return f"{self._suit}({self._value})"




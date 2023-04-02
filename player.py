from poker_rules import *
from itertools import combinations

class Player:
    def __init__(self, name):
        self.name = str(name)
        self._holeCards = []
        self._bestHand = None

    def __str__(self):
        if not self._bestHand:
            return self.name + ":" + str(self._holeCards)
        else:
            return self.name + ":" + str(self._bestHand) + "," + categorize_hand(self._bestHand)
        
    def __repr__(self):
        return str(self)
        
    def add_card(self, c):
        if len(self._holeCards) < 2:
            self._holeCards.append(c)
        else:
            raise ValueError("Player can only have two hole cards")

    def update_best_hand(self, table):
        """
        return the best 5 card hand possible for player 
        using a combination of hole cards and community cards
        
        :param table: list of Cards on the table
        :return: best possible hand for player
        :rtype: list[Card]
        """
        if len(table) < 3:
            raise ValueError("table has insufficient community cards")
        if len(table) >= 3:
            lst_hands = [list(combo) for combo in combinations(self._holeCards + table, 5)]
            self._bestHand = best_hand(lst_hands)
            self._bestHand.sort(reverse=True)
            return self._bestHand    

    def get_holecards(self):
        return self._holeCards

    def get_best_hand(self):
        if not self._bestHand:
            raise ValueError("Best hand undetermined. Call update_best_hand")
        return self._bestHand

    def get_holecards_pokernotation(self):
        """
        return a string representation of the holecards in conventional poker notation
        e.g. 'AA', 'AKs', 'KQo'
        :return: two or three character string:
            each capitalized character represents the value of a card
            non-pairs are classified as 's' or 'o' where s means suited, and o means offsuite
        :rtype: string
        """
        self._holeCards.sort(reverse=True)
        poker_notation = self._holeCards[0].value + self._holeCards[1].value
        if poker_notation[0] == poker_notation[1]:
            return poker_notation
        else:
            if self._holeCards[0].suite == self._holeCards[1].suite:
                poker_notation = poker_notation + "s"
            else:
                poker_notation = poker_notation + "o"
            return poker_notation
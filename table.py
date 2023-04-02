from player import Player
from poker_rules import best_hand

def winning_player(players: Player):
    """
    given a list of players, return the winners who have the best poker hand
    
    :param players: list of [Player] objects
    :return: list of players that won
    :rtype: list[Player]
    """
    player_best_hands = [p.get_best_hand() for p in players]
    winning_hand = best_hand(player_best_hands)
    winners = [p for p in players if p.get_best_hand() == winning_hand]
    return winners
        
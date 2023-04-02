from deck import Deck
from table import *
from poker_stats import *
import csv 

starting_hands_stats = {}

# dict to track win/loss stats
hand_stats = {'won': 0, 'played': 0}
create_stats_dict(starting_hands_stats, hand_stats)

num_simulations = 100000
num_players = 8
for n in range(2, num_players+1):
    for i in range(num_simulations):
        print(f"game{i}")
        # define a deck of cards
        play_deck = Deck()
        play_deck.shuffle()
        assert len(play_deck) == 52

        # set players
        players = [Player(f"Player{p}") for p in range(n)]

        # deal cards
        for _ in range(2):
            for p in players:
                p.add_card(play_deck.dealcard())

        for p in players:
            p_hand = p.get_holecards_pokernotation()
            starting_hands_stats[p_hand]['played'] += 1

        play_deck.dealcard() # burn before flop
        flop_cards = [play_deck.dealcard() for _ in range(3)]
        # print("Flop:", flop_cards)
        # print(players)

        play_deck.dealcard() # burn before flop
        turn_card = [play_deck.dealcard()]
        # print("Turn:", turn_card)

        play_deck.dealcard() # burn before flop
        river_card = [play_deck.dealcard()]
        # print("River:", river_card)

        table = flop_cards + turn_card + river_card
        # print("Table: ", table)

        for p in players:
            bh = p.update_best_hand(table)
            # print(poker_rules.categorize_hand(bh), bh)


        for p in winning_player(players):
            p_hand = p.get_holecards_pokernotation()
            starting_hands_stats[p_hand]['won'] += 1


    with open(f"simulation_{n}.csv", 'w', newline='') as f:
        cols = ['hand','won','played']
        w = csv.DictWriter(f, cols)
        w.writeheader()
        for hand, stat in starting_hands_stats.items():
            row = {"hand": hand}
            row.update(stat)
            w.writerow(row)
    
    


















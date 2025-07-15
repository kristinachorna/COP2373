# Kristina Chorna
# Programming Exercise 11
# The goal of this program is to deal a Poker hand of five cards and prompt the user to enter the number of
# the cards they wish to replace. It then replaces the cards with different ones and display the result.

import random

# Card and Deck classes
class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in range(4)
                      for rank in range(1, 14)]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


# Function to deal a hand
def deal_hand(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        hand.append(deck.deal_card())
    return hand


# Replace selected cards in the hand
def replace_cards(hand, deck, indices_to_replace):
    for i in indices_to_replace:
        if 0 <= i < len(hand):
            hand[i] = deck.deal_card()
    return hand


# display a hand
def print_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")


# Main game
def main():
    deck = Deck()
    hand = deal_hand(deck, 5)

    print("\nYour initial hand:")
    print_hand(hand)

    replace_input = input("\nEnter card numbers to replace (e.g., 1, 3, 5): ")
    if replace_input.strip():
        try:
            indices = [int(i.strip()) - 1 for i in replace_input.split(',') if i.strip()]
            hand = replace_cards(hand, deck, indices)
        except ValueError:
            print("Invalid input. Skipping card replacement.")

    print("\nYour final hand:")
    print_hand(hand)


if __name__ == "__main__":
    main()

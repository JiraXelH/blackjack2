"""Hi-Lo card counting and betting strategy."""
from typing import List, Tuple

CARD_VALUES = {
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": -1,
    "J": -1,
    "Q": -1,
    "K": -1,
    "A": -1,
}


def update_count(cards_seen: List[str], num_decks: int = 8) -> Tuple[int, int]:
    """Return running and true counts."""
    running = sum(CARD_VALUES.get(card, 0) for card in cards_seen)
    decks_remaining = max(num_decks - len(cards_seen) / 52, 1)
    true = int(running / decks_remaining)
    return running, true


def suggest_action(player_cards: List[str], dealer_card: str, true_count: int) -> str:
    """Very simplified basic strategy placeholder."""
    total = 0
    for card in player_cards:
        if card in ["J", "Q", "K", "10"]:
            total += 10
        elif card == "A":
            total += 11
        else:
            total += int(card)
    if total <= 11:
        return "Hit"
    if total >= 17:
        return "Stand"
    if true_count >= 2 and len(player_cards) == 2:
        return "Double"
    return "Hit"


def recommend_bet(balance: float, true_count: int) -> float:
    """Return bet size recommendation based on true count."""
    base = balance * 0.02
    if true_count >= 2:
        return balance * 0.05
    return base

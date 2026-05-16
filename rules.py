# rules.py
# Funzioni pure per le regole del gioco.
# Questo file NON importa pygame.

VOWELS = set("AEIOU")


def is_even(number: int) -> bool:
    """Restituisce True se number è pari."""
    return number % 2 == 0


def is_vowel(letter: str) -> bool:
    """Restituisce True se letter è una vocale (A, E, I, O, U)."""
    return letter.upper() in VOWELS


def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    """
    Calcola la risposta corretta in base alla posizione della carta.
    - TOP    → controlla se il numero è pari
    - BOTTOM → controlla se la lettera è una vocale
    """
    if position == "TOP":
        return is_even(number)
    else:  # BOTTOM
        return is_vowel(letter)

# generator.py
# Genera i trial casuali del gioco.
# Riceve un oggetto rng (random.Random) dall'esterno: così il seed
# è controllabile e le partite sono riproducibili.
# Questo file NON importa pygame.

import random
import string

from models import Trial
from rules import compute_expected_answer

POSITIONS = ["TOP", "BOTTOM"]
LETTERS   = list(string.ascii_uppercase)   # A-Z
NUMBERS   = list(range(1, 10))             # 1-9


def generate_trial(rng: random.Random) -> Trial:
    """
    Genera un trial casuale usando l'oggetto rng passato.
    Lo stesso seed produce sempre la stessa sequenza di trial.
    """
    position = rng.choice(POSITIONS)
    letter   = rng.choice(LETTERS)
    number   = rng.choice(NUMBERS)
    expected = compute_expected_answer(position, letter, number)

    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=expected,
    )

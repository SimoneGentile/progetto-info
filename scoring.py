# scoring.py
# Gestisce il punteggio del gioco.
# Questo file NON importa pygame.

from config import POINTS_CORRECT, POINTS_WRONG


def apply_answer(score: int, is_correct: bool) -> int:
    """
    Aggiorna il punteggio in base alla risposta.
    - risposta corretta  → score + 10
    - risposta errata    → score invariato (0 punti in meno)
    Restituisce il nuovo punteggio.
    """
    if is_correct:
        return score + POINTS_CORRECT
    else:
        return score + POINTS_WRONG

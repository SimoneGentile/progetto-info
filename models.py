# models.py
# Definisce la struttura dati Trial con @dataclass.
# Questo file NON importa pygame: è logica pura.

from dataclasses import dataclass, field


@dataclass
class Trial:
    """
    Rappresenta un singolo trial del gioco.

    position        : "TOP" o "BOTTOM"
    letter          : lettera maiuscola (es. "A", "K")
    number          : numero intero da 1 a 9
    expected_answer : risposta corretta (True = SÌ, False = NO)
    user_answer     : risposta data dal giocatore (None se non ha ancora risposto)
    is_correct      : True se user_answer == expected_answer
    """
    position: str
    letter: str
    number: int
    expected_answer: bool
    user_answer: bool | None = None
    is_correct: bool = False

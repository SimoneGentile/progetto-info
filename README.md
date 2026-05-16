# Brain Shift 🧠

Un gioco di rapid task-switching sviluppato con Python e pygame.

## Come si gioca

Ogni round mostra una carta in posizione **alta** o **bassa** con una lettera e un numero.

- **Carta in alto** → rispondi: il numero è pari?
- **Carta in basso** → rispondi: la lettera è una vocale?

| Tasto | Azione |
|-------|--------|
| `→`  | SÌ |
| `←`  | NO |
| `R`   | Rigioca (nella schermata risultati) |
| `ESC` | Esci |

La partita dura **60 secondi**. Alla fine vedi il tuo punteggio, le risposte corrette/sbagliate e la percentuale di accuratezza.

## Installazione

```bash
git clone <url-del-repo>
cd brain_shift
pip install -r requirements.txt
python main.py
```

## Struttura del progetto

```
brain_shift/
├── main.py       ← loop principale, macchina a stati
├── config.py     ← costanti (colori, dimensioni, timing)
├── models.py     ← dataclass Trial
├── rules.py      ← is_even, is_vowel, compute_expected_answer
├── scoring.py    ← apply_answer
├── generator.py  ← generatore trial con seed
├── ui.py         ← rendering pygame
├── tests/        ← test pytest
└── docs/         ← documentazione
```

I moduli `rules.py`, `scoring.py`, `generator.py`, `models.py` **non importano pygame**: sono logica pura e testabile.

## Test

```bash
pytest tests/
```

## Autori

- [Nome 1]
- [Nome 2]

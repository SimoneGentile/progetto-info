# Devlog — Brain Shift

## Settimana 1

**Giorno 1** — Setup del repository, struttura cartelle, primo commit con i file vuoti. Abbiamo letto la specifica e pianificato il lavoro.

**Giorno 2** — Scritto `rules.py` con `is_even`, `is_vowel` e `compute_expected_answer`. Lanciato `pytest tests/test_rules.py`: tutto verde al primo tentativo (quasi — avevamo sbagliato le vocali, mancava la U).

**Giorno 3** — Definita la `dataclass Trial` in `models.py`. Capito come funzionano i default nei campi.

## Settimana 2

**Giorno 4** — Scritto `generator.py`. Abbiamo avuto difficoltà con il seed: all'inizio usavamo `random.choice` direttamente, poi abbiamo capito che bisogna passare l'oggetto `rng` da fuori.

**Giorno 5** — Scritto `scoring.py` e passato tutti i test di `test_scoring_base.py`. Deciso di usare 0 punti per risposta errata (niente penalità).

**Giorno 6** — Prima finestra pygame. Solo finestra nera, ma funziona. Aggiunto il loop base con gestione della chiusura.

## Settimana 3

**Giorno 7** — Disegnata la carta con `draw_card()` in `ui.py`. Ci sono volute molte prove per centrare bene lettera e numero.

**Giorno 8** — Aggiunto l'input da tastiera. Il gioco è già giocabile, anche senza feedback visivo.

**Giorno 9** — Aggiunto il timer a 60 secondi e la schermata risultati. Implementato il feedback verde/rosso senza usare `pygame.time.wait`.

## Settimana 4

**Giorno 10** — Aggiunto l'HUD (punteggio, timer, contatori). Pulito il codice, aggiunto il fading delle istruzioni.

**Giorno 11** — Documentazione e README. Verifica finale: `pytest tests/` tutto verde, `python main.py` funziona da clone pulito.

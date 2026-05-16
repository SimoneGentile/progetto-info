# Architettura del progetto

## Separazione logica / pygame

Il principio fondamentale dell'architettura è la **separazione tra logica e presentazione**:

| Modulo | Importa pygame? | Descrizione |
|--------|-----------------|-------------|
| `models.py`    | ❌ No | Struttura dati `Trial` |
| `rules.py`     | ❌ No | Regole del gioco (is_even, is_vowel) |
| `scoring.py`   | ❌ No | Calcolo punteggio |
| `generator.py` | ❌ No | Generazione trial casuali |
| `config.py`    | ❌ No | Costanti |
| `ui.py`        | ✅ Sì | Rendering (carta, HUD, risultati) |
| `main.py`      | ✅ Sì | Loop principale, gestione eventi |

## Macchina a stati

```
PLAYING ──(timer scaduto)──→ RESULTS
RESULTS ──(premi R)────────→ PLAYING
```

## Flusso di un trial

1. `generate_trial(rng)` crea il trial
2. `draw_card()` lo disegna sullo schermo
3. Il giocatore preme una freccia
4. `apply_answer()` aggiorna il punteggio
5. Feedback visivo (verde/rosso) per 150ms
6. Vai al prossimo trial

## Seed e riproducibilità

Il generatore accetta un oggetto `random.Random` con un seed configurabile. Lo stesso seed produce sempre la stessa sequenza di trial. Questo permette di testare il generatore e di avere partite riproducibili.

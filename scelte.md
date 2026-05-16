# Scelte implementative

## Scoring: 0 punti per risposta errata

Abbiamo scelto di non penalizzare le risposte errate (0 punti, non -5). Motivazione: il gioco è già abbastanza stressante con il timer, una penalità renderebbe frustrante chi è alle prime armi. Il valore è configurabile in `config.py` → `POINTS_WRONG`.

## Seed iniziale fisso (42) poi casuale

La prima partita usa seed 42 (per debug e test). Dal secondo rigioco in poi il seed è casuale (`random.Random()` senza argomenti), così ogni partita è diversa.

## Feedback 150ms

Abbiamo scelto 150ms come durata del feedback (configurabile in `FEEDBACK_DURATION`). Meno di 100ms non si vede quasi, più di 200ms rallenta troppo il ritmo.

## Istruzioni che scompaiono dopo 10 corrette

Soglia scelta: 10 risposte corrette (configurabile in `INSTRUCTIONS_HIDE_AFTER`). Abbastanza per imparare le regole, non così tante da tenere le istruzioni per tutta la partita.

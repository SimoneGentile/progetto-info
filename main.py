
# main.py
# Punto di partenza del gioco. Gestisce:
#   - inizializzazione pygame
#   - macchina a stati: PLAYING → RESULTS
#   - loop principale con eventi, logica, rendering

import sys
import time
import random

import pygame

import config as c
from generator import generate_trial
from scoring import apply_answer
import ui


# ------------------------------------------------------------------ reset

def new_game(rng):
    """
    Resetta tutto lo stato per una nuova partita.
    Restituisce un dizionario con lo stato iniziale.
    """
    return {
        "state":          "PLAYING",
        "score":          0,
        "correct":        0,
        "wrong":          0,
        "start_time":     None,       # parte al primo trial
        "trial":          generate_trial(rng),
        "feedback_color": None,       # None / c.GREEN / c.RED
        "feedback_until": 0,          # timestamp fine feedback
        "waiting":        False,      # True durante il feedback
    }


# ------------------------------------------------------------------ main

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pygame.display.set_caption(c.TITLE)
    clock = pygame.time.Clock()
    fonts = ui.load_fonts()

    # Oggetto random con seed: cambia il numero per avere partite diverse
    # ma la stessa sequenza è sempre riproducibile con lo stesso seed.
    rng = random.Random(42)

    game = new_game(rng)

    # ---------------------------------------------------------------- loop
    while True:
        now = time.time()

        # ----- eventi -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # ESC chiude sempre
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Schermata risultati: R per rigiocare
                if game["state"] == "RESULTS":
                    if event.key == pygame.K_r:
                        rng = random.Random()   # nuovo seed casuale
                        game = new_game(rng)

                # In gioco: frecce
                elif game["state"] == "PLAYING" and not game["waiting"]:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        user_ans = (event.key == pygame.K_RIGHT)

                        # Avvia il timer al primo input
                        if game["start_time"] is None:
                            game["start_time"] = now

                        trial = game["trial"]
                        trial.user_answer = user_ans
                        trial.is_correct  = (user_ans == trial.expected_answer)

                        # Aggiorna punteggio e contatori
                        game["score"] = apply_answer(game["score"],
                                                     trial.is_correct)
                        if trial.is_correct:
                            game["correct"] += 1
                        else:
                            game["wrong"] += 1

                        # Avvia feedback visivo
                        game["feedback_color"] = (
                            c.GREEN if trial.is_correct else c.RED)
                        game["feedback_until"] = now + c.FEEDBACK_DURATION
                        game["waiting"] = True

        # ----- logica -----
        if game["state"] == "PLAYING":

            # Fine feedback → prossimo trial
            if game["waiting"] and now >= game["feedback_until"]:
                game["waiting"]        = False
                game["feedback_color"] = None
                game["trial"]          = generate_trial(rng)

            # Controlla timer (solo se la partita è iniziata)
            if game["start_time"] is not None:
                elapsed = now - game["start_time"]
                if elapsed >= c.GAME_DURATION:
                    game["state"] = "RESULTS"

        # ----- rendering -----
        screen.fill(c.BG_COLOR)

        if game["state"] == "PLAYING":
            # Calcola tempo rimasto
            if game["start_time"] is None:
                time_left = c.GAME_DURATION
            else:
                time_left = max(0, c.GAME_DURATION -
                                (now - game["start_time"]))

            ui.draw_card(screen, game["trial"], fonts,
                         feedback_color=game["feedback_color"])
            ui.draw_hud(screen, game["score"], time_left,
                        game["correct"], game["wrong"], fonts)
            ui.draw_controls(screen, fonts)

            # Istruzioni: scompaiono dopo INSTRUCTIONS_HIDE_AFTER corrette
            if game["correct"] < c.INSTRUCTIONS_HIDE_AFTER:
                ui.draw_instructions(screen, fonts)

        elif game["state"] == "RESULTS":
            ui.draw_results(screen, game["score"],
                            game["correct"], game["wrong"], fonts)

        pygame.display.flip()
        clock.tick(c.FPS)


if __name__ == "__main__":
    main()

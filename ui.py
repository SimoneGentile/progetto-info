# ui.py
# Tutto il rendering del gioco: carta, HUD, schermata risultati.
# Questo file USA pygame (è l'unico modulo insieme a main.py che lo fa).

import pygame
import config as c


# ------------------------------------------------------------------ helpers

def draw_rounded_rect(surface, color, rect, radius):
    """Disegna un rettangolo con angoli arrotondati."""
    pygame.draw.rect(surface, color, rect, border_radius=radius)


def center_text(surface, text, font, color, cx, cy):
    """Disegna testo centrato in (cx, cy)."""
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(cx, cy))
    surface.blit(rendered, rect)


# ------------------------------------------------------------------ card

def draw_card(surface, trial, fonts, feedback_color=None):
    """
    Disegna la carta del trial corrente.
    feedback_color: None = colore normale, altrimenti verde o rosso.
    """
    # Calcola la Y in base alla posizione
    if trial.position == "TOP":
        card_y = c.CARD_Y_TOP
        label  = "▲  numero pari?"
    else:
        card_y = c.CARD_Y_BOTTOM
        label  = "▼  lettera vocale?"

    rect = pygame.Rect(c.CARD_X, card_y, c.CARD_WIDTH, c.CARD_HEIGHT)

    # Sfondo carta
    bg = feedback_color if feedback_color else c.CARD_COLOR
    draw_rounded_rect(surface, bg, rect, c.CARD_RADIUS)

    # Bordo
    border_color = c.CARD_BORDER if not feedback_color else bg
    pygame.draw.rect(surface, border_color, rect,
                     width=2, border_radius=c.CARD_RADIUS)

    # Lettera (sinistra) e numero (destra)
    cx = c.CARD_X + c.CARD_WIDTH // 2
    cy = card_y + c.CARD_HEIGHT // 2

    letter_surf = fonts["big"].render(trial.letter, True, c.TEXT_DARK)
    number_surf = fonts["big"].render(str(trial.number), True, c.TEXT_DARK)

    lw = letter_surf.get_width()
    nw = number_surf.get_width()

    # Lettera a sinistra, numero a destra (con un po' di spazio)
    surface.blit(letter_surf, (cx - lw - 20, cy - letter_surf.get_height() // 2))
    surface.blit(number_surf, (cx + 20, cy - number_surf.get_height() // 2))

    # Etichetta sotto/sopra la carta (piccola, grigia)
    label_y = card_y - 22 if trial.position == "TOP" else card_y + c.CARD_HEIGHT + 6
    lbl = fonts["tiny"].render(label, True, c.GRAY)
    surface.blit(lbl, (c.CARD_X, label_y))


# ------------------------------------------------------------------ HUD

def draw_hud(surface, score, time_left, correct, wrong, fonts):
    """Disegna il HUD in alto: punteggio, timer, contatori."""
    # Timer al centro in alto
    timer_text = f"{int(time_left):02d}"
    color = c.RED if time_left <= 10 else c.YELLOW
    center_text(surface, timer_text, fonts["big"], color,
                c.SCREEN_WIDTH // 2, 28)

    # Punteggio a sinistra
    score_text = f"Score: {score}"
    s = fonts["small"].render(score_text, True, c.TEXT_LIGHT)
    surface.blit(s, (20, 10))

    # Corrette / sbagliate a destra
    stats = f"✓ {correct}   ✗ {wrong}"
    st = fonts["small"].render(stats, True, c.GRAY)
    surface.blit(st, (c.SCREEN_WIDTH - st.get_width() - 20, 10))


# ------------------------------------------------------------------ istruzioni

def draw_instructions(surface, fonts, opacity=255):
    """
    Mostra le due regole sullo schermo.
    opacity: 255 = completamente visibile, 0 = invisibile.
    """
    if opacity <= 0:
        return

    color = (min(255, c.GRAY[0]), min(255, c.GRAY[1]), min(255, c.GRAY[2]))

    top_text = fonts["tiny"].render(
        "CARTA IN ALTO  →  il numero è pari?", True, color)
    bot_text = fonts["tiny"].render(
        "CARTA IN BASSO →  la lettera è vocale?", True, color)

    # Testo vicino alle due posizioni delle carte
    surface.blit(top_text, (c.CARD_X, c.CARD_Y_TOP + c.CARD_HEIGHT + 8))
    surface.blit(bot_text, (c.CARD_X, c.CARD_Y_BOTTOM - 22))


# ------------------------------------------------------------------ controlli

def draw_controls(surface, fonts):
    """Mostra i controlli in basso al centro."""
    text = fonts["tiny"].render(
        "←  NO      →  SÌ", True, c.GRAY)
    x = c.SCREEN_WIDTH // 2 - text.get_width() // 2
    surface.blit(text, (x, c.SCREEN_HEIGHT - 28))


# ------------------------------------------------------------------ results

def draw_results(surface, score, correct, wrong, fonts):
    """Disegna la schermata dei risultati."""
    total = correct + wrong
    accuracy = (correct / total * 100) if total > 0 else 0

    # Titolo
    center_text(surface, "FINE PARTITA", fonts["huge"], c.YELLOW,
                c.SCREEN_WIDTH // 2, 120)

    # Punteggio
    center_text(surface, f"Punteggio: {score}", fonts["big"], c.WHITE,
                c.SCREEN_WIDTH // 2, 220)

    # Statistiche
    center_text(surface, f"Corrette: {correct}    Sbagliate: {wrong}",
                fonts["medium"], c.TEXT_LIGHT,
                c.SCREEN_WIDTH // 2, 300)

    center_text(surface, f"Accuratezza: {accuracy:.0f}%",
                fonts["medium"], c.GREEN if accuracy >= 70 else c.RED,
                c.SCREEN_WIDTH // 2, 350)

    # Istruzioni per rigiocare
    center_text(surface, "Premi  R  per rigiocare", fonts["small"], c.GRAY,
                c.SCREEN_WIDTH // 2, 450)
    center_text(surface, "Premi  ESC  per uscire", fonts["tiny"], c.GRAY,
                c.SCREEN_WIDTH // 2, 490)


# ------------------------------------------------------------------ font loader

def load_fonts():
    """
    Carica tutti i font usati nel gioco.
    Restituisce un dizionario: {"huge": ..., "big": ..., ...}
    """
    return {
        "huge":   pygame.font.SysFont("Arial", c.FONT_HUGE,   bold=True),
        "big":    pygame.font.SysFont("Arial", c.FONT_BIG,    bold=True),
        "medium": pygame.font.SysFont("Arial", c.FONT_MEDIUM),
        "small":  pygame.font.SysFont("Arial", c.FONT_SMALL),
        "tiny":   pygame.font.SysFont("Arial", c.FONT_TINY),
    }

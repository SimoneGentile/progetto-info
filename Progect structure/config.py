# config.py
# Tutte le costanti del gioco: colori, dimensioni, timing, punteggi.
# Modifica questi valori per cambiare l'aspetto del gioco.

# --- Finestra ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "Brain Shift"

# --- Colori (R, G, B) ---
WHITE       = (255, 255, 255)
BLACK       = (10,  10,  10)
BG_COLOR    = (20,  20,  35)      # sfondo scuro
CARD_COLOR  = (255, 255, 255)
CARD_BORDER = (180, 180, 200)
TEXT_DARK   = (30,  30,  50)
TEXT_LIGHT  = (220, 220, 240)
GRAY        = (140, 140, 160)

GREEN       = (60,  200, 100)
RED         = (220, 70,  70)
YELLOW      = (255, 210, 60)
BLUE        = (80,  140, 255)
PURPLE      = (160, 80,  220)

# --- Carta ---
CARD_WIDTH  = 220
CARD_HEIGHT = 140
CARD_RADIUS = 14      # angoli arrotondati

# Posizione orizzontale: centrata
CARD_X = SCREEN_WIDTH // 2 - CARD_WIDTH // 2

# Y per TOP e BOTTOM
CARD_Y_TOP    = 60
CARD_Y_BOTTOM = SCREEN_HEIGHT - CARD_HEIGHT - 60

# --- Timer di gioco ---
GAME_DURATION = 60    # secondi

# --- Scoring ---
POINTS_CORRECT = 10
POINTS_WRONG   = 0    # scegli 0 oppure -5

# --- Feedback visivo ---
FEEDBACK_DURATION = 0.15   # secondi: quanto resta verde/rosso la carta

# --- Fading istruzioni ---
INSTRUCTIONS_HIDE_AFTER = 10   # dopo N risposte corrette le istruzioni spariscono

# --- Font sizes ---
FONT_HUGE   = 72
FONT_BIG    = 48
FONT_MEDIUM = 32
FONT_SMALL  = 22
FONT_TINY   = 16

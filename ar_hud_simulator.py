import pygame
import sys

pygame.init()

# Your original dimensions (exact size of each transparent OLED)
LSCREEN_X = 128
SCREEN_Y = 64
RSCREEN_X = 128
RSCREEN_Y = 64

FEMBOY_PINK     = (255, 102, 166)   # #FF66A6  ← main one
SOFT_FEMBOY     = (255, 153, 156)   # #FF999C  softer & cuter
PASTEL_FEMBOY   = (255, 192, 203)   # #FFC0CB  classic baby pink
BRIGHT_FEMBOY   = (255, 112, 146)   # #FF7092  super vibrant
DEEP_FEMBOY     = (207,  98, 169)   # #CF62A9  richer magenta-pink
NEON_FEMBOY     = (255,  20, 147)   # #FF1493  hot neon version


# Main window = Left Eye + Right Eye side-by-side
main_width = LSCREEN_X + RSCREEN_X   # 256
main_height = SCREEN_Y               # 64
CHOSEN_COLOR = FEMBOY_PINK
screen = pygame.display.set_mode((main_width, main_height))
pygame.display.set_caption("PROTOTYPE")

# Two completely separate surfaces (your "eyes")
left_eye_surface  = pygame.Surface((LSCREEN_X, SCREEN_Y))
right_eye_surface = pygame.Surface((RSCREEN_X, SCREEN_Y))

# Simple fonts
font = pygame.font.SysFont("consolas", 8, bold=True)

running = True

def bar(float temp):
    pyxels = 60
    #bar mins and max are temp+20 for simplicity
    rock = temp + 20
    num_bars = int((60/140)*rock)

    bar_min = 0
    bar_max = 140

    return num_bars

    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === LEFT EYE (completely independent) ===
    left_eye_surface.fill((0, 0, 0))
    left_text = font.render("LEFT EYE", True, FEMBOY_PINK)
    left_eye_surface.blit(left_text, (0, 0))

    # === RIGHT EYE (completely independent) ===
    right_eye_surface.fill((0, 0, 0))
    right_text = font.render("RIGHT EYE", True, FEMBOY_PINK)
    right_eye_surface.blit(right_text, (0, 0))

    # Blit both eyes onto the main window
    screen.blit(left_eye_surface, (0, 0))                    # left eye on left
    screen.blit(right_eye_surface, (LSCREEN_X, 0))           # right eye on right

    # Divider line (just like the bridge of your glasses)
    pygame.draw.line(screen, (90, 90, 90), (128, 0), (128, 64), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()
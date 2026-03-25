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
sprites = []
num_spritess = 0
def load_sprite(path):
    temp_sprite = pygame.image.load(path).convert_alpha()
    num_spritess += 1
    sprites.append(temp_sprite)

    #No terminal for glasses
    #there is no fail!
        
# Two completely separate surfaces (your "eyes")
left_eye_surface  = pygame.Surface((LSCREEN_X, SCREEN_Y))
right_eye_surface = pygame.Surface((RSCREEN_X, SCREEN_Y))

# Simple fonts
font = pygame.font.SysFont("consolas", 8, bold=True)

running = True

def get_temp_bar_infill(temp: float):
    """Returns 0–60 pixels to fill from the BOTTOM up. Perfect for -20°C → 120°C."""
    MIN_TEMP = -20.0

    MAX_TEMP = 120.0

    clamped = max(MIN_TEMP, min(MAX_TEMP, temp))
    fill_ratio = (clamped - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)

    return int(fill_ratio * 60)

def draw_temp_bar(surface, temp: float, base_x: int = 92, base_y: int = 2):
    surface.blit(sprites[0], (base_x, base_y))

    fill_px = get_temp_bar_infill(temp)
    if fill_px <= 0:
        
        pass

    
    INNER_LEFT   = 4      # left edge of the empty interior
    INNER_TOP    = 8      # top edge of the empty interior (after the 120 label)
    INNER_WIDTH  = 22     # width of the fill zone (your two-column area)
    INNER_MAX_H  = 60     # exactly the 60 pyxels you said are available

    fill_rect = pygame.Rect(
        base_x + INNER_LEFT,
        base_y + INNER_TOP + INNER_MAX_H - fill_px,
        INNER_WIDTH,
        fill_px
    )
    pygame.draw.rect(surface, CHOSEN_COLOR, fill_rect)   # hot FEMBOY_PINK infill

    temp_text = font.render(f"{temp:.0f}°C", True, CHOSEN_COLOR)
    surface.blit(temp_text, (base_x + 2, base_y + INNER_TOP + INNER_MAX_H + 5))
def get_temp():
    #will be implemented with temp sensor soon! until then its sunny and 75 degrees!
    return 75
def get_compass_angle():
    #will return north for now(90)
    return 90

def init():
    load_sprite("/SPRITES/TEMP_BAR.ase") # 1
    draw_temp_bar(right_eye_surface,get_temp(),64,0)

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
    init()




pygame.quit()
sys.exit()
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 854, 480
BG_COLOR = (26, 17, 16)  # Dark background color
PANEL_COLOR = (60, 60, 60)  # Gray panel color
TEXT_COLOR = (255, 255, 255)  # White color for text
BUTTON_COLOR = (100, 100, 100)  # Grey color for the button
BUTTON_HOVER_COLOR = (130, 130, 130)  # Lighter grey for button hover
FONT_NAME = 'timesnewroman'  # Default font

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CAVE GAME ULTRA LAUNCHER 1.0')

# Function to draw text
def draw_text(text, font_name, size, color, x, y, center=True):
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.midtop = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing background
    screen.fill(BG_COLOR)

    # Drawing the panel
    panel_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100, 300, 200)
    pygame.draw.rect(screen, PANEL_COLOR, panel_rect)

    # Drawing text fields and labels
    draw_text('Username:', FONT_NAME, 20, TEXT_COLOR, panel_rect.x + 10, panel_rect.y + 20, center=False)
    draw_text('Password:', FONT_NAME, 20, TEXT_COLOR, panel_rect.x + 10, panel_rect.y + 70, center=False)

    # Drawing the login button
    login_button = pygame.Rect(panel_rect.x + 10, panel_rect.y + 150, panel_rect.width - 20, 30)
    if login_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, login_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, login_button)
    draw_text('Login', FONT_NAME, 20, TEXT_COLOR, login_button.centerx, login_button.centery - 10)

    # Drawing the title
    draw_text('CAVE GAME ULTRA LAUNCHER 1.0', FONT_NAME, 24, TEXT_COLOR, SCREEN_WIDTH // 2, 20)

    # Update the display
    pygame.display.update()

pygame.quit()

'''
Personal project to practice python and pygame.
by ppericas
'''
# ----------------------------------------------------------------------------------------------------------------------
# imports
import pygame
import os

pygame.init()

# ----------------------------------------------------------------------------------------------------------------------
# constants
# window
WIDTH, HEIGHT = 340, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe')

# colors
WHITE = (255, 255, 255)

# sizes
BUTTON_WIDTH, BUTTON_HEIGHT = 133, 37

# menu buttons
PLAY_X = QUIT_X = 107
PLAY_Y, QUIT_Y = 287, 340

# play buttons
MENU_Y = QUIT_QUIT_Y = 128
MENU_X, QUIT_QUIT_X,  = 27, 181

# images
START_MENU_IMAGE = pygame.image.load(
    os.path.join('assets', 'start_menu.png'))
START_MENU = pygame.transform.scale(START_MENU_IMAGE, (WIDTH, HEIGHT))

PLAY_MENU_IMAGE = pygame.image.load(
    os.path.join('assets', 'play_menu.png'))
PLAY_MENU = pygame.transform.scale(PLAY_MENU_IMAGE, (WIDTH, HEIGHT))

PLAY_BUTTON = pygame.Rect(PLAY_X, PLAY_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
QUIT_BUTTON = pygame.Rect(QUIT_X, QUIT_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

MENU_BUTTON = pygame.Rect(MENU_X, MENU_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
QUIT_QUIT_BUTTON = pygame.Rect(
    QUIT_QUIT_X, QUIT_QUIT_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

PIECE_SIZE = 85

X_IMAGE = pygame.image.load(
    os.path.join('assets', 'x.png'))
X = pygame.transform.scale(X_IMAGE, (PIECE_SIZE, PIECE_SIZE))

O_IMAGE = pygame.image.load(
    os.path.join('assets', 'o.png'))
O = pygame.transform.scale(O_IMAGE, (PIECE_SIZE, PIECE_SIZE))

X_WON_IMAGE = pygame.image.load(
    os.path.join('assets', 'x_won.png'))
X_WON = pygame.transform.scale(X_WON_IMAGE, (BUTTON_WIDTH, BUTTON_HEIGHT))

O_WON_IMAGE = pygame.image.load(
    os.path.join('assets', 'o_won.png'))
O_WON = pygame.transform.scale(O_WON_IMAGE, (BUTTON_WIDTH, BUTTON_HEIGHT))

# sounds
victory_sound = pygame.mixer.Sound(
    os.path.join('assets', 'sounds', 'victory.wav'))

click_sound = pygame.mixer.Sound(
    os.path.join('assets', 'sounds', 'click.wav'))

# coordinate system for all possible positions
# uppercase letter for 'x', lowercase letter for 'y'


A, B, C = 27, 128, 229
a, b, c = 192, 292, 393

# others
FPS = 60
winner = None
X_TURN = 'X'
O_TURN = 'O'

storage = {
    'Aa': {
        'square': pygame.Rect(A, a, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Ba': {
        'square':pygame.Rect(B, a, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Ca': {
        'square':pygame.Rect(C, a, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Ab': {
        'square':pygame.Rect(A, b, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Bb': {
        'square':pygame.Rect(B, b, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Cb': {
        'square':pygame.Rect(C, b, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Ac': {
        'square':pygame.Rect(A, c, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Bc': {
        'square':pygame.Rect(B, c, PIECE_SIZE, PIECE_SIZE),
        'value': None
    },
    'Cc': {
        'square':pygame.Rect(C, c, PIECE_SIZE, PIECE_SIZE),
        'value': None
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# class & functions
def draw_window(menu, winner):
    WIN.blit(menu, (0, 0))
    if winner == X:
        WIN.blit(X_WON, ((WIDTH - BUTTON_WIDTH) // 2, 88))
    elif winner == O:
        WIN.blit(O_WON, ((WIDTH - BUTTON_WIDTH) // 2, 88))
    for keys in storage.values():
        if keys['value'] is not None:
            WIN.blit(keys['value'], keys['square'])
    pygame.display.update()

def win():
    # Verify columns
    for _ in range(3):
        if (storage[f'Aa']['value'] == storage[f'Ba']['value'] == storage[f'Ca']['value'] == X) or \
           (storage[f'Aa']['value'] == storage[f'Ba']['value'] == storage[f'Ca']['value'] == O):
            return storage[f'Aa']['value']

        if (storage[f'Ab']['value'] == storage[f'Bb']['value'] == storage[f'Cb']['value'] == X) or \
           (storage[f'Ab']['value'] == storage[f'Bb']['value'] == storage[f'Cb']['value'] == O):
            return storage[f'Ab']['value']

        if (storage[f'Ac']['value'] == storage[f'Bc']['value'] == storage[f'Cc']['value'] == X) or \
           (storage[f'Ac']['value'] == storage[f'Bc']['value'] == storage[f'Cc']['value'] == O):
            return storage[f'Ac']['value']

    # Verify rows
    for _ in range(3):
        if (storage[f'Aa']['value'] == storage[f'Ab']['value'] == storage[f'Ac']['value'] == X) or \
           (storage[f'Aa']['value'] == storage[f'Ab']['value'] == storage[f'Ac']['value'] == O):
            return storage[f'Aa']['value']

        if (storage[f'Ba']['value'] == storage[f'Bb']['value'] == storage[f'Bc']['value'] == X) or \
           (storage[f'Ba']['value'] == storage[f'Bb']['value'] == storage[f'Bc']['value'] == O):
            return storage[f'Ba']['value']

        if (storage[f'Ca']['value'] == storage[f'Cb']['value'] == storage[f'Cc']['value'] == X) or \
           (storage[f'Ca']['value'] == storage[f'Cb']['value'] == storage[f'Cc']['value'] == O):
            return storage[f'Ca']['value']

    # Verify diagonals
    if (storage[f'Aa']['value'] == storage[f'Bb']['value'] == storage[f'Cc']['value'] == X) or \
       (storage[f'Aa']['value'] == storage[f'Bb']['value'] == storage[f'Cc']['value'] == O):
        return storage[f'Aa']['value']

    if (storage[f'Ac']['value'] == storage[f'Bb']['value'] == storage[f'Ca']['value'] == X) or \
       (storage[f'Ac']['value'] == storage[f'Bb']['value'] == storage[f'Ca']['value'] == O):
        return storage[f'Ac']['value']

    return None




# ----------------------------------------------------------------------------------------------------------------------
# main function
def main():
    clock = pygame.time.Clock()
    run = True
    menu = START_MENU
    turn = X_TURN
    winner = None

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu == START_MENU:
                    if PLAY_BUTTON.collidepoint(event.pos):
                        menu = PLAY_MENU
                    elif QUIT_BUTTON.collidepoint(event.pos):
                        run = False
                elif menu == PLAY_MENU:
                    if MENU_BUTTON.collidepoint(event.pos):
                        for keys in storage.values():
                            if keys['value'] is not None:
                                keys['value'] = None
                        winner = None
                        menu = START_MENU
                    elif QUIT_QUIT_BUTTON.collidepoint(event.pos):
                        run = False

                    elif storage['Aa']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Aa']['value'] = X if turn == X_TURN else O

                    elif storage['Ba']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Ba']['value'] = X if turn == X_TURN else O

                    elif storage['Ca']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Ca']['value'] = X if turn == X_TURN else O

                    elif storage['Ab']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Ab']['value'] = X if turn == X_TURN else O

                    elif storage['Bb']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Bb']['value'] = X if turn == X_TURN else O

                    elif storage['Cb']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Cb']['value'] = X if turn == X_TURN else O

                    elif storage['Ac']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Ac']['value'] = X if turn == X_TURN else O

                    elif storage['Bc']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Bc']['value'] = X if turn == X_TURN else O

                    elif storage['Cc']['square'].collidepoint(event.pos):
                        turn = X_TURN if turn == O_TURN else O_TURN
                        storage['Cc']['value'] = X if turn == X_TURN else O

                    click_sound.play()
                    winner_piece = win()
                    if winner_piece is not None:
                        victory_sound.play()
                        winner = X if winner_piece == X else O


        draw_window(menu, winner)

    pygame.quit()


if __name__ == '__main__':
    main()
import pygame
pygame.init()  # Initialize all imported pygame modules

# Load images for animations
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')  # Load background image
# Load character image for standing position
char = pygame.image.load('standing.png')

# Game window setup
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

# Character initial position and properties
x = 50
y = 400
width = 40
height = 60
vel = 5

# Time control for animation frame rate
clock = pygame.time.Clock()

# Variables for character state
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

# Function to redraw the game window


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))  # Draw background

    if walkCount + 1 >= 27:  # Check if animation frame needs to reset
        walkCount = 0

    if left:  # Animation for walking left
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:  # Animation for walking right
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:  # Character is standing
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()  # Update the display


# Main game loop
run = True
while run:
    clock.tick(27)  # Maintain a consistent frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # Check pressed keys

    # Movement and animation logic
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    # Jump logic
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5  # Parabolic jump
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()  # Redraw the window with updated positions and frames

pygame.quit()  # Quit the game when the loop ends

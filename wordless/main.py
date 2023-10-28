import pygame
import sys
import random

# List of words and corresponding hints
word_list = [("apple", "A fruit"), ("banana", "A yellow fruit"), ("cherry", "A red fruit"), ("date", "A sweet fruit")]

# Select a random word and hint to guess
word_to_guess, hint = random.choice(word_list)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("worde.py")

# Load background image
background = pygame.image.load("background.jpg")  # Replace with your background image path
background = pygame.transform.scale(background, (screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fonts
word_font = pygame.font.Font("your_font.ttf", 48)  # Replace with your font file path
hint_font = pygame.font.Font("your_font.ttf", 24)

# Word state
guessed_word = [""] * len(word_to_guess)

# Hints
show_hint = False  # Flag to display hint

# Calculate the size of each square
square_size = 60
start_x = (screen_width - (len(word_to_guess) * square_size)) / 2
start_y = 200

# Main game loop
running = True
attempts = 5

# Create Hint button
hint_button = pygame.Rect(screen_width - 150, screen_height - 50, 140, 40)
hint_button_text = hint_font.render("Hint", True, WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key)
                if letter in word_to_guess:
                    for i, char in enumerate(word_to_guess):
                        if char == letter and guessed_word[i] != letter:
                            guessed_word[i] = letter
                            if "".join(guessed_word) == word_to_guess:
                                print("You win!")
                                running = False
                else:
                    attempts -= 1
                    if attempts == 0:
                        print("You lose!")
                        running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hint_button.collidepoint(event.pos):
                show_hint = not show_hint

    # Clear the screen with the background image
    screen.blit(background, (0, 0))

    # Draw the word squares and guessed letters
    for i in range(len(word_to_guess)):
        pygame.draw.rect(screen, WHITE, (start_x + i * square_size, start_y, square_size, square_size))
        if guessed_word[i] == word_to_guess[i]:
            pygame.draw.rect(screen, GREEN, (start_x + i * square_size, start_y, square_size, square_size))
            text = word_font.render(guessed_word[i], True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (start_x + i * square_size + square_size // 2, start_y + square_size // 2)
            screen.blit(text, text_rect)
        elif guessed_word[i] != "":
            pygame.draw.rect(screen, YELLOW, (start_x + i * square_size, start_y, square_size, square_size))
            text = word_font.render(guessed_word[i], True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (start_x + i * square_size + square_size // 2, start_y + square_size // 2)
            screen.blit(text, text_rect)

    # Draw Hint button
    pygame.draw.rect(screen, (0, 128, 255), hint_button)
    screen.blit(hint_button_text, (screen_width - 140, screen_height - 40))

    # Draw hint if requested
    if show_hint:
        hint_text = hint_font.render("Hint: " + hint, True, BLACK)
        hint_text_rect = hint_text.get_rect()
        hint_text_rect.center = (screen_width // 2, 400)
        screen.blit(hint_text, hint_text_rect)

    # Draw attempts left
    attempts_text = hint_font.render(f"Attempts left: {attempts}", True, BLACK)
    screen.blit(attempts_text, (100, 500))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

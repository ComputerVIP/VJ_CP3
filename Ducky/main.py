import pygame
import keyboard
import mouse

# Initialize pygame mixer
pygame.mixer.init()

# Load the duck sound
duck_sound = pygame.mixer.Sound("Ducky/Ducky_Sound.wav")  # Use forward slash or double backslash

def play_duck_sound():
    duck_sound.play()
    
def play_duck_sound_on_key_press(event):
    if event.event_type == 'down':  # Only play on key down
        play_duck_sound()

# Listen for all key presses globally
keyboard.on_press(play_duck_sound_on_key_press)
mouse.on_click(play_duck_sound)

print("Press any key for a duck quack! (Press ESC to quit)")
keyboard.wait('esc')
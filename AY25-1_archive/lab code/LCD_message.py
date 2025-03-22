import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
import time
from adafruit_circuitplayground import cp
import random

# Initialize the TFT Gizmo display
def create_display():
    # Initialize and return the TFT Gizmo display object
    display = tft_gizmo.TFT_Gizmo()
    return display

# Create the text display for A or B or other messages like ":)", ":(" or "?"
def show_text(display, message):
    # Create a group to hold display elements
    splash = displayio.Group()

    # Create a black background for the display
    color_bitmap = displayio.Bitmap(240, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000  # Black background

    # Create a TileGrid for the background and add it to the group
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)
    
    # Position text based on whether it's 'A' or 'B' or another message
    if message == "A":
        x_pos = 160  # Display 'A' on the right side of the screen
    elif message == "B":
        x_pos = 40   # Display 'B' on the left side of the screen
    else:
        x_pos = 100  # Default position for "?", ":)", ":(", etc. (centered)
 
    # Create a text label to show the message (A or B) on the display
    text_group = displayio.Group(scale=10, x=x_pos, y=90)  # Text size and position
    text_area = label.Label(terminalio.FONT, text=message, color=0xFFFFFF)  # White text
    text_group.append(text_area)
    splash.append(text_group)

    # Show the group on the display and refresh the screen
    display.show(splash)
    display.refresh()

# Wait for player input and return 'A' or 'B' based on button press
def get_player_input(display):
    # Display "?" in the middle of the screen while waiting for input
    show_text(display, "?")
    
    # Loop until the player presses a button
    while True:
        if cp.button_a:  # Check if button A is pressed
            print("Button A pressed")
            time.sleep(0.01)  # Short pause to debounce the button
            return "A"  # Return 'A' for button A press

        if cp.button_b:  # Check if button B is pressed
            print("Button B pressed")
            time.sleep(0.01)  # Short pause to debounce the button
            return "B"  # Return 'B' for button B press

        time.sleep(0.01)  # Small delay

# Show the sequence of A's and B's
def show_sequence(display, sequence):
    # Loop through each item in the sequence
    for item in sequence:
        show_text(display, item)  # Show the current item (A or B)
        time.sleep(0.25)  # Pause to display it
        show_text(display, "")  # Clear the display (show nothing)
        time.sleep(0.1)  # Pause between letters

# Main game logic
def main():
    display = create_display()  # Initialize the TFT display
    sequence = []  # Empty sequence to start the game
    max_length = 10  # Maximum sequence length

    # Start the game loop
    while len(sequence) < max_length:
        # Add a random 'A' or 'B' to the sequence
        sequence += [random.choice(["A", "B"])]
        
        # Show the updated sequence to the player
        show_sequence(display, sequence)
        
        # Print the current sequence to the console for debugging
        print("Sequence:", sequence)

        # Check the player's input for each item in the sequence
        for i in range(len(sequence)):
            player_input = get_player_input(display)  # Show "?" while waiting and get player's button press
            print("Player pressed:", player_input)
            
            # If player input does not match the sequence, display ":(" and end the game
            if player_input != sequence[i]:
                show_text(display, ":(")  # Show "Game Over" on display
                print("Game Over! Player made a mistake.")
                # Keep the ":(" displayed on the screen indefinitely
                while True:
                    pass
                return  # End the game (this line won't be reached)

        # If the player got the sequence correct, show a success message for a short time
        show_text(display, ":)")
        time.sleep(1)  # Pause for 1 second before the next round

    # If the player completes all 8 rounds, display ":)" and keep it on the screen
    show_text(display, ":)")
    print("Congratulations! You win!")
    # Keep the ":)" displayed on the screen indefinitely
    while True:
        pass

# Start the game by calling the main function
main()

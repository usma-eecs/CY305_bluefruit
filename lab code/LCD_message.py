import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
import time

# Function to return the dictionary of ROYGBIV colors plus black and white
def get_color_map():
    return {
        "red": 0xFF0000,      # Red
        "orange": 0xFFA500,   # Orange
        "yellow": 0xFFFF00,   # Yellow
        "green": 0x00FF00,    # Green
        "blue": 0x0000FF,     # Blue
        "purple": 0x800080,   # Purple (for violet)
        "black": 0x000000,    # Black
        "white": 0xFFFFFF     # White
    }

# Create the TFT Gizmo display
def create_display():
    display = tft_gizmo.TFT_Gizmo()
    return display

def setup(message, position=(50, 100), text_color="yellow", background_color="black"):
    # Initialize display and create display group
    display = create_display()
    splash = displayio.Group()
    display.show(splash)

    # Get the color map
    color_map = get_color_map()

    # Convert background color name to hex value using the color map
    background_color_hex = color_map.get(background_color.lower(), 0x000000)  # Default to black if not found

    # Create a background with the specified color
    color_bitmap = displayio.Bitmap(240, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = background_color_hex  # Set background color

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Convert text color name to hex value using the color map
    text_color_hex = color_map.get(text_color.lower(), 0xFFFF00)  # Default to yellow if not found

    # Create the label for the message with a default scale of 10
    text_group = displayio.Group(scale=10, x=position[0], y=position[1])
    text_area = label.Label(terminalio.FONT, text=message, color=text_color_hex)
    text_group.append(text_area)
    splash.append(text_group)

    return display

def main():
    message = "Hi"               # Message to display
    position = (70, 100)          # Adjust this to change the position of the message
    text_color = "red"          # Set text color (e.g., "red", "blue", "white")
    background_color = "white"    # Set the background color (e.g., "red", "purple", "black")
    
    setup(message, position, text_color, background_color)

    # Infinite loop to keep the display active
    while True:
        pass

main()

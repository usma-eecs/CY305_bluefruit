import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
import time

def setup(background_color, text, text_color, text_scale, anchor_point):
    """
    Set up the TFT Gizmo display with the specified customizations.
    """
    # Initialize the TFT Gizmo display
    display = tft_gizmo.TFT_Gizmo()

    # Create the main display group
    splash = displayio.Group()
    display.show(splash)

    # Create a background bitmap and palette
    color_bitmap = displayio.Bitmap(240, 240, 1)  # 240x240 pixels
    color_palette = displayio.Palette(1)          # Single color palette
    color_palette[0] = background_color           # Set background color

    # Create and append the background sprite
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Create the text label with specified parameters
    text_area = label.Label(
        terminalio.FONT,
        text=text,
        color=text_color,
        scale=text_scale
    )

    # Set anchor_point and anchored_position to align the text
    text_area.anchor_point = anchor_point
    text_area.anchored_position = (display.width // 2, display.height // 2)

    # Append the text label to the main display group
    splash.append(text_area)

    return display, text_area

def customizations():
    """
    Define and return customization parameters.

    Students can modify the following parameters:
        - background_color: Color of the display background (hex format)
        - text: The string to display
        - text_color: Color of the text (hex format)
        - text_scale: Scaling factor for the text size
        - anchor_point: Defines the anchor point of the text
    """
 
    # Background color (e.g., 0x000000 for black, 0xFFFFFF for white)
    background_color = 0x000000  # Black
    
    # Text to display
    text = "Hi"  # Change to desired text, e.g., "Hi!", "Hello World!"
    
    # Text color (e.g., 0xFFFF00 for yellow, 0xFF0000 for red)
    text_color = 0xFFFF00  # Yellow
    
    # Text scaling factor (integer)
    text_scale = 10  # Adjust to make text larger or smaller
    
    # Anchor point for the text (tuple of floats between 0 and 1)
    # (0.5, 0.5) centers the text both horizontally and vertically
    anchor_point = (0.5, 0.5)
     
    return background_color, text, text_color, text_scale, anchor_point

def main():
    """
    Main function to set up the display and keep the program running.
    """
    # Retrieve customization parameters
    background_color, text, text_color, text_scale, anchor_point = customizations()
    
    # Set up the display with the retrieved customizations
    display, text_area = setup(background_color, text, text_color, text_scale, anchor_point)
    
    # Keep the program running to maintain the display
    while True:
        pass

# Execute the main function
main()
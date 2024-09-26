# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
import time

# Create the TFT Gizmo display
def create_display():
    display = tft_gizmo.TFT_Gizmo()
    return display

def setup(message):
    # Draw the gray background
    splash = displayio.Group()
    display = create_display()
    display.show(splash)

    color_bitmap = displayio.Bitmap(240, 240, 1) # Creates a 240x240 bitmap with 1 color
    color_palette = displayio.Palette(1) # Creates a color palette of one color
    color_palette[0] = 0xA9A9A9  # Assigns the color Gray to the color palette

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(200, 200, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
    splash.append(inner_sprite)

    # Draw a label
    text_group = displayio.Group(scale=3, x=30, y=100)

    text_area = label.Label(terminalio.FONT, text=message, color=0xFFD700)

    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

    return display, text_area

def main():
    messages = ["Go Army! \nBeat Navy!", "Beat \nAir Force!", "Beat \nEveryone!"]
    current_message_index = 0
    display, text_area = setup(messages[current_message_index])
    while True:
        current_message_index = (current_message_index + 1) % len(messages)
        text_area.text = messages[current_message_index]  # Update the label text

        display.refresh()  # Refresh the display to show the updated text
        time.sleep(2)  # Wait for 2 seconds before updating the text again

main()
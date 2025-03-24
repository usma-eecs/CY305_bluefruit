import displayio
from adafruit_gizmo import tft_gizmo

# Function to display an image
def display_image(display, bitmap):
    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    # Add the Group to the Display
    display.root_group = group

def main():
    # Initialize the display
    display = tft_gizmo.TFT_Gizmo()

    # Define the first bitmap
    bitmap1 = displayio.OnDiskBitmap("/EECS.bmp")

    # Display the first image (bitmap1)
    display_image(display, bitmap1)

    # Keep the program running to display the image
    # This loop prevents the program from exiting and turning off the display.
    while True:
        pass

main()
import displayio
from adafruit_gizmo import tft_gizmo

def display_image():
    display = tft_gizmo.TFT_Gizmo()
    # Setup the file as the bitmap data source
    bitmap = displayio.OnDiskBitmap("/EECS.bmp")

    # Create a TileGrid to hold the bitmap
    # Notice that you're using the variable bitmap in here twice!
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    # Add the Group to the Display
    display.show(group)

def main():
    display_image()

    # Keep the program running indefinitely to display the image
    # This loop prevents the program from exiting and turning off the display.
    while True:
        pass

main()
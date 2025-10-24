import time
import board
import adafruit_ble
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Set up the UART service
uart = UARTService()

# Create an advertisement
advertisement = ProvideServicesAdvertisement(uart)

# Start BLE radio
ble = adafruit_ble.BLERadio()
ble.name = "MyBluefruit" #change this to unique name
ble.start_advertising(advertisement)

while True:
    if ble.connected:
        print("Connected")
        while ble.connected:
            # Check if there is data available to be read
            if uart.in_waiting > 0:
                received_bytes = uart.read(uart.in_waiting)
                received = received_bytes.decode("utf-8").strip()
                print("Received:", received)
                
            time.sleep(0.1)  # Add a small delay to prevent a tight loop
    else:
        if not ble.advertising:
            print("Waiting for connection...")
            ble.start_advertising(advertisement)
        
    time.sleep(1)

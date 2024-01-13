import RPi.GPIO as GPIO
import time
import serial
from spotifyClass import SpotifyRequests

spotify = SpotifyRequests
# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for buttons
button_pins = [17, 22, 23, 24, 27]
czyleci = False
# Setup the serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Change '/dev/ttyS0' to your actual serial port


# Setup the GPIO pins for input with pull-up resistors
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Button Press Detection. Press Ctrl+C to exit.")
    
    while True:
        if GPIO.input(17) == GPIO.LOW:
            spotify.classInterface("skipToNextRequest")
            czyleci = True

        if GPIO.input(22) == GPIO.LOW:
            spotify.classInterface("skipToPreviousRequest")
            czyleci = True
        if GPIO.input(23) == GPIO.LOW:
            if czyleci == True:
                spotify.classInterface("stopRequest")
                czyleci = False
            else:
                spotify.classInterface("playRequest")
                czyleci = True

        if GPIO.input(24) == GPIO.LOW:
            print()
        if GPIO.input(27) == GPIO.LOW:
            print()
            
        serial_data = ser.readline().decode('utf-8').strip()
        if serial_data:
            print(f"Serial Data Received: {serial_data}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()

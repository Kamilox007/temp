import RPi.GPIO as GPIO
import time

# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for buttons
button_pins = [17, 22, 23, 24, 27]

# Setup the GPIO pins for input with pull-up resistors
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Button Press Detection. Press Ctrl+C to exit.")
    
    while True:
        for pin in button_pins:
            if GPIO.input(pin) == GPIO.LOW:
                print(f"Button on GPIO {pin} pressed.")
                time.sleep(0.2)  # debounce time

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()

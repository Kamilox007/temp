import RPi.GPIO as GPIO
import time

# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for buttons
button_pins = [17, 22, 23, 24, 27]

# Setup the serial port
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)  # Change '/dev/ttyS0' to your actual serial port


# Setup the GPIO pins for input with pull-up resistors
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Button Press Detection. Press Ctrl+C to exit.")
    
    while True:
        for pin in button_pins:
            if GPIO.input(pin) == GPIO.LOW:
                print(f"Button on GPIO {pin} pressed.")
                time.sleep(1)  # debounce time

        serial_data = ser.readline().decode('utf-8').strip()
        if serial_data:
            print(f"Serial Data Received: {serial_data}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()

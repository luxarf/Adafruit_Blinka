import sys
import time
from adafruit_blinka.agnostic import board as agnostic_board
import board
import digitalio

# from Adafruit_GPIO import Platform
# print("Platform = ", Platform.platform_detect(), Platform.pi_version())

print("hello blinka!")

print(
    "Found system type: %s (sys.plaform %s implementation %s) "
    % (agnostic_board, sys.platform, sys.implementation.name)
)

print("board contents: ", dir(board))


led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
    led.value = button.value
    time.sleep(0.1)

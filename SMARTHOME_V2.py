# Robbe De Budt
# 22/04/2020

# LIBRARIES
import time
import thread
from gpiozero import Button
from gpiozero import LED

# VARIABLES
system_enabled = True
SYSTEM_ESSENTIALS = {
    Button(12): LED(21),
    Button(24): LED(20),
    Button(23): LED(16),
    Button(18): LED(5)
}


def setup_button(button, LED):
    time_elapsed = 0
    button_pressed = 0

    while True:
        time_elapsed = 0

        if button.value == 1:
            # Button has been pressed.
            # Do stuff if button has been pressed.

            startTick = time.time()
            button_pressed += 1

            print("Button has been pressed.")

            while True:
                if button.value == 0:
                    # Button has been released.
                    # Do stuff if button has been released.

                    time_elapsed = time.time() - startTick

                    print("Button has been released.")
                    break

                time.sleep(1/30)
            
            if time_elapsed < 0.25:
                print("OPTION 1")

                continue

            elif time_elapsed < 1 and time_elapsed > 0.25:
                print("OPTION 2")

                if LED.value == 1:
                    LED.off()
                else:
                    LED.on()

            elif time_elapsed > 1 and time_elapsed < 2:
                print("OPTION 3")

                button_pressed = 0

                if LED.value == 1:
                    LED.off()
                else:
                    LED.on()

            elif time_elapsed > 2 and time_elapsed < 3:
                print("OPTION 4")

                button_pressed = 0

                newTick = time.time()

                while True:
                    if time.time() < newTick + 5:
                        LED.on()
                        time.sleep(0.125)
                        LED.off()
                        time.sleep(0.125)
                    else:
                        break

            print("BUTTON PRESSED: " + str(button_pressed))
            print("TIME ELAPSED: " + str(time_elapsed))

    time.sleep(1/30)


def main():
    for key, value in SYSTEM_ESSENTIALS.items():
        try:
            thread.start_new_thread(setup_button, (key, value, ))
        except:
            print("ERROR: FAILED TO CREATE NEW THREAD.")

        time.sleep(0.125)


if __name__ == "__main__":
    main()

while system_enabled:
    pass
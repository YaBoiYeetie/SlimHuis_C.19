__version__ = '1.000'
__author__ = 'Robbe De Budt'
__date__ = "05/05/2020"

# LIBRARIES
import time
import thread
from gpiozero import Button
from gpiozero import LED

# VARIABLES
BUTTON_LED_ARRAY = {
    Button(12): LED(21),
    Button(24): LED(20),
    Button(23): LED(16),
    Button(18): LED(5)
}          

# FUNCTIONS
def better_setup_button(button, LED):    
    while 1: # MAIN LOOP
        time.sleep(1/30) # HOTFIX

        time_elapsed = 0
        button_pressed = 0
        new_tick = time.time()

        while time.time() < new_tick + 0.5: # SUB LOOP 1
            if button.value == 1:
                # Button has been pressed

                button_pressed += 1
                startTick = time.time()

                while 1: # SUB LOOP 2
                    if button.value == 0:
                        # Button has been released

                        time_elapsed = time.time() - startTick

                        break
                
                if time_elapsed < 0.35:
                    new_tick = time.time()
                    time_elapsed = 0
                    continue
                else:
                    break
        
        if button_pressed >= 1: # Button was pressed once at minimum.
            if button_pressed >= 2: # Button was pressed twice at minimum.
                if button_pressed >= 3: # Button was pressed three times at minimum.
                    if LED.value == 1: # LED is on.
                        print("OPTION 3 - 1")
                    else: # LED is off.
                        print("OPTION 3 - 2")
                else: # Button was pressed twice.
                    if LED.value == 1: # LED is on.
                        LED.off() # Turn off LED.
                    else: # LED is off.
                        LED.on() # Turn on LED.
            else: # Button was pressed once.
                if LED.value == 1: # LED is on.
                    if time_elapsed > 1: # Button was held for longer than 1 second.
                        time.sleep(10) # Wait 10 seconds.
                        LED.off() # Turn off LED.
                    else: # Button was not held longer than 1 second.
                        LED.off() # Turn off LED.
                else: # LED is off.
                    if time_elapsed > 1: # Button was held for longer than 1 second.
                        LED.on() # Turn on LED.
                        time.sleep(15) # Wait 15 seconds.
                        
                        new_tick = time.time() + 25 # Make the LED blink for 25 seconds.
                        while time.time() < new_tick:
                            LED.off()
                            time.sleep(0.25)
                            LED.on()
                            time.sleep(0.25)
                    else: # Button was not held longer than 1 second.
                        LED.on() # Turn on LED.
                


"""
def setup_button(button, LED):
    time_elapsed = 0
    button_pressed = 0

    while 1:
        time_elapsed = 0
        temporary_tick = time.time() + 0.25

        # CHECK IF BUTTON IS PRESSED, THEN CHECK AGAIN FOR ANOTHER PRESS within 0.25 seconds, if none, continue the script with given input.

        while time.time() < temporary_tick:
            if button.value == 1:
                # Button has been pressed.
                # Do stuff if button has been pressed.

                startTick = time.time()
                button_pressed += 1

                print("Button has been pressed.")

                while 1:
                    if button.value == 0:
                        # Button has been released.
                        # Do stuff if button has been released.

                        time_elapsed = time.time() - startTick

                        print("Button has been released.")
                        break

                    time.sleep(1/30)

                continue

        if button_pressed > 0:
            if time_elapsed < 0.25 and time_elapsed > 0:
                print("RAPID PRESS.")
                continue 
            elif button_pressed == 1:
                print("Button was pressed once")

                if time_elapsed < 1:
                    if LED.value == 0:
                        LED.on()
                    else:
                        LED.off()
                elif time_elapsed > 1 and time_elapsed < 3:
                    newTick = time.time()
                    while time.time() < newTick + 10:
                        LED.on()
                        time.sleep(0.125)
                        LED.off()
                        time.sleep(0.125)
            elif button_pressed == 2:
                print("Button was pressed twice")
            elif button_pressed == 3:
                print("Button was pressed thrice")       

            button_pressed = 0
            print("BUTTON PRESSED: " + str(button_pressed))
            print("TIME ELAPSED: " + str(time_elapsed))

    time.sleep(1/30)
"""


def main():
    for key, value in BUTTON_LED_ARRAY.items():
        try:
            thread.start_new_thread(better_setup_button, (key, value, ))
        except:
            print("ERROR: FAILED TO CREATE NEW THREAD.")

        time.sleep(0.125)

# CODE
if __name__ == "__main__":
    main()

while 1:
    pass
from papirus import PapirusTextPos
import Item_List as IL
import RPi.GPIO as GPIO


def main():

    SW1 = 16
    SW2 = 26
    SW3 = 20
    SW4 = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SW1, GPIO.IN)
    GPIO.setup(SW2, GPIO.IN)
    GPIO.setup(SW3, GPIO.IN)
    GPIO.setup(SW4, GPIO.IN)

    while True:
        if (GPIO.input(SW1) == False) and (GPIO.input(SW2) == False):
            write_text(papirus, "Exiting ...", SIZE)
            sleep(0.2)
            papirus.clear()
            sys.exit()
        if GPIO.input(SW4) == False:
            print("button 4 pressed")
        if GPIO.input(SW3) == False:
            print("button 3 pressed")
        if GPIO.input(SW1) == False:
            IL.Item_List().draw_lines_and_text(["Hello", "world", "dog"], 3)
        sleep(0.1)


main()

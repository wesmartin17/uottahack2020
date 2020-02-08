from papirus import PapirusTextPos
import Item_List as IL
import RPi.GPIO as GPIO
from time import sleep


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

    menu = IL.Item_List(["Hello", "world", "dog"], 4).show()

    while True:
        if (GPIO.input(SW1) == False) and (GPIO.input(SW2) == False):
            write_text(papirus, "Exiting ...", SIZE)
            sleep(0.2)
            papirus.clear()
            sys.exit()
        if GPIO.input(SW4) == False:
            menu.select_down()
            menu.show()
        if GPIO.input(SW3) == False:
            menu.select_up()
            menu.show()
        sleep(0.1)


main()

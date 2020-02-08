from papirus import PapirusTextPos
import ui.Item_List as IL


def main():

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

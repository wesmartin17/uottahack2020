from papirus import PapirusTextPos
from ui.Item_List import Item_List


def main():

    while True:
        if (GPIO.input(SW1) == False) and (GPIO.input(SW2) == False):
            write_text(papirus, "Exiting ...", SIZE)
            sleep(0.2)
            papirus.clear()
            sys.exit()
        if GPIO.input(SW4) == False:
            draw_text("button 4 pressed")
        if GPIO.input(SW3) == False:
            draw_text("button 3 pressed")
        if GPIO.input(SW1) == False:
            Item_List().draw_lines_and_text(["Hello", "world", "dog"], 3)
        sleep(0.1)


def draw_text(text_str):

    # Same as calling "PapirusTextPos(True [,rotation = rot])"
    text = PapirusTextPos([rotation=rot])

    # Write text to the screen at selected point, with an Id
    # "hello world" will appear on the screen at (10, 10), font size 20, straight away
    text.AddText(text_str, 0, 10, Id="Start")


main()

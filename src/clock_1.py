from __future__ import print_function

import os
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
import time
from papirus import Papirus

# Check EPD_SIZE is defined
EPD_SIZE=0.0
if os.path.exists('/etc/default/epd-fuse'):
    exec(open('/etc/default/epd-fuse').read())
if EPD_SIZE == 0.0:
    print("Please select your screen size by running 'papirus-config'.")
    sys.exit()

# Running as root only needed for older Raspbians without /dev/gpiomem
if not (os.path.exists('/dev/gpiomem') and os.access('/dev/gpiomem', os.R_OK | os.W_OK)):
    user = os.getuid()
    if user != 0:
        print("Please run script as root")
        sys.exit()

WHITE = 1
BLACK = 0

CLOCK_FONT_FILE = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
DATE_FONT_FILE  = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'

def main(argv):

    """main program - draw and display time and date"""

    papirus = Papirus(rotation = int(argv[0]) if len(sys.argv) > 1 else 0)

    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=papirus.panel, w=papirus.width, h=papirus.height, v=papirus.version, g=papirus.cog, f=papirus.film))
    print(jerk)
    papirus.clear()

    demo(papirus)


def demo(papirus):
    """simple partial update demo - draw a clock"""

    # initially set all white background
    image = Image.new('1', papirus.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    width, height = image.size

    clock_font_size = int((width - 4)/(8*0.65))      # 8 chars HH:MM:SS
    clock_font = ImageFont.truetype(CLOCK_FONT_FILE, clock_font_size)
    date_font_size = int((width - 10)/(10*0.65))     # 10 chars YYYY-MM-DD
    date_font = ImageFont.truetype(DATE_FONT_FILE, date_font_size)

    # clear the display buffer
    draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
    previous_second = 0
    previous_day = 0

    while True:
        while True:
            now = datetime.today()
            if now.second != previous_second:
                break
            time.sleep(0.1)

        if now.day != previous_day:
            draw.rectangle((2, 2, width - 2, height - 2), fill=WHITE, outline=BLACK)
            draw.text((10, clock_font_size + 10), '{y:04d}-{m:02d}-{d:02d}'.format(y=now.year, m=now.month, d=now.day), fill=BLACK, font=date_font)
            previous_day = now.day
        else:
            draw.rectangle((5, 10, width - 5, 10 + clock_font_size), fill=WHITE, outline=WHITE)

        draw.text((5, 10), '{h:02d}:{m:02d}:{s:02d}'.format(h=now.hour, m=now.minute, s=now.second), fill=BLACK, font=clock_font)

        # display image on the panel
        papirus.display(image)
        if now.second < previous_second:
            papirus.update()    # full update every minute
        else:
            papirus.partial_update()
        previous_second = now.second

# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))

    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass

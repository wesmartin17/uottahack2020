from papirus import Papirus, PapirusComposite


class Item_List():

    items = []
    textNImg = PapirusComposite(False)

    def __init__(self, items, items_per_screen=3):
        self.items = items
        self.num_lines = items_per_screen
        self.draw_lines_and_text(items, items_per_screen)

    def draw_lines_and_text(self, items, num_lines):
        horiz_line = "./img/ui/horiz_line.bmp"
        # LINES
        for i in range(num_lines):
            h = 128/num_lines * (i+1)
            self.textNImg.AddImg(horiz_line, 0, h, (128, 1),
                                 Id="Line{}".format(str(i)))
        # TEXT
        for i in range(items):
            invert = False
            if i % 2:
                invert = True
            h = 128/num_lines * i
            self.textNImg.AddText(items[i], 10, h, Id=i, invert=invert)

    def show(self):
        self.textNImg.WriteAll()

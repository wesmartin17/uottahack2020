from papirus import Papirus, PapirusComposite


class Item_List():

    items = []
    textNImg = PapirusComposite(False)
    selected = 0

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
        for i in range(len(items)):
            invert = False
            if i == self.selected:
                invert = True
            h = (128/num_lines * i) + 10
            self.textNImg.AddText(items[i], 10, h, Id=i, invert=invert)

    def show(self):
        self.textNImg.WriteAll()

    def select_up(self):
        self.selected = self.selected - 1
        if self.selected < 0:
            self.selected = len(self.items)-1

    def select_down(self):
        self.selected = self.selected + 1
        if self.selected > len(self.items):
            self.selected = 0

from papirus import Papirus, PapirusComposite


class Item_List():

    items = []
    items_per_screen = 0
    textNImg = PapirusComposite(True)
    selected = 0

    def __init__(self, items, items_per_screen=3):
        self.items = items
        self.items_per_screen = items_per_screen
        self.draw_lines_and_text()

    def draw_lines_and_text(self):
        horiz_line = "./img/ui/horiz_line.bmp"
        num_lines = self.items_per_screen
        items = self.items
        # LINES
        for i in range(num_lines):
            h = 128/num_lines * (i+1)
            self.textNImg.AddImg(horiz_line, 0, h, (128, 1),
                                 Id="Line{}".format(str(i)))
        # TEXT
        for i in range(len(items)):
            txt = items[i]
            if i == self.selected:
                txt = u"\u003E"+txt
            h = (128/num_lines * i) + 10
            self.textNImg.AddText(txt, 10, h, Id=i)
        self.textNImg.WriteAll()

    def redraw_text(self, oldID, newID):
        self.textNImg.UpdateText(oldID, self.items[oldID])
        self.textNImg.UpdateText(newID, u"\u003e"+self.items[newID])
        self.textNImg.WriteAll()

    def select_up(self):
        old = self.selected
        self.selected = self.selected - 1
        if self.selected < 0:
            self.selected = len(self.items)-1
        self.redraw_text(old, self.selected)

    def select_down(self):
        old = self.selected
        self.selected = self.selected + 1
        if self.selected >= len(self.items):
            self.selected = 0
        self.redraw_text(old, self.selected)

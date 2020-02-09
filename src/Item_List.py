from papirus import Papirus, PapirusComposite, PapirusTextPos


class Item_List():

    items = []
    text = PapirusTextPos(False)
    items_per_screen = 0
    selected = 0
    bottom_window = 2

    def __init__(self, items, items_per_screen=3):
        self.items = items
        self.items_per_screen = items_per_screen
        self.draw_text()

    def draw_text(self):
        if self.selected > bottom_window:
            self.bottom_window += 1
        elif self.selected < bottom_window - 2:
            self.bottom_window -= 1

    def redraw_text(self, oldID, newID):
        self.text.UpdateText(oldID, self.items[oldID])
        self.text.UpdateText(newID, u"\u003E"+self.items[newID])
        self.text.WriteAll()

    def select_up(self):
        old = self.selected
        if self.selected > 0:
            self.selected = self.selected - 1
        self.redraw_text(old, self.selected)

    def select_down(self):
        old = self.selected
        if self.selected < len(self.items):
            self.selected = self.selected + 1
        self.redraw_text(old, self.selected)

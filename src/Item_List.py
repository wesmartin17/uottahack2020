from papirus import Papirus, PapirusComposite, PapirusTextPos


class Item_List():

    items = []
    text = PapirusTextPos(False)
    items_per_screen = 0
    selected = 0

    def __init__(self, items, items_per_screen=3):
        self.items = items
        self.items_per_screen = items_per_screen
        self.draw_text()

    def draw_text(self):
        items = self.items
        num_lines = self.items_per_screen
        # TEXT
        for i in range(len(items)):
            txt = items[i]
            if i == self.selected:
                txt = u"\u003E"+txt
            h = (128/num_lines * i) + 10
            self.text.AddText(txt, 10, h, Id=i)
        self.text.WriteAll()

    def redraw_text(self, oldID, newID):
        self.text.UpdateText(oldID, self.items[oldID])
        self.text.UpdateText(newID, u"\u003E"+self.items[newID])
        self.text.WriteAll()

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

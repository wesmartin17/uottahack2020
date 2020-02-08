from papirus import Papirus, PapirusComposite


class Item_List():

    items = []
    textNImg = PapirusComposite(False)
    num_lines = 0

    def __init__(self, items, items_per_screen=3):
        self.items = items
        self.num_lines = items_per_screen
        self.draw_lines_and_text(items_per_screen)

    def draw_lines_and_text(self):
        horiz_line = "./img/ui/horiz_line.bmp"

        for i in range(num_lines):
            h = 128/num_lines * i
            textNImg.AddImg("/path/to/image", 0, h, Id="Line{}".format(str(i)))

        for i in self.items:
            h = 128/num_lines * i
            textNImg.AddText(i, 0, h, Id=i)

    def show(self):
        textNImg.WriteAll()

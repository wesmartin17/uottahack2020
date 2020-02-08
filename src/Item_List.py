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

        for i in range(num_lines):
            h = 128/num_lines * i
            self.textNImg.AddImg(horiz_line, 0, h,
                                 Id="Line{}".format(str(i)))

        for i in items:
            h = 128/num_lines * len(items)
            self.textNImg.AddText(i, 0, h, Id=i)

    def show(self):
        textNImg.WriteAll()

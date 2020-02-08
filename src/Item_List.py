from papirus import Papirus, PapirusComposite


class Item_List():

    items = []
    textNImg = PapirusComposite(False)

    def __init__(self, items, items_per_screen=3):
        super().__init__()
        self.items = items
        self.draw_lines_and_text(items_per_screen)
        textNImg.WriteAll()

    def draw_lines_and_text(self, num_lines):
        horiz_line = "./img/ui/horiz_line.bmp"

        for i in range(num_lines):
            h = 128/num_lines * i
            textNImg.AddImg("/path/to/image", 0, h, Id="Line{}".format(str(i)))

        for i in self.items:
            h = 128/num_lines * i
            textNImg.AddText(i, 0, h, Id=i)

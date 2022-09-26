from PIL import Image, ImageDraw, ImageFont # 823, 416
from threading import Thread

class Token(Thread):

    def __init__(self, num) :
        Thread.__init__(self)
        self.num = num

    def run(self):
        image = Image.open("sourceBW.jpg")

        draw = ImageDraw.Draw(image, "RGB")

        font = ImageFont.truetype("Fonts\\TimesNewRoman\\times.ttf", 72)

        draw.text(xy = (823, 416), text = f"{self.num:3d}", fill = (0, 0, 0), font = font)

        image.save(f"TokenThread\\{self.num:03d}.png")
        print(f"Ready : {self.num:03d}.png")

def make_tokens(n) :
    Tokens = ()

    for i in range(n) :
        Tokens += (Token(i+1), )

    for token in Tokens :
        token.start()

    for token in Tokens :
        token.join()

    print(f"TOKENS READY : {n}")

make_tokens(340)
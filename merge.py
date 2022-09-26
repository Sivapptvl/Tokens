from PIL import Image
from threading import Thread

WIDTH = 1078
HEIGHT = 579

class Merge(Thread) :

    def __init__(self, x, y, canvas_no) :
        Thread.__init__(self)

        self.canvas = Image.new("RGB", (x * WIDTH, y * HEIGHT), (0, 0, 0))  # Making an empty image
        
        self.X = x  # no. of images in X-axis
        self.Y = y  # no. of images in Y-axis
        
        self.canvas_no = canvas_no  # n th page (merged)
        self.token_no = (((canvas_no-1) * self.X * self.Y) + 1) # Starting Page-No

    def run(self) :

        for y in range(0, self.Y * HEIGHT, HEIGHT) :    # Looping through a row

            for x in range(0, self.X * WIDTH, WIDTH) :  # Looping through a column

                image = Image.open(f"TokenThread\\{self.token_no:03d}.png")     # Opening a token using number

                self.canvas.paste(image, (x, y))    # Pasting token at a coordinate : (x, y)
                
                # print(f"Pasted Token {self.token_no:03d} on page {self.canvas_no:02d}")     # Logging recently pasted token

                self.token_no += 1      # Changing token number to next

        self.canvas.save(f"PageThread\\page{self.canvas_no:02d}.png")   # saving the page with pasted tokens
        print(F"Page {self.canvas_no:02d}.png is ready")     # Logging that Page is Ready

def make_pages(x, y, n) :
    PageThreads = ()

    for i in range(n) :
        PageThreads += (Merge(x, y, i+1), )

    for i in range(n) :
        PageThreads[i].start()

    for i in range(n) :
        PageThreads[i].join()

    print("-" * 21)
    print("ALL PAGES ARE READY")
    print("-" * 21)

make_pages(4, 5, 500//20)
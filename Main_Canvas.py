import numpy
from tkinter import *
import cv2
from PIL import ImageTk,Image

class Main_Canvas(Frame):
    __canvas = None
    __img = None

    def __init__(self, image_filename):
        super().__init__()

        self.__canvas = Canvas(self)

        self.initUI(image_filename)

    def initUI(self, image_filename):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)



        # canvas = Canvas(self)

        self.__canvas.create_rectangle(30, 10, 180, 280,
            outline="#fb0", fill="#fb0")
        # self.__canvas.create_rectangle(150, 10, 240, 80,
        #     outline="#f50", fill="#f50")
        # self.__canvas.create_rectangle(270, 10, 370, 80,
        #     outline="#05f", fill="#05f")
        self.__canvas.pack(fill=BOTH, expand=1)

    def draw_rectangle(self, member):
        self.__canvas.create_rectangle(member.x, member.y, member.w, member.h,
                                       outline="#fb0", fill="#fb0")
        self.__canvas.create_rectangle()

    def draw_image(self, image_filename):
        load = Image.open(image_filename)
        load = load.resize((500, 500))
        # load = cv2.imread(image_filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


def main():
    image = "images/iron.jpg"
    root = Tk()
    mc = Main_Canvas(image)
    root.geometry("1000x500+300+300")
    mc.draw_image(image)

    root.mainloop()


if __name__ == '__main__':
    main()
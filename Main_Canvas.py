import numpy
from tkinter import *


class Main_Canvas(Frame):
    __canvas = None

    def __init__(self):
        super().__init__()

        self.__canvas = Canvas(self)
        canvas = self.initUI()

    def initUI(self):

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

    def draw_image(self,filename):
        img = PhotoImage(file="ball.ppm")
        canvas.create_image(20, 20, anchor=NW, image=img)


def main():

    root = Tk()
    ex = Main_Canvas()
    root.geometry("400x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
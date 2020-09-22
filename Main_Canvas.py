import numpy
from tkinter import *
import cv2
from PIL import ImageTk,Image
from Image_Reproduction import Image_Reproduction

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

    def draw_rectangle(self, population, i):
        # if i < len(population):
        member = population[i]
        self.__canvas.create_rectangle(member.x + 500, member.y, member.w, member.h,
                                       outline="#fb0", fill="#fb0")


        # self.__canvas.create_rectangle()

    def draw_image(self, image_filename):
        load = Image.open(image_filename)
        load = load.resize((500, 500))
        # load = cv2.imread(image_filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def draw_member(self):

        main_canvas.draw_rectangle(population, 0)

        self.__canvas.after(20, self.dr(population, i + 1))


def main():
    image = "images/bluee.jpg"
    population_size = 100
    window_w = 1000
    window_h = 600

    root = Tk()
    main_canvas = Main_Canvas(image)

    image_reproduction = Image_Reproduction()
    population = image_reproduction.create_population(population_size, int(window_w * 0.5), window_h)

    root.geometry(f"{window_w}x{window_h}+300+300")

    main_canvas.draw_image(image)

    # for i in range(population.__len__()):

    root.mainloop()


if __name__ == '__main__':
    main()
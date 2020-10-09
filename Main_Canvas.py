import numpy
from tkinter import *
import cv2
from PIL import ImageTk,Image
from Image_Reproduction import Image_Reproduction
import time

class Main_Canvas(Canvas):
    __canvas = None
    __img_filename = None
    __num_of_frames = None
    window_w = None
    population = None
    image_reproduction = None
    index = 0
    member_changed = False
    items = []
    def __init__(self, image_filename, num_of_frames, window_w, image_reproduction):
        super().__init__()

        self.image_reproduction = image_reproduction
        self.population = image_reproduction.population
        self.__num_of_frames = num_of_frames
        self.shapes = [0 for i in range(num_of_frames)]
        self.window_w = window_w
        self.member = None
        self.__img_filename = image_filename
        # self.__canvas = Canvas(self)

        self.initUI(image_filename, self.population[1])

        # self.__canvas.pack(fill=BOTH, expand=1)


    def initUI(self, image_filename, member):
        self.member = member
        self.master.title("Image Reproduction")
        # self.pack(fill = BOTH, expand = 1)
        self.draw_image(self.__img_filename)
        self.create_shapes()

        self.do_actions()

        # canvas = Canvas(self)

        # self.__canvas.create_rectangle(509, 00, 180, 280,
        #     outline="#fb0", fill="#000")
        # self.__canvas.create_rectangle(150, 10, 240, 80,
        #     outline="#f50", fill="#f50")
        # self.__canvas.create_rectangle(270, 10, 370, 80,
        #     outline="#05f", fill="#05f")
        # self.pack(fill = BOTH, expand = 1)

    def draw_rectangle(self, population, i):
        pass

    def create_shapes(self):

        for i in range(self.__num_of_frames):
            color = self.member.get_color_in_hex_str(i)
            x1 = 510 + self.member.shapes[i, 0]
            y1 = self.member.shapes[i, 1]
            x2 = x1 + self.member.shapes[i, 2]
            y2 = y1 + self.member.shapes[i, 3]
            tmp_item = self.create_rectangle(x1, y1, x2, y2, outline=color, fill=color, tag=f"shape_{i}")
            self.items.append(tmp_item)
            self.pack()

    def update_shapes(self, flag=False):
        # member = population[index]
        for i in range(self.__num_of_frames):
            color = self.member.get_color_in_hex_str(i)
            x1 = 510 + self.member.shapes[i, 0]
            y1 = self.member.shapes[i, 1]
            x2 = x1 + self.member.shapes[i, 2]
            y2 = y1 + self.member.shapes[i, 3]
            self.coords(self.find_withtag(f"shape_{i}"), (x1, y1, x2, y2))
            self.itemconfig(self.items[i], outline=color, fill=color)


    def draw_image(self, image_filename):
        img_size = int(self.window_w/2)
        load = Image.open(image_filename)
        load = load.resize((img_size, img_size))
        # load = cv2.imread(image_filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        # self.pack(fill = BOTH, expand = 1)

    def pack_it_up(self):
        self.__canvas.pack()

    def do_actions(self):
        self.index += 1
        success_level_reached = False
        if self.index >= len(self.population):
            self.index = 0


        self.member = self.population[self.index]

        if not success_level_reached:
            success_level_reached, fittest_member = self.image_reproduction.evolve()
            self.member = fittest_member

        self.update_shapes()

        self.after(1000, self.do_actions)

    def change_member(self, member):
        self.member = member



def main():
    img_path = "images/bluee.jpg"
    population_size = 100
    num_of_frames = 100
    window_w = 1000
    window_h = 600

    image_reproduction = Image_Reproduction(population_size, num_of_frames, int(window_w/2), int(window_w/2),img_path)

    root = Tk()
    root.geometry(f"{window_w}x{window_h}+300+300")
    main_canvas = Main_Canvas(img_path, num_of_frames, window_w, image_reproduction)
    main_canvas.pack(fill=BOTH, expand=1)


    root.mainloop()



if __name__ == '__main__':
    main()
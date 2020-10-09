import numpy as np
from Shape import Shape
import cv2
from random import randint
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

class Member:
    num_of_frames = None
    shapes = []
    fitness = 0
    color_matrix = None
    habitat_w = 0
    habitat_h = 0
    def __init__(self, num_of_shapes, habitat_w, habitat_h):
        self.frame_list = []
        self.habitat_w = habitat_w
        self.habitat_h = habitat_h

        self.color_matrix = np.zeros((habitat_h, habitat_w, 3)) + 255

        self.create_shapes(num_of_shapes, habitat_w, habitat_h)

    def create_shapes(self, num_of_shapes, habitat_w, habitat_h):
        # self.population = np.zeros(num_of_shapes, self.DNA_length)
        ww = int(habitat_w*0.2)
        hh = int(habitat_h*0.2)
        self.w = np.random.randint(low=1, high=ww - 1, size=(num_of_shapes, 1))
        self.h = np.random.randint(low=1, high=hh - 1, size=(num_of_shapes, 1))
        self.x = np.random.randint(low=1, high=habitat_w - self.w, size=(num_of_shapes, 1))
        self.y = np.random.randint(low=1, high=habitat_h - self.h, size=(num_of_shapes, 1))
        self.g = np.random.randint(low=0, high=254, size=(num_of_shapes, 1))
        self.r = np.random.randint(low=0, high=254, size=(num_of_shapes, 1))
        self.b = np.random.randint(low=0, high=254, size=(num_of_shapes, 1))
        # self.shapes = [Shape(x[i], y[i], w[i], h[i], r[i], g[i], b[i], habitat_w, habitat_h) for i in range(num_of_shapes)]
        self.shapes = np.concatenate((
            self.x,
            self.y,
            self.w,
            self.h,
            self.r,
            self.g,
            self.b),

            axis=1)

    def get_color_in_hex_str(self, index):
        color_in_hex = self.integer_to_hex(self.r[index, 0]) + self.integer_to_hex(self.g[index, 0]) + self.integer_to_hex(self.b[index, 0])
        assert len(color_in_hex) == 6
        return f"#{color_in_hex}"

    def integer_to_hex(self, number):
        number_hex = hex(number)
        number_hex = number_hex.replace("0x", "")
        if number < 16:
            number_hex = f"0{number_hex}"
        return number_hex

    def get_color_matrix(self):
        # self.color_matrix = -1
        for shape in self.shapes:
            # for i in range(shape[2]):
            #     for j in range(shape[3]):
            # if np.sum(self.color_matrix[shape[0] + i-1, shape[1] + j-1]) < 0:
            self.color_matrix[shape[1]:shape[1] + shape[3], shape[0]:shape[0] + shape[2]] = np.array([shape[4], shape[5], shape[6]]).astype(np.int)  #BGR
        # self.color_matrix = self.color_matrix.astype(np.int)


        # norm_image = cv2.normalize(self.color_matrix, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        # bgr_image = cv2.cvtColor(norm_image, cv2.COLOR_RGB2BGR)
        # cv2.imshow("img", bgr_image)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        return self.color_matrix

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def get_DNA(self):
        # DNA = np.reshape(self.shapes, (int(self.shapes.shape[0]*self.shapes.shape[0]), 1))

        return self.shapes

    def set_DNA(self, new_shapes):
        self.shapes = new_shapes


    '''
     Advertisement: 
     Hey kid. You ever feel like you don't belong?
     Feeling like the world doesmn't accept you for who you are.
     Well, don't be afraid. There is a place in where no matter who you are, you'll fit in.
     Apply for Xaviers school for speciail kids!
     We even have an explosion-evacuation program. 
     As soon as an eplosion is detected, we play "Sweet Dreams" and Quicksilver handles the rest.
    '''
    def mutate(self, mutation_index):
        if len(self.shapes) < mutation_index or \
                len(self.shapes[mutation_index]) < 7:
            print("yo")
        ww = int(self.habitat_w * 0.2)
        hh = int(self.habitat_h * 0.2)
        self.shapes[mutation_index][0] = randint(1, ww - 1)  #, size=(1, 1))
        self.shapes[mutation_index][1] = randint(1, hh - 1)  #, size=(1, 1))
        self.shapes[mutation_index][2] = randint(1, self.habitat_w - self.shapes[mutation_index][0])  #, size=(1, 1))
        self.shapes[mutation_index][3] = randint(1, self.habitat_h - self.shapes[mutation_index][1])  #, size=(1, 1))
        self.shapes[mutation_index][4] = randint(0, 254)  #, size=(1, 1))
        self.shapes[mutation_index][5] = randint(0, 254)  #, size=(1, 1))
        self.shapes[mutation_index][6] = randint(0, 254)  #, size=(1, 1))

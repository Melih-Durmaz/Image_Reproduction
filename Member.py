import numpy as np
from Shape import Shape

class Member:
    num_of_frames = None
    DNA_length = 7
    shapes = []
    def __init__(self,num_of_shapes, habitat_w, habitat_h):
        self.frame_list = []

        self.habitat_matrix = np.zeros((habitat_h, habitat_w))

        self.create_shapes(num_of_shapes, habitat_w, habitat_h)

    def create_shapes(self, num_of_shapes, habitat_w, habitat_h):
        # self.population = np.zeros(num_of_shapes, self.DNA_length)
        w = np.random.randint(low=1, high=habitat_w - 1, size=num_of_shapes)
        h = np.random.randint(low=1, high=habitat_h - 1, size=num_of_shapes)
        x = np.random.randint(low=1, high=habitat_w - w, size=num_of_shapes)
        y = np.random.randint(low=1, high=habitat_h - h, size=num_of_shapes)
        g = np.random.randint(low=0, high=254, size=num_of_shapes)
        r = np.random.randint(low=0, high=254, size=num_of_shapes)
        b = np.random.randint(low=0, high=254, size=num_of_shapes)
        # self.shapes = [Shape(x[i], y[i], w[i], h[i], r[i], g[i], b[i], habitat_w, habitat_h) for i in range(num_of_shapes)]
        self.shapes = np.concatenate((x, y, w, h, r, g, b), axis=1)

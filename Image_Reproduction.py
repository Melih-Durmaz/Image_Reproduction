from Member import Member
import numpy as np

class Image_Reproduction:

    population = None
    population_size = None
    def __init__(self, population_size):
        pass
        # self.create_population(population_size, habitat_w, habitat_h)

    def create_population(self,population_size, number_of_shapes, habitat_w, habitat_h):

        self.population = [Member(number_of_shapes, habitat_w, habitat_h) for i in range(population_size)]

    def get_fittest_member(self):
        pass
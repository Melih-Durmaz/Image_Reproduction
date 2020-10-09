from Member import Member
import numpy as np
# from skimage.measure import _structural_similarity as ssim
from skimage.metrics import structural_similarity as ssim
import cv2
from random import randint
import random
import copy
import time

class Image_Reproduction:

    population = []
    __reproducers = []
    population_size = None
    __child = None
    __numOfGenerations = 0
    __numOfShapesPerMember = None
    __numOfDeadAndNewBorn = None
    __average_fitness = 0
    __sum_fitness = 0
    __habitat_w = 0
    __habitat_h = 0
    img_path = None

    def __init__(self, population_size, number_of_shapes, habitat_w, habitat_h, img_path):
        self.__numOfShapesPerMember = number_of_shapes
        self.create_population(population_size, number_of_shapes, habitat_w, habitat_h)
        self.img_path = img_path
        self.population_size = population_size
        self.__habitat_w = habitat_w
        self.__habitat_h = habitat_h

        self.__numOfDeadAndNewBorn = int(self.population_size * 0.2)

    def create_population(self, population_size, number_of_shapes, habitat_w, habitat_h):

        self.population = [Member(number_of_shapes, habitat_w, habitat_h) for i in range(population_size)]

    def evolve(self):
        successLevelReached = False
        self.__numOfGenerations = 1

        # if not successLevelReached:
        successLevelReached, fittest_member = self.calculateFitness()

        if not successLevelReached:
            self.naturalSelection()
            self.reproduction()
            print('Generation: ', self.__numOfGenerations)
            print('Average Fitness: ', self.__average_fitness)
        else:
            print('SUCCESS LEVEL REACHED!!')
            print(f"Avg. Fitness: {self.__average_fitness}")
        self.__numOfGenerations += 1

        return successLevelReached, fittest_member

    def naturalSelection(self):
        self.theWeakIsDead()
        self.orderSelection(0)
        # self.diversityOrderSelection()

    def theWeakIsDead(self):
        self.sortPopulation()

        for i in range(self.__numOfDeadAndNewBorn):
            whoWillDie = randint(1, self.__numOfDeadAndNewBorn)
            weakMember = self.population[-whoWillDie]
            self.population.remove(weakMember)
    
    def sortPopulation(self):
        k = 1
        gap = self.population.__len__()//pow(2, k)
        while gap > 0:
            for j in range(0, (self.population.__len__() - gap)):
                i = j
                while i >= 0:
                    if self.population[i].get_fitness() < self.population[i + gap].get_fitness():
                        self.population[i], self.population[i + gap] = \
                            self.population[i + gap], self.population[i]
                    i -= gap
            k += 1
            gap = self.population.__len__() // pow(2, k)

    '''
        Applies order selection to the sorted population.

        For population size = n:

        sampleSpace = 1 + 2 + 3 + ...... (n - 1) + n = n*(n + 1)/2

        Then a random number is selected from [0,sampleSpace).
        Then, Binary Search is used to find the interval of randomIntervalValue.

        If, for example, the randomIntervalValue is 5, it's in between 2(1 + 2) and 3(1 + 2 + 3)
        In this case, lowerLimit is selected to determine selectedMemberIndex.
        If, lowerLimit is 2, as in the example above, (n - 2) becomes selectedMemberIndex.

        Basically, members with lower indexes (therefore higher fitness values) have higher possibilities of being selected.
        So the first member is selected if randomIntervalValue happens to be
        in the last n numbers (interval of (sampleSpace - n,sampleSpace] ),
        and the last member is selected if randomIntervalValue is 0.

         This function is called 2 times. First for selecting the (rather) fit ones, then for selecting
        diverse ones
    '''

    def orderSelection(self,secondTime):
        sampleSpace = int((self.population.__len__()*(self.population.__len__()+1))/2)

        '''
          If this function is called for the first time in this generation,
         clear reproducers fom the last generation.
        '''
        if not secondTime:
            del self.__reproducers[:]

        # currentMember = Shape.Shape()
        # currentMember.setFitness(0.99)

        condition = True

        for i in range(self.__numOfDeadAndNewBorn * 2):
            condition = True
            # while (condition):

            randomIntervalValue = randint(0, sampleSpace)
            lowerLimit = 0
            upperLimit = self.population.__len__()

            while upperLimit != (lowerLimit + 1):
                currentIndex = int((lowerLimit + upperLimit) / 2)
                totalSumUntilCurrentIndex = currentIndex * (currentIndex + 1) / 2

                if randomIntervalValue >= totalSumUntilCurrentIndex:
                    lowerLimit = currentIndex
                else:
                    upperLimit = currentIndex

            selectedMemberIndex = self.population.__len__() - lowerLimit - 1
            currentMember = self.population[selectedMemberIndex]

                # if currentMember.get_fitness() < 0.97:
                #     condition = False

            self.__reproducers.append(currentMember)
            self.population.remove(currentMember) # TODO: Why am I deleting the reproducers from the population?

    def reproduction(self):
        # self.sortReproducers()
        i = 0

        while (i + 1) < self.__reproducers.__len__():
            # self.__reproducers[i].increasePriority()
            # self.__reproducers[i + 1].increasePriority()

            parent1 = self.__reproducers[i]
            parent2 = self.__reproducers[i+1]

            # Child member is initialized
            self.__child = Member(self.__numOfShapesPerMember, self.__habitat_w, self.__habitat_h)
            self.__child.set_fitness(0)

            self.cross_over(parent1, parent2, self.__child)
            self.mutation(self.__child)

            # newChromosome = self.scatterChromosomeValues(self.__child,self.__child.getChromosome())
            # self.__child.setNewChromosome(newChromosome)

            # self.__child.createPhenotype()

            self.population.append(copy.deepcopy(self.__child))
            # self.__view.addItem(self.__child)
            #print 'Reproduced', i


            i += 2

        for reproducer in self.__reproducers:
            self.population.append(reproducer)
        assert self.population.__len__() == self.population_size
        print ('Population: ', self.population.__len__())
        # self.resetPopulationDiversity()

    def cross_over(self, parent1, parent2, child):
        new_childs_shapes = np.zeros((self.__numOfShapesPerMember, 7))
        for i in range(self.__numOfShapesPerMember):
            a_or_b = bool(random.getrandbits(1))

            if a_or_b:
                new_childs_shapes[i] = (parent1.shapes[i])
            else:
                new_childs_shapes[i] = (parent2.shapes[i])

            # print(new_childs_shapes[0:i+1])
        assert len(new_childs_shapes) == self.__numOfShapesPerMember
        child.set_DNA(new_childs_shapes.astype(np.int))

    def mutation(self, member):
        for i in range(1):
            mutationProbability = randint(0, 99)
            if mutationProbability < 8:
                mutationIndex = randint(0, self.__numOfShapesPerMember-1)
                member.mutate(mutationIndex)

    def calculateFitness(self):
        successLevelReached = False
        fittest_member = None
        highest_similarity = 0
        self.__sum_fitness = 0
        self.__average_fitness = 0
        for member in self.population:
            if member.get_fitness() == 0:
                current_color_matrix = member.get_color_matrix()
                reference_image = cv2.imread(self.img_path)
                reference_image = cv2.resize(reference_image, (500, 500))
                similarity = ssim(reference_image, current_color_matrix, multichannel=True)

                if similarity > highest_similarity:
                    highest_similarity = similarity
                    fittest_member = member

                self.__sum_fitness += similarity
                member.set_fitness(similarity)
                # print(f"fitness of member {member} is set to {similarity}")

                if highest_similarity > 0.92:
                    successLevelReached = True

        # print(f"Fittest member: ")
        norm_image = cv2.normalize(fittest_member.color_matrix, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX,
                                   dtype=cv2.CV_32F)
        bgr_image = cv2.cvtColor(norm_image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Fittest member", bgr_image)
        # time.sleep(2)
        # cv2.waitKey()
        #
        # cv2.destroyAllWindows()

        print(f"Highest Fitness: {highest_similarity}")
        self.__average_fitness = self.__sum_fitness/self.population_size
        return successLevelReached, fittest_member

    def get_fittest_member(self):
        pass

'Functions to implement the genetic algorithm'
import random

'Create a member of the population'
def individual():
    x = random.uniform(-3,3)
    y = random.uniform(-3,3)
    return [x, y]

'Generate a population - some number of individuals'
def populate(count):
    return [individual() for i in xrange(count)]

'Calculate the fitness of an individual'
def fitness(individual):
    return null

'Take a population and evolve it one generation'
def evolve(pop):
    return null
    

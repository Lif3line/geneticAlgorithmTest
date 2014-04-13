'Functions to implement the genetic algorithm'
import random
import math

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
    x = individual[0]
    y = individual[1]
    return ((1-x)**2) * math.exp(-x**2 - (y+1)**2) - (x - x**3 - y**3)*math.exp(-x**2 - y**2) 

'Take a population and evolve it one generation'
def evolve(pop):
    return null
    

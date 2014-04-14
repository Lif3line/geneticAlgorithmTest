'Functions to implement the genetic algorithm'
import random
import math

class Chromosome:
    def __init__(self,x,y,fitness):
        self.x = x
        self.y = y
        self.fitness = fitness

'Create a member of the population'
def createChromosome():
    x = random.uniform(-3,3)
    y = random.uniform(-3,3)
    return Chromosome(x,y,0)
    

'Generate a population - some number of individuals'
def populate(count):
    return [createChromosome() for i in xrange(count)]

'Calculate the fitness of an individual'
def fitness(chromosome):
    x = chromosome.x
    y = chromosome.y
    return ((1-x)**2) * math.exp(-x**2 - (y+1)**2) - (x - x**3 - y**3)*math.exp(-x**2 - y**2) 

'Take a population and evolve it one generation'
'StrongRet: Percentage of strong candidates to keep'
'WeakRet: Percentage of weak candidates to keep'
'mutationChance: Percentage likelihood of a mutation'
def evolve(pop, strongRet, weakRet, mutationChance):
    for chromosome in pop:
        chromosome.fitness = fitness(chromosome)

    'Take a simplistic approach by keeping strong candidates + some weaker ones and mutation'
    numStrong = int(len(pop) * strongRet)
    parents = pop[:numStrong] # Keep strong candidates
    newPop = pop[numStrong:]  # Remove these from the general population

    for i in xrange(int(len(pop) * weakRet)):
        k = random.randint(0,len(newPop))
        parents.append(newPop[k])
        del newPop[k]

    
    return parents

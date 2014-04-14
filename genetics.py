'Functions to implement the genetic algorithm'
import random
import math

class Chromosome:
    def __init__(self,x,y,fitness):
        self.x = x
        self.y = y
        self.fitness = fitness

    def mutate(self):
        i = random.randint(0,2)
        if (i == 0):
            self.x = random.uniform(-3,3)
        elif (i == 1):
            self.y = random.uniform(-3,3)
        else:
            self.x = random.uniform(-3,3)
            self.y = random.uniform(-3,3)
            
'Calculate the fitness of an individual'        
def fitness(x,y):
    return ((1-x)**2) * math.exp(-x**2 - (y+1)**2) - (x - x**3 - y**3)*math.exp(-x**2 - y**2) 

'Create a member of the population'
def createChromosome():
    x = random.uniform(-3,3)
    y = random.uniform(-3,3)
    return Chromosome(x,y,fitness(x,y))

'Generate a population - some number of individuals'
def populate(count):
    return [createChromosome() for i in xrange(count)]

def calcPopFitness(pop):
    for chromosome in pop:
        chromosome.fitness = fitness(chromosome.x, chromosome.y)
    return pop

'Take a population and evolve it one generation'
'StrongRet: Percentage of strong candidates to keep'
'WeakRet: Percentage of weak candidates to keep'
'mutationChance: Percentage likelihood of a mutation'
def evolve(pop, strongRet, weakRet, mutationChance):
    numStrong = int(len(pop) * strongRet)
    numWeak = int(len(pop) * weakRet)
    if (numStrong + numWeak < 2):
        return 1              # Error case - only one parent available

    pop.sort(key=lambda i: i.fitness, reverse = True)
   
    'Take a simplistic approach by keeping strong candidates + some weaker ones and mutation'
    parents = pop[:numStrong] # Keep strong candidates
    newPop = pop[numStrong:]  # Remove these from the general population

    children = []
    for i in xrange(int(math.ceil(numStrong * 0.5))): # Keep strongest candidates 
        children.append(parents[i])
    
    'Select weaker parents'
    for i in xrange(numWeak):
        k = random.randint(0,len(newPop) - 1)
        parents.append(newPop[k])
        del newPop[k]         # Remove parent from general population

    'Introduce random mutations'
    for chromosome in parents:
        if mutationChance > random.random():
            chromosome.mutate()

    'Crossover to create new children - keep population size constant'
    desiredPopSize = len(pop)
    numParents = len(parents) - 1 # -1 to account for zero index
        
    while len(children) < desiredPopSize:
        i = random.randint(0, numParents)
        j = random.randint(0, numParents)
        if(i != j):               # Don't let anymore asexual reproduction happen           
            male = parents[i]
            female = parents[j]
            child = Chromosome(male.y,female.x,0)
            children.append(child)
    
    return children

'Calculate average fitness of population'
def averageFitness(pop):
    sum = 0
    for i in xrange(len(pop)):
        sum += pop[i].fitness

    return sum / (len(pop) * 1.0)

'Get highest fitness value'
def maxFitness(pop):
    fitnessList = []
    for chromosome in pop:
        fitnessList.append(chromosome.fitness)
    
    return max(fitnessList)



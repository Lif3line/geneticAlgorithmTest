from genetics import *

pop = populate(100)
fitnessTrack = [[averageFitness(pop), maxFitness(pop)]]

for i in xrange(10):
    pop = evolve(pop,0.2,0.05,0.01)
    pop = calcPopFitness(pop)
    fitnessTrack.append([averageFitness(pop), maxFitness(pop)])
    
for i in fitnessTrack:
   print i

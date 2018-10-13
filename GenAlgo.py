#Python3 program to generate target string from a random string using genetic algorithm concepts
 
import random 
#Time delay in printing, to view the string convergence more clearly
import time 
 
#Number of individuals in each generation 
POPULATION_SIZE = 100
  
#Valid genes established for possible chromosomes/individuals/solutions
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
  
#Target string
TARGET = input("Enter Target: ") 
 
class Individual(object): 
    ''' 
    Class representing individuals
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness()   
    @classmethod
    def mutated_genes(self): 
        ''' 
        Creating random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene   
    @classmethod
    def create_gnome(self): 
        ''' 
        Creating chromosome or string of genes 
        '''
        global TARGET 
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''  
        #Chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
  
            #Random probability to determine how much of each parent goes into the child
            #If probability is lesser than 0.45, genes are inserted from parent 1
            #If it is between 0.45 and 0.90, genes are inserted from parent 2
            #Otherwise, genes are mutated for maintaining diversity
            
            prob = random.random()  
            if prob < 0.45: 
                child_chromosome.append(gp1) 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        return Individual(child_chromosome) 
  
    def cal_fitness(self): 
        ''' 
        Calculating fittness score as the number of 
        characters in the random string which differ from target 
        string 
        '''
        global TARGET 
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt: fitness+= 1
        return fitness 
  
#Driver code 
def main(): 
    global POPULATION_SIZE 
  
    #Current generation 
    generation = 1
  
    found = False
    population = [] 
  
    #Create initial population 
    for _ in range(POPULATION_SIZE): 
                gnome = Individual.create_gnome() 
                population.append(Individual(gnome)) 
  
    while not found: 
  
        #Sorting the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 
  
        #If an individual has the lowest fitness score i.e 0, the target has been reached and loop breaks 
        if population[0].fitness <= 0: 
            found = True
            break
        #Otherwise new offsprings are generated for the next generation
        new_generation = [] 
        #Performing Elitism - 10% of the "fittest" population goes to the next gen
        s = int((10*POPULATION_SIZE)/100) 
        new_generation.extend(population[:s]) 

        #From 50% of the "fittest" population, individuals will mate to produce offspring
        s = int((90*POPULATION_SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2) 
            new_generation.append(child) 
  
        population = new_generation 
  
        print("Generation: {}\tString: {}\tFitness: {}".\
              
              format(generation, 
              "".join(population[0].chromosome), 
              population[0].fitness))
        time.sleep(0.5)
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".\
          
          format(generation, 
          "".join(population[0].chromosome), 
          population[0].fitness))
    time.sleep(0.5)
  
if __name__ == '__main__': 
    main()
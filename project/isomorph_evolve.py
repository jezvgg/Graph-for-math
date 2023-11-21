from random import randint, seed, choice, random, choices 
from test import coding_data, create_test 
import matplotlib.pyplot as plt 
from graph import Graph
 

GOAL_MATRIX = Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"})
OUR_MATRIX = Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"})

POPULATION_SIZE = 100 # количество особий в пополяции 
P_CROSSOVER = 0.9   # вероятность скрещивания 
P_MUTATION = 0.1    # вероятность мутации 
MAX_GENERATION = 50 # максимальное количество поколений 
 
GOAL = 0 # цель приспособленности особи 
 
seed(42) 
 
 
class FitnessMax(): 
    def __init__(self): 
        self.values = 0 
 
 
class Individual(list): 
    def __init__(self, *args): 
        super().__init__(*args) 
        self.fitness = FitnessMax() 
 
 
def oneMaxFintess(ind: Individual): 
    ''' 
    Рассчитывает приспособленность особи к задаче. 

    Будем смотреть насколько близко к итоговой матрице находиться наша.

    Для этого дадим каждому столбцу вес (1,2,3,4...) и будем умножать на него, если там единица.

    Потом будем суммировать всё и брать разницу между итоговой матрицей. И возращать модуль разницы. Нужно чтоб она была 0.
    ''' 
    return sum([abs(sum([el*(i+1) for i,el in enumerate(row1)])-sum([el*(i+1) for i,el in enumerate(row2)])) for row1, row2 in zip(GOAL_MATRIX.matrix, ind.matrix)])
 
 
def individualCreator(): 
    verts = GOAL_MATRIX.verticles
    
 
 
def populationCreator(n: int = 0): 
    return list([individualCreator() for i in range(n)]) 
 
 
def clone(value): 
    individ = Individual(value[:]) 
    individ.fitness.values = value.fitness.values 
    return individ 
 
 
def sel_tournament(population, p_len): # fitness proportional selection 
    offspring = [] 
    for _ in range(p_len): 
        ind1, ind2, ind3 = choice(population), choice(population), choice(population) 
        while ind1==ind2 or ind2==ind3 or ind1==ind3: 
            ind1, ind2, ind3 = choice(population), choice(population), choice(population) 
 
        offspring.append(min([ind1, ind2, ind3], key=lambda x: x.fitness.values)) 
 
    return offspring 
 
 
def FPS(population, p_len): 
    weights=[x.fitness.values for x in population] 
    max_weight = max(weights) 
    weights = [max_weight-x for x in weights] 
    return choices(population, weights=weights, k=p_len) 
 
 
def FPS_rang(population, p_len): 
    weights = [indx+1 for indx, _ in enumerate(sorted(population, key=lambda x: x.fitness.values, reverse=True))] 
    return choices(sorted(population, key=lambda x: x.fitness.values, reverse=True), weights=weights, k=p_len) 
 
 
def crossingover(child1, child2): 
    for indx, _ in enumerate(child1): 
        if random() < 0.3: 
            sym1 = child1[indx] 
            sym2 = child2[indx] 
            child1[child1.index(sym2)] = sym1 
            child1[indx] = sym2 
            child2[child2.index(sym1)] = sym2 
            child2[indx] = sym1 
 
 
def mutation(ind, mutv=0.005): 
    for i, _ in enumerate(ind): 
        if random() < mutv: 
            ind1, ind2 = randint(0,len(ind)-1), randint(0,len(ind)-1) 
            while ind1==ind2: 
                ind1, ind2 = randint(0,len(ind)-1), randint(0,len(ind)-1) 
            ind[ind1], ind[ind2] = ind[ind2], ind[ind1] 
 
 
 
if __name__ == "__main__": 
    max_fitnesses = [] 
    mean_fitnesses = [] 
    for i in range(GENERATION_COUNT): 
        population = populationCreator(n=POPULATION_SIZE) 
        gen_counter = 0 
 
        fintess_values = list(map(oneMaxFintess, population)) 
 
        for individual, fintess_value in zip(population, fintess_values): 
            individual.fitness.values = fintess_value 
 
        fintess_values = [ind.fitness.values for ind in population] 
 
        mean_fitness = [] 
        # mean_fitness_ = sum(fintess_values) / len(fintess_values) 
        max_fitness = [] 
        # max_fitness_ = min(fintess_values) 
 
        while min(fintess_values) > GOAL and gen_counter < MAX_GENERATION: 
            gen_counter += 1 
 
            offspring = sel_tournament(population, len(population)) 
            offspring = list(map(clone, offspring)) 
 
            for child1, child2 in zip(offspring[::2], offspring[1::2]): 
                if random() < P_CROSSOVER: 
                    crossingover(child1, child2) 
 
            for mutant in offspring: 
                if random() < P_MUTATION: 
                    mutation(mutant, mutv=1.0/(4*NUMERS_LENGHT)) 
 
            fresh_fintess_values = list(map(oneMaxFintess, offspring)) 
            for ind, fintess_value in zip(offspring, fresh_fintess_values): 
                ind.fitness.values = fintess_value 
 
            population[:] = offspring 
 
            fintess_values = [ind.fitness.values for ind in population] 
 
            max_fitness_ = min(fintess_values) 
            max_fitness.append(max_fitness_) 
            mean_fitness_ = sum(fintess_values) / len(fintess_values) 
            mean_fitness.append(mean_fitness_) 
            # print(f'Поколение {gen_counter}: Макс. приспособ. = {max_fitness_}, Сред. приспособ = {mean_fitness_}') 
            # print(f'Лучший индивидуум: {min(population, key=lambda x: x.fitness.values)}\n') 
        max_fitnesses.append(max_fitness_)  
        mean_fitnesses.append(mean_fitness_) 
        print(f'Популяция {i+1} лучший индивидуум {max_fitness_}, средняя приспособленность {mean_fitness_}') 
        if max_fitness_ == 0: break 
        # fig, axis = plt.subplots(1,2) 
        # plt.plot(range(gen_counter), max_fitness) 
        # plt.plot(range(gen_counter), mean_fitness) 
        # plt.show() 
        # break

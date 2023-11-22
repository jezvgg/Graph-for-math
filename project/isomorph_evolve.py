from random import seed, random, choices, sample
from project.graph import Graph
 
 
seed(42) 
 
 
class Individual(Graph): 
    def __init__(self, *args): 
        super().__init__(*args) 
        self.fitness = 0
 
 
def oneMaxFintess(ind: Individual): 
    ''' 
    Рассчитывает приспособленность особи к задаче. 

    Будем смотреть насколько близко к итоговой матрице находиться наша.

    Для этого дадим каждому столбцу вес (1,2,3,4...) и будем умножать на него, если там единица.

    Потом будем суммировать всё и брать разницу между итоговой матрицей. И возращать модуль разницы. Нужно чтоб она была 0.
    ''' 
    return sum([abs(sum([el*(i+1) for i,el in enumerate(row1)])-sum([el*(i+1) for i,el in enumerate(row2)])) for row1, row2 in zip(GOAL_MATRIX.matrix, ind.matrix)])
 
 
def individualCreator() -> Individual: 
    '''
    Копируем нашу матрицу, и переставляем случайным образом вершины.
    '''
    samples = sample(list(range(len(OUR_MATRIX.verticles))), k=len(OUR_MATRIX.verticles))
    ind = OUR_MATRIX.copy()
    ind.set(samples)
    return ind
    
 
def populationCreator(n: int = 0) -> list[Individual]: 
    return list([individualCreator() for i in range(n)]) 
 
 
def clone(ind): 
    fit = ind.fitness
    new_ind = Individual(ind.dict)
    new_ind.fitness = fit
    return new_ind
 
 
def sel_tournament(population: list[Individual], p_len): # fitness proportional selection 
    offspring = [] 
    for _ in range(p_len): 
        ind1, ind2, ind3 = sample(population, k=3)
        offspring.append(min([ind1, ind2, ind3], key=lambda x: x.fitness)) 
 
    return offspring 
 
 
def FPS(population, p_len): 
    weights=[x.fitness for x in population] 
    max_weight = max(weights) 
    weights = [max_weight-x for x in weights] 
    return choices(population, weights=weights, k=p_len) 
 
 
def FPS_rang(population, p_len): 
    weights = [indx+1 for indx, _ in enumerate(sorted(population, key=lambda x: x.fitness, reverse=True))] 
    return choices(sorted(population, key=lambda x: x.fitness, reverse=True), weights=weights, k=p_len) 
 
 
def crossingover(child1: Individual, child2: Individual):
    '''
    С определённой вероятностью меняем местами некоторые индексы
    ''' 
    for vert1, vert2 in zip(child1.verticles, child2.verticles):
        if random() < 0.3:
            child1.replace(vert1, vert2)
            child2.replace(vert2, vert1)

 
def mutation(ind: Individual, mutv=0.05): 
    for _ in enumerate(ind.verticles): 
        if random() < mutv: 
            vert1, vert2 = sample(ind.verticles, k=2)
            ind.replace(vert1, vert2)
 
 
def isomorph_evolve(goal_matrix: Graph, our_matrix: Graph, POPULATION_SIZE = 100, P_CROSSOVER = 0.9, P_MUTATION = 0.1, MAX_GENERATION = 50) -> tuple[bool, Graph]:
    '''
    Эврестический алгоритм который проверяет являются ли графы изоморфны и ищет подстановку,

    при которой матрицы смежности графов совпадают.
    '''

    global GOAL_MATRIX
    GOAL_MATRIX = goal_matrix
    global OUR_MATRIX 
    OUR_MATRIX = our_matrix
    
    GOAL = 0 # цель приспособленности особи 
    
    seed(42) 
    
    population = populationCreator(n=POPULATION_SIZE) 
    gen_counter = 0 
 
    fintess_values = list(map(oneMaxFintess, population)) 
 
    for individual, fintess_value in zip(population, fintess_values): 
        individual.fitness = fintess_value 
 
    fintess_values = [ind.fitness for ind in population] 
 
    mean_fitness = [] 
    max_fitness = [] 
    max_fitness_ = min(fintess_values)
 
    while min(fintess_values) > GOAL and gen_counter < MAX_GENERATION: 
        gen_counter += 1 
 
        offspring = sel_tournament(population, len(population)) 
        offspring = list(map(clone, offspring)) 
 
        for child1, child2 in zip(offspring[::2], offspring[1::2]): 
            if random() < P_CROSSOVER: 
                crossingover(child1, child2) 
 
        for mutant in offspring: 
            if random() < P_MUTATION: 
                mutation(mutant, mutv=0.05) 
 
        fresh_fintess_values = list(map(oneMaxFintess, offspring)) 
        for ind, fintess_value in zip(offspring, fresh_fintess_values): 
            ind.fitness = fintess_value 
 
        population[:] = offspring 
 
        fintess_values = [ind.fitness for ind in population] 
 
        max_fitness_ = min(fintess_values) 
        max_fitness.append(max_fitness_) 
        mean_fitness_ = sum(fintess_values) / len(fintess_values) 
        mean_fitness.append(mean_fitness_) 

    return max_fitness_==0, min(population, key=lambda x: x.fitness).copy()


if __name__ == "__main__":
    result = isomorph_evolve(goal_matrix=Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"}),
    our_matrix=Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"}))

    print(result[0])
    print(result[1])
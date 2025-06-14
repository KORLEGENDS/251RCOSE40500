import random

# 간단한 유전 알고리즘 예제: 이진 문자열에서 1의 개수 최댓값 찾기
POP_SIZE = 20
GENE_LENGTH = 16
GENERATIONS = 50
MUT_RATE = 0.01

# 적합도 함수: 문자열에서 '1'의 개수 세기
def fitness(chromosome):
    return chromosome.count('1')

# 초기 집단 무작위 생성
population = [''.join(random.choice('01') for _ in range(GENE_LENGTH)) for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    # 적합도 계산 및 부모 선택 (비례적 선택)
    weights = [fitness(chrom) for chrom in population]
    mating_pool = random.choices(population, weights=weights, k=POP_SIZE)
    next_population = []
    for i in range(0, POP_SIZE, 2):
        parent1 = mating_pool[i]
        parent2 = mating_pool[i+1]
        # 단순 1점 교차
        point = random.randint(1, GENE_LENGTH-1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        # 돌연변이
        def mutate(chrom):
            new_chrom = list(chrom)
            for j in range(GENE_LENGTH):
                if random.random() < MUT_RATE:
                    new_chrom[j] = '1' if new_chrom[j] == '0' else '0'
            return ''.join(new_chrom)
        child1 = mutate(child1); child2 = mutate(child2)
        next_population += [child1, child2]
    population = next_population  # 세대 교체

# 최종 결과
best = max(population, key=fitness)
print("최적 개체:", best, "적합도:", fitness(best))

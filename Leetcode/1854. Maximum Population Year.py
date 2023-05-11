# Leetcode # 1854. Maximum Population Year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = dict()
        for birth, death in logs:
            for year in range(birth, death):
                if year not in population:
                    population[year] = 0
                population[year] += 1
        max_year, max_cnt = 0, 0
        for year in sorted(population.keys()):
            if population[year] > max_cnt:
                max_year, max_cnt = year, population[year]
        return max_year

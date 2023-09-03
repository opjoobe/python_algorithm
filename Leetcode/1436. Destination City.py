# Leetcode # 1436. Destination City

''' Solution 1 '''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure, arrival = set(), set()
        for city_a, city_b in paths:
            departure.add(city_a)
            arrival.add(city_b)
        return (arrival - departure).pop()
        
''' Solution 2 : 1 Line '''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return ({path[1] for path in paths} - {path[0] for path in paths}).pop()

''' Solution 3 : use zip and asterisk '''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures, arrivals = map(set, zip(*paths))
        return max(arrivals - departures)

'''
paths = [['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]
*paths = ['London', 'New York'] ['New York', 'Lima'] ['Lima', 'Sao Paulo']
zip(*paths) = ('London', 'New York', 'Lima'), ('New York', 'Lima', 'Sao Paulo')
'''
        
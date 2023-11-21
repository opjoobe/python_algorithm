# Leetcode # 2363. Merge Similar Items
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item1_dict, item2_dict = dict(items1), dict(items2)
        return [[val, item1_dict.get(val, 0) + item2_dict.get(val, 0)] for val in sorted(set(item1_dict.keys()).union(set(item2_dict.keys())))]
    
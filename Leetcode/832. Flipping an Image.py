# Leetcode # 832. Flipping an Image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        return [list(map(lambda x : 0 if x else 1, row[::-1])) for row in image]

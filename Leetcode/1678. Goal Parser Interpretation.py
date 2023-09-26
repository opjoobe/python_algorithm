# Leetcode # 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        goal_mapping = {"()":"o", "(al)":"al"}
        return re.sub(r'\(\)|\(al\)', lambda x: goal_mapping[x.group()], command)
    
"""
multiple substitution in re.sub => use lambda with mapper(dictionary)
"""
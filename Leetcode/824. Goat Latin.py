# Leetcode # 824. Goat Latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def wordToGoatLatin(rank: int, word: str):
            if word[0].lower() not in 'aeiou':
                word = word[1:] + word[0]
            return word + 'ma' + 'a' * rank
        return ' '.join([wordToGoatLatin(rank, word) for rank, word in enumerate(sentence.split(), 1)])
# Leetcode # 2325. Decode the Message

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = ' abcdefghijklmnopqrstuvwxyz'
        secret_map = {' ':' '}
        for letter in key:
            if letter in secret_map:
                continue
            secret_map[letter] = alphabets[len(secret_map)]
        return ''.join([secret_map[letter] for letter in message])
        
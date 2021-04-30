#WORK
from collections import defaultdict
#comment
class Solution:
    #recursively search from each letter on the board if it matches the word.
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    found = self.recursive_search(board, i, j, word, 1, {(i,j)})
                    if found:
                        return True
        return False
                    
    #Similar to DFS, but in all directions possible.
    def recursive_search(self, board, i, j, word, idx, visited):
        if idx == len(word):
            return True
        print(word[idx])
        a, b = len(board), len(board[0])
        if i + 1 < a and (i + 1, j) not in visited and board[i + 1][j] == word[idx]:
            visited.add((i + 1,j))
            if self.recursive_search(board, i + 1, j, word, idx+1, visited):
                return True
        if j + 1 < b and (i, j + 1) not in visited and board[i][j + 1] == word[idx]:
            visited.add((i,j + 1))
            if self.recursive_search(board, i, j + 1, word, idx+1, visited):
                return True
        if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == word[idx]:
            visited.add(((i - 1),j))
            if self.recursive_search(board, i - 1, j, word, idx+1, visited):
                return True
        if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == word[idx]:
            visited.add((i,j - 1))
            if self.recursive_search(board, i, j - 1, word, idx+1, visited):
                return True
        visited.remove((i,j))
        return False
        
        
#test commit        

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxes = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] not in rows[r] and board[r][c] not in cols[c] and board[r][c] not in boxes[(r//3, c//3)]:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        boxes[(r//3, c//3)].add(board[r][c])
                    else:
                        return False
                    
        return True
                        
                
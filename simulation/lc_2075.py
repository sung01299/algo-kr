class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        self.rows = rows
        self.cols = len(encodedText) // self.rows
        self.board = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        if len(encodedText) == 0:
            return encodedText
        if rows == 1:
            return encodedText

        idx = 0
        for r in range(self.rows):
            for c in range(self.cols):
                self.board[r][c] = encodedText[idx]
                idx += 1

        res = ''
        for i in range(self.cols):
            res += self.decipher(i)

        return res.rstrip()

    def decipher(self, idx):
        res = ''
        x, y = 0, idx
        while True:
            if x > self.rows - 1 or y > self.cols - 1:
                break
            res += self.board[x][y]
            x += 1
            y += 1
        return res
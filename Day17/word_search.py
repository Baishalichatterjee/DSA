class Solution:
    def search(self, board: List[List[str]], word: str,i:int,j:int,n:int,m:int,k:int)->bool:
        if k == len(word):
            return True;
        if i<0 or i==n or j<0 or j==m or board[i][j]!=word[k]:
            return False;
        ch = board[i][j];
        board[i][j]='#';
        found = (
            self.search(board,word,i+1,j,n,m,k+1) or
            self.search(board,word,i-1,j,n,m,k+1) or
            self.search(board,word,i,j+1,n,m,k+1) or
            self.search(board,word,i,j-1,n,m,k+1)
        )
        board[i][j] = ch;
        return found;

    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board);
        m=len(board[0]);
        i=0;
        j=0;
        k=0;
        for i in range(0,n):
            for j in range(0,m):
                if board[i][j] == word[k]:
                    if self.search(board,word,i,j,n,m,k):
                        return True;
        
        return False;
        
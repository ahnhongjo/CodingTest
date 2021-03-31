package Level2;

public class largeSquare {
	public int solution(int [][]board)
    {
        System.out.println("Hello Java");
        
        int row=board.length;
        int col=board[0].length;
        int large=0;
        
        for(int i=0;i<row-large;i++) {
        	for(int j=0;j<col-large;j++) {
        		large=largeNum(i, j, board,large);
        	}
        }
        return large*large;
    }
	
	int largeNum(int i,int j, int[][]board,int large) {
		while(true) {
			for(int x=i;x<i+large+1;x++) {
				for(int y=j;y<j+large+1;y++) {
					if(x>=board.length || y>=board[0].length || board[x][y]==0) {
						return large;
					}
				}		
			}
			large++;
		}
	}
	
}



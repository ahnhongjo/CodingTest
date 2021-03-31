package Level2;

public class largeSquare2 {
	public int solution(int [][]board)
    {
        int answer = 1234;
        
        int row=board[0].length;
        int col=board.length;
        int[][]answerSheet = new int[col][row];
        
        int max=0;
        
        for(int i=0;i<row;i++) {
        	answerSheet[0][i]=board[0][i];
        }
        
        for(int i=0;i<col;i++) {
        	answerSheet[i][0]=board[i][0];
        }
        
        for(int i=1;i<col;i++) {
        	for(int j=1;j<row;j++) {
        		if(board[i][j]==1) {
        			answerSheet[i][j]=minValue(answerSheet[i-1][j-1],answerSheet[i][j-1],answerSheet[i-1][j])+1;
        			if (answerSheet[i][j]>max)
        				max=answerSheet[i][j];
        		}
        	}
        }

        return max*max;
    }
	
	int minValue(int a,int b,int c) {
		
		int min=a;
		if(min>b)
			min=b;
		if(min>c)
			min=c;
		
		return min;
	}
}

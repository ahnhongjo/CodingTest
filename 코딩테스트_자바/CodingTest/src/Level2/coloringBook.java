package Level2;

import java.util.ArrayList;
import java.util.Collections;


public class coloringBook {
	public int[][] group;
	public int[][] check;
	ArrayList<Integer> groupCnt = new ArrayList<>();
	
	public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        group=new int[m][n];
        check = new int[m][n];
        
        
        //배열 두개 초기화
        for(int i=0;i<m;i++) {
        	for(int j=0;j<n;j++) {
        		group[i][j]=-1;
        		check[i][j]=0;
        	}
        }
        
        //배열 확인
        for(int i=0;i<m;i++) {
        	for(int j=0;j<n;j++) {
        		if(picture[i][j]==0) {
        			check[i][j]=1;
        			continue;
        		}
        		
        		if(check[i][j]==0) {
        			groupCnt.add(0);
        			group[i][j]=groupCnt.size()-1;
        			this.checkDFS(i,j,picture[i][j],group[i][j],picture);
        		}
        	}
        }
        
        Collections.sort(groupCnt);

        int[] answer = new int[2];
        answer[0] = groupCnt.size();
        answer[1] = groupCnt.get(answer[0]-1);
        return answer;
    }
	
	public void checkDFS(int i, int j, int color, int groupNum, int[][] picture) {
		
		if(i<0||i>picture.length-1||j<0||j>picture[0].length-1)
			return;
		
		if(check[i][j]==1)
			return;
		
		if(picture[i][j]!=color)
			return;
		
		if(picture[i][j]==color) {
			group[i][j]=groupNum;
			groupCnt.set(groupNum, groupCnt.get(groupNum)+1);
			check[i][j]=1;
		}
		
		this.checkDFS(i+1, j, picture[i][j], group[i][j], picture);
		this.checkDFS(i, j+1, picture[i][j], group[i][j], picture);
		this.checkDFS(i-1, j, picture[i][j], group[i][j], picture);
		this.checkDFS(i, j-1, picture[i][j], group[i][j], picture);
	}
}

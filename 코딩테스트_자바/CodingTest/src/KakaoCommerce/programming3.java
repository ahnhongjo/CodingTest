package KakaoCommerce;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class programming3 {
	public int[] solution(int n, int[] passenger, int[][] train) {
		
		line[] trainInfo = new line[n];
		int[] passengerNum=new int[n];
		Queue<Integer> queue = new LinkedList<>(); 
		queue.add(0);
		
		passengerNum[0]=passenger[0];
		
		for(int i=0;i<n;i++) {
			trainInfo[i]=new line(i);
		}
		
		for(int[] info:train) {
			trainInfo[info[0]-1].addLine(info[1]-1);
			trainInfo[info[1]-1].addLine(info[0]-1);		
		}
		
		while(!queue.isEmpty()) {
			int root=queue.poll();
			ArrayList<Integer> tmplist=trainInfo[root].getLinkNum();
			
			for(int lineNum:tmplist) {
				if(passengerNum[lineNum]==0) {
					passengerNum[lineNum]=passenger[lineNum]+passengerNum[root];
					queue.add(lineNum);
				}
			}
		}
		
        int[] answer = {1,passengerNum[0]};
        
        for(int i=0;i<passengerNum.length;i++) {
        	if(answer[1]<=passengerNum[i] && answer[0]-1<i) {
        		answer[0]=i+1;
        		answer[1]=passengerNum[i];
        	}
        }

        return answer;
    }
	
	class line{
		
		int root;
		ArrayList<Integer> linkNum=new ArrayList<>();
		
		public line(int root) {
			this.root = root;
		}
		
		public void addLine(int lineNum) {
			linkNum.add(lineNum);
		}
		
		
		public int getRoot() {
			return root;
		}

		public void setRoot(int root) {
			this.root = root;
		}

		public ArrayList<Integer> getLinkNum() {
			return linkNum;
		}

		public void setLinkNum(ArrayList<Integer> linkNum) {
			this.linkNum = linkNum;
		}

	}
}

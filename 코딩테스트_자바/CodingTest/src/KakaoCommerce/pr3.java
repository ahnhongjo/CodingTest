package KakaoCommerce;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class pr3 {
	public int[] solution(int n, int[] passenger, int[][] train) {
		
		ArrayList<Integer>[] trainInfo = new ArrayList[n];
		int[] passengerNum=new int[n];
		Queue<Integer> queue = new LinkedList<>(); 
		queue.add(0);
		
		passengerNum[0]=passenger[0];
		for(ArrayList<Integer>a:trainInfo) {
			a=new ArrayList<>();
		}
		
		for(int[] info:train) {
			trainInfo[info[0]-1].add(info[1]-1);
			trainInfo[info[1]-1].add(info[0]-1);		
		}
		
		while(!queue.isEmpty()) {
			int root=queue.poll();
			ArrayList<Integer> tmplist=trainInfo[root];
			
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
}

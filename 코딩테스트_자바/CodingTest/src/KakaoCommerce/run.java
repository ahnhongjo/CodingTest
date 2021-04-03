package KakaoCommerce;

import java.util.Arrays;

public class run {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		pr3 test=new pr3();
		
		int n=6;
		int[] passenger= {1,1,1,1,1,1};
		int[][] train = {{1,2},{1,3},{1,4},{3,5},{3,6}};
		
		int[] result=test.solution(n, passenger, train);
		
		System.out.println(Arrays.toString(result));

	}

}

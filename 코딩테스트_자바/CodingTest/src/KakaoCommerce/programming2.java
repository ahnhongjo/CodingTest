package KakaoCommerce;
public class programming2 {
	public int solution(int[][] needs, int r) {
        
		int num=needs[0].length;
		
		int[] sumNeeds=new int[num];
		int[] buyList= new int[r];
		
		for(int[] need:needs) {
			for(int i=0;i<need.length;i++) {
				sumNeeds[i]+=need[i];
			}
		}
		
		int tmpidx;
		int max;
		int[] check=new int[num];
		for(int j=0;j<r;j++) {
			tmpidx=0;
			max=0;
				
			for(int i=0;i<num;i++) {
				if(check[i]==0 && max<sumNeeds[i]) {
					tmpidx=i;
					max=sumNeeds[i];
				}
			}
			
			check[tmpidx]=1;
			buyList[j]=tmpidx;
		}
		
		int makeWan=0;
		
		for(int[] need:needs) {
			if(canMake(need, buyList))
					makeWan++;
		}
		
        return makeWan;
    }
	
	boolean canMake(int[] parts, int[] buylists){
		
		for(int i=0;i<parts.length;i++) {
			if(parts[i]==1 && !isIn(i,buylists))
				return false;
		}
		
		return true;
	}
	
	boolean isIn(int part, int[]buylists) {
		for(int buylist:buylists) {
			if(buylist==part)
				return true;
		}
		
		return false;
	}
}


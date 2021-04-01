package Level3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class jewelShopping {
	public int[] solution(String[] gems) {
        
        ArrayList<String> gemKind = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String g:gems) {
        	if(!gemKind.contains(g)) {
        		gemKind.add(g);
        		map.put(g, 0);
        	}
        }

        int min=gems.length+1;
        int start=0;
        int end=0;
        int num=0;
        int kind=gemKind.size();
        int[] startEnd = {0,0};
        boolean flag=false;
        
        while(end!=gems.length) {
        	String tmp=gems[end];
        	int cnt=map.get(tmp);
        	
    		map.put(tmp, cnt+1);
    		if(cnt==0) {
    			num++;
    		}
    		
    		if(num==kind)
    			flag=true;
    		
        	if(flag) {
        		while(map.get(gems[start])>1) {
        			map.put(gems[start], map.get(gems[start])-1);
        			start++;
        		}
        		
        		if(min>end-start+1) {
        			min=end-start+1;
        			startEnd[0]=start;
        			startEnd[1]=end;
        		}
        	}
        	end++;
        }
        startEnd[0]+=1;
        startEnd[1]+=1;
        System.out.println(Arrays.toString(startEnd));
        return startEnd;
    }
}

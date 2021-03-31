package Level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;

public class expressionMax {
	public long solution(String expression) {
		
		ArrayList<String> exp=new ArrayList<>();
		ArrayList<Integer> num=new ArrayList<>();
		int[] primul= {0,0,1,1,2,2};
		int[] priplus= {1,2,0,2,0,1};
		int[] prisub= {2,1,2,0,1,0};
		
		String number="";
		for(int i=0;i<expression.length();i++) {
			if(expression.charAt(i)=='*'||expression.charAt(i)=='+'||expression.charAt(i)=='-') {
				exp.add(number);
				exp.add(expression.charAt(i)+"");
				number="";
			}
			else {
				number=number+expression.charAt(i);
			}
		}	
		exp.add(number);
		
		String[] postfix = new String[6];
		
		long max=0;
		
		for(int i=0;i<6;i++) {
			HashMap<String, Integer> priority = new HashMap<>();
			Stack<String> stack=new Stack<>();
			
			priority.put("*", primul[i]);
			priority.put("-", prisub[i]);
			priority.put("+", priplus[i]);
			postfix[i]=exp.get(0);
			
			for(int j=1;j<exp.size();j++) {
				
				if(exp.get(j).equals("*") || exp.get(j).equals("+")||exp.get(j).equals("-")) {
					if (stack.empty()) {
						stack.push(exp.get(j));
					}
					
					else if(priority.get(stack.peek())<priority.get(exp.get(j))) {
						stack.push(exp.get(j));
					}
					
					else if(priority.get(stack.peek())>=priority.get(exp.get(j))) {
						while(!stack.empty() && priority.get(stack.peek())>=priority.get(exp.get(j))) {
							postfix[i]=postfix[i]+","+stack.pop();
						}
						stack.push(exp.get(j));
					}
				}
				
				else {
					postfix[i]=postfix[i]+","+exp.get(j);
				}
			}
			
			while(!stack.empty()) {
				postfix[i]=postfix[i]+","+stack.pop();
			}
			
			long tmp=calcul(postfix[i]);
			
			if(max<tmp) {
				max=tmp;
			}
		}

        return max;
    }
	
	long calcul(String s) {
		
		Stack<Long> stack = new Stack<>();
		String[] splS=s.split(",");
		
		for(int i=0;i<splS.length;i++) {
			if(splS[i].equals("+")) {
				long a=stack.pop();
				long b=stack.pop();
				stack.push(a+b);
			}
			else if(splS[i].equals("-")) {
				long a=stack.pop();
				long b=stack.pop();
				stack.push(b-a);
			}
			else if(splS[i].equals("*")) {
				long a=stack.pop();
				long b=stack.pop();
				stack.push(a*b);
			}
			
			else {
				stack.push(Long.parseLong(splS[i]));
			}
		}
		
		return Math.abs(stack.pop());
	}
}

package com.example.day11.leetcode_150;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 逆波兰表达式
 */
public class Solution {
    Deque<Integer> stack = new ArrayDeque<>();
    public int evalRPN(String[] tokens) {
        for(String token : tokens){
            if(token.equals("+")){
                stack.push(stack.pop() + stack.pop());
            }else if(token.equals("-")){
                stack.push(-stack.pop() + stack.pop());
            }else if(token.equals("*")){
                stack.push(stack.pop() * stack.pop());
            }else if(token.equals("/")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b/ a);
            }else{
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
    public static void main(String[] args) {
        String[] tokens = {"4","13","5","/","+"};
        System.out.println(new Solution().evalRPN(tokens));
    }
}

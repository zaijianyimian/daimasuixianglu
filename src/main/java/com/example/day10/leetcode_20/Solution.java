package com.example.day10.leetcode_20;

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    Deque<Character> deque = new ArrayDeque<>();
    public boolean isValid(String s) {
        for(char c : s.toCharArray()){
            if(deque.isEmpty() || c == '(' || c == '[' || c == '{'){
                deque.addLast(c);
            }
            else if(c == ')' && deque.peekLast() == '('){
                deque.pollLast();
            }
            else if(c == ']' && deque.peekLast() == '['){
                deque.pollLast();
            }
            else if(c == '}' && deque.peekLast() == '{'){
                deque.pollLast();
            }
            else{
                return false;
            }
        }
        return deque.isEmpty();
    }
}
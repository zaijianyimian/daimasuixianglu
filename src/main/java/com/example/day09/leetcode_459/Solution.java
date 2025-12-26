package com.example.day09.leetcode_459;

public class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        for(int i = 1;i<=n/2;i++){
            if(n % i ==0){
                boolean flag = true;
                for(int j = i; j < n;j ++){
                    if(s.charAt(j)!=s.charAt(j-i)){
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    return flag;
                }
            }
        }
        return false;
    }
}
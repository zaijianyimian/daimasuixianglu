package com.example.day08.leetcode_541;

/**
 * 反转字符串2
 */
class Solution {
    public String reverseStr(String s, int k) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        for(int i = 0;i < n;i += 2 * k){
            reverse(arr,i,Math.min(i + k,n) - 1);
        }
        return new String(arr);
    }

    private void reverse(char[] s,int l,int r){
        while(l < r){
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l++;
            r --;
        }
    }

}
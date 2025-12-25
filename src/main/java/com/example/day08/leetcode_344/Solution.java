package com.example.day08.leetcode_344;

/**
 * 反转字符串
 */
class Solution {
    public void reverseString(char[] s) {
        int i = 0,j = s.length - 1;
        while(i < j){
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i ++ ;
            j --;
        }
    }
}
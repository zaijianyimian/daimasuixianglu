package com.example.day6.leetcode_242;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int[] arr = new int[26];
        for(char i : s.toCharArray()){
            arr[i - 'a'] ++;
        }
        for(char j : t.toCharArray()){
            arr[j - 'a']--;
        }
        for(int i : arr){
            if(i != 0){
                return false;
            }
        }
        return true;
    }
}
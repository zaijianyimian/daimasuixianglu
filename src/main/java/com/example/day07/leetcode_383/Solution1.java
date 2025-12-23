package com.example.day07.leetcode_383;

import java.util.HashMap;
import java.util.Map;

public class Solution1 {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length()){
            return false;
        }
        int[] arr = new int[26];
        for(char i : magazine.toCharArray()){
            arr[i - 'a'] ++;
        }
        for(char j : ransomNote.toCharArray()){
            if(arr[j - 'a'] > 0){
                arr[j - 'a']--;
            }
            else{
                return false;
            }
        }
        return true;

    }
}

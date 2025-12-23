package com.example.day07.leetcode_383;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character,Integer> map = new HashMap<>();
        for(char c : magazine.toCharArray()){
            map.put(c,map.getOrDefault(c,0) + 1);
        }
        for(char c : ransomNote.toCharArray()){
            if(map.getOrDefault(c,0) == 0){
                return false;
            }
            map.put(c,map.getOrDefault(c,0) - 1);
        }
        for(Map.Entry<Character,Integer> entry : map.entrySet()){
            if(entry.getValue() < 0){
                return false;
            }
        }
        return true;
    }
}
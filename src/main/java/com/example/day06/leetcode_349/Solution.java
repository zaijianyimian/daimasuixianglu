package com.example.day6.leetcode_349;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        for(int i : nums1){
            set1.add(i);
        }
        for(int i : nums2){
            set2.add(i);
        } 
        List<Integer> list = new ArrayList<>();
        for(int i : set1){
            if(set2.contains(i)){
                list.add(i);
            }
        }
        int[] arr = new int[list.size()];
        int ind = 0;
        for(int i : list){
            arr[ind] = i;
            ind ++;
        }
        return arr;
    }
}
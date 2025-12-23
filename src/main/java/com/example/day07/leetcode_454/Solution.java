package com.example.day07.leetcode_454;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer,Integer> map1 = new HashMap<>();
        Map<Integer,Integer> map2 = new HashMap<>();
        int n = nums1.length;
        for(int i = 0;i < n;i ++){
            for(int j = 0;j < n;j ++){
                map1.put(nums1[i] + nums2[j],map1.getOrDefault(nums1[i] + nums2[j],0) + 1);
            }
        }
        for(int i = 0;i < n;i ++){
            for(int j = 0;j < n;j ++){
                map2.put(nums3[i] + nums4[j],map2.getOrDefault(nums3[i] + nums4[j],0) + 1);
            }
        }
        int res = 0;
        for(Map.Entry<Integer,Integer> entry : map1.entrySet()){
            if(map2.containsKey(-entry.getKey())){
                res += entry.getValue() * map2.get(-entry.getKey());
            }
        }
        return res;
    }
}

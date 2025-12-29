package com.example.day11.leetcode_347;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ans = new int[k];
        Map<Integer,Integer> map = new HashMap<>();
        for(int i = 0;i < nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0) + 1);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] - b[1]);
        for(var x : map.entrySet()){
            int[] tmp = new int[2];
            tmp[0] = x.getKey();
            tmp[1] = x.getValue();
            pq.add(tmp);
            if(pq.size() > k){
                pq.poll();
            }
        }
        for(int i = 0;i < k;i ++){
            ans[i] = pq.poll()[0];
        }
        return ans;
    }
}

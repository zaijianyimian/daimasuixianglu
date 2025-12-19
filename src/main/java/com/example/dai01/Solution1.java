package com.example.dai01;

public class Solution1 {
    public int minSubArrayLen(int target, int[] nums) {
        int start = 0, end = 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;
        while (end < nums.length) {
            while (end < nums.length && sum < target) {
                sum += nums[end];
                end++;
            }
            while(sum >= target) {
                res = Math.min(res, end - start);
                sum -= nums[start];
                start++;
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
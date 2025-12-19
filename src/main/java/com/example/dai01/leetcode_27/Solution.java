package com.example.dai01.leetcode_27;

/**
 * 代码随想录day01第二题,移除元素
 */
public class Solution {
    public int removeElement(int[] nums,int val){
        int l = 0;
        for(int r = 0;r < nums.length; r ++){
            if(nums[r] != val){
                nums[l] = nums[r];
                l ++;
            }
        }
        return l;
    }
}

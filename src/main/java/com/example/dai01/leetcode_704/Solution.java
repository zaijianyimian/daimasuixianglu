package com.example.dai01.leetcode_704;

/**
 * 代码随想录dai01第一题,二分查找.
 */
class Solution {
    public int search(int[] nums, int target) {
        int index = -1;
        int l = 0,r = nums.length - 1;
        while(l < r){
            int mid = l + (r - l) / 2;
            if(nums[mid] == target){
                index = mid;
                break;
            }else if(nums[mid] > target){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return index;
    }
}
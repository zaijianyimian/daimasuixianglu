package com.example.dai01.leetcode_977;

/**
 * 代码随想录day01第三题,有序数组的平方
 */
public class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        int l = 0,r = n - 1;
        while(l <= r){
            int ansl = nums[l] * nums[l];
            int ansr = nums[r] * nums[r];
            if(ansl >= ansr){
                arr[n - 1] = ansl;
                l ++;
            }else{
                arr[n - 1] = ansr;
                r --;
            }
            n--;//一定要记得减一下,要不就全覆盖到n - 1上了
        }
        return arr;
    }
}

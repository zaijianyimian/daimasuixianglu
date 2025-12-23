package com.example.day07.leetcode_18;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0;i < n;i ++){
            if (nums[i] > target && nums[i] >= 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for(int j = i + 1;j < n;j ++){
                if(nums[i] + nums[j] > target && nums[i] + nums[j] >= 0){
                    break;
                }
                if(j > i + 1 && nums[j] == nums[j - 1]){
                    continue;
                }
                long tmp = nums[i] + nums[j];
                int l = j + 1;
                int r = n - 1;
                while(l < r){
                    if(nums[l] + nums[r] > target - tmp){
                        r --;
                    }else if(nums[l] + nums[r] < target - tmp){
                        l ++;
                    }
                    else{
                        res.add(Arrays.asList(nums[i],nums[j],nums[l],nums[r]));
                        while(l < r && nums[l] == nums[l + 1])l++;
                        while(l < r && nums[r] == nums[r - 1])r--;
                        r--;
                        l++;
                    }
                }
                while (j < n - 1 && nums[j] == nums[j + 1]) j++;
            }
            while (i < n - 1 && nums[i] == nums[i + 1]) i++;
        }
        return res;
    }
}

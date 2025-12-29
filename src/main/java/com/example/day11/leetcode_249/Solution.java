package com.example.day11.leetcode_249;

import java.util.*;

/**
 * 滑动窗口最大值
 */
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums.length == 0 || k == 0)return new int[0];
        int[] ans = new int[nums.length - k + 1];
        Deque<Integer> deque = new LinkedList<>();
        for(int i = 0; i < k; i++){
            while(!deque.isEmpty() && deque.peekLast() < nums[i])deque.pollLast();
            deque.addLast(nums[i]);
        }
        ans[0] = deque.peekFirst();
        for(int i = k; i < nums.length; i++){
            if(deque.peekFirst() == nums[i - k])deque.pollFirst();
            while(!deque.isEmpty() && deque.peekLast() < nums[i])deque.pollLast();
            deque.addLast(nums[i]);
            ans[i - k + 1] = deque.peekFirst();
        }
        return ans;
    }
}
package com.example.day6.leetcode_202;

import java.util.HashSet;
import java.util.Set;

/**
 * leetcode 202
 */
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while(!set.contains(n)){
            set.add(n);
            n = getSum(n);
            if(n == 1){
                return true;
            }
        }
        return false;
    }
    private int getSum(int n){
        int sum = 0;
        while(n != 0){
            int target = n % 10;
            sum += target * target;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 19;
        System.out.println(new Solution().isHappy(n));
    }
}
package com.example.day15.leetcode_110;

import com.example.day13.leetcode_226.TreeNode;

class Solution {
    public boolean isBalanced(TreeNode root) {
        return depth(root) != -1;
    }
    private int depth(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = depth(root.left);
        if (left == -1){
            return -1;
        }
        int right = depth(root.right);
        if (right == -1){
            return -1;
        }
        int result = Math.abs(left - right);
        return result > 1 ? -1 : Math.max(left,right) + 1;
    }
}
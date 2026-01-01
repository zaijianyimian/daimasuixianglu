package com.example.day13.leetcode_101;

import com.example.day13.leetcode_226.TreeNode;

public class Solution {
    public boolean isSymmetric(TreeNode root) {
        return compare(root.left,root.right);
    }
    private boolean compare(TreeNode left,TreeNode right){
        if(left == null && right == null)return true;
        if(left == null && right != null)return false;
        if(left != null && right == null)return false;
        if(left.val != right.val)return false;
        boolean outside = compare(left.left,right.right);
        boolean inside = compare(left.right,right.left);
        return outside && inside;
    }
}
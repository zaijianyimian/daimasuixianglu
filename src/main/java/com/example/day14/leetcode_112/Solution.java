package com.example.day14.leetcode_112;

import com.example.day13.leetcode_226.TreeNode;

class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null){
            return false;
        }
        if(root.left == null && root.right == null){
            return targetSum == root.val;
        }
        if(root.left != null){
            if(hasPathSum(root.left, targetSum - root.val)){
                return true;
            }
        }
        if(root.right != null){
            if(hasPathSum(root.right, targetSum - root.val)){
                return true;
            }
        }
        return false;

    }
}
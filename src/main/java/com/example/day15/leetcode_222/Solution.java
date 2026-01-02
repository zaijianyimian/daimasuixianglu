package com.example.day15.leetcode_222;

import com.example.day13.leetcode_226.TreeNode;

class Solution {
    public int countNodes(TreeNode root) {
        if(root == null){
            return 0;
        }
        TreeNode lef = root.left;
        TreeNode rig = root.right;
        int leftHeight = 0, rightHeight = 0;
        while (lef != null){
            leftHeight++;
            lef = lef.left;
        }
        while (rig != null){
            rightHeight++;
            rig = rig.right;
        }
        if (leftHeight == rightHeight){
            return (2 << leftHeight) - 1;
        }
        int leftNum = countNodes(root.left);
        int rightNum = countNodes(root.right);
        return leftNum + rightNum + 1;
    }
}
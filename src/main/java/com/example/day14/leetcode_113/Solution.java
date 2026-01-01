package com.example.day14.leetcode_113;

import com.example.day13.leetcode_226.TreeNode;

import java.util.LinkedList;
import java.util.List;

public class Solution {
    LinkedList<List<Integer>> res = new LinkedList<>();
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        find(root, targetSum);
        return res;
    }
    private void find(TreeNode root, int targetSum){
        if(root == null)return;
        path.add(root.val);
        targetSum -= root.val;
        if(root.left == null && root.right == null && targetSum == 0){
            res.add(new LinkedList<>(path));
        }
        find(root.left, targetSum);
        find(root.right, targetSum);
        path.removeLast();
    }
}
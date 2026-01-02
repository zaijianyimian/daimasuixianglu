package com.example.day15.leetcode_257;

import com.example.day13.leetcode_226.TreeNode;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if(root == null){
            return res;
        }
        List<Integer> path = new ArrayList<>();
        dfs(res,path,root);
        return res;
    }

    private void dfs(List<String> res, List<Integer> path, TreeNode root) {
        path.add(root.val);
        if(root.left == null && root .right == null){
            StringBuilder sb = new StringBuilder();
            for(int i = 0;i < path.size() - 1;i ++){
                sb.append(path.get(i)).append("->");
            }
            sb.append(path.get(path.size() - 1));
            res.add(sb.toString());
            return;
        }
        if(root.left != null){
            dfs(res,path,root.left);
            path.remove(path.size() - 1);
        }
        if(root.right != null){
            dfs(res,path,root.right);
            path.remove(path.size() - 1);
        }
    }
}
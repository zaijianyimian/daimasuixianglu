package com.example.day03.leetcode_203;

/**
 * 203. 移除链表元素
 */
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    public ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode p = head;
        while(p.next != null){
            if(p.next.val == val){
                p.next = p.next.next;
            }else{
                p = p.next;
            }
        }
        return head;
    }
}


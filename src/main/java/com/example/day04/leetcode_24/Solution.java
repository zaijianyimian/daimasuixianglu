package com.example.day04.leetcode_24;

/**
 * 两两交换链表的节点
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;
        ListNode tmp = null;
        ListNode first, second;
        while(cur.next!= null && cur.next.next != null){
            tmp = cur.next.next.next;
            first = cur.next;
            second = cur.next.next;
            cur.next = second;
            second.next = first;
            first.next = tmp;
            cur = first;
        }
        return dummy.next;
    }
}

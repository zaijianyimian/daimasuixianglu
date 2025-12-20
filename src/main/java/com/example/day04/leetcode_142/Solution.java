package com.example.day04.leetcode_142;

import com.example.day04.leetcode_24.ListNode;

/**
 * 力扣142环形链表2,快慢指针
 */
class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head == null || head.next == null){
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        int flag = 0;
        ListNode cur = null;
        while(fast != null && fast.next != null){
            if(flag != 0 && slow == fast){
                cur = slow;
                break;
            }
            flag++;
            slow = slow.next;
            fast = fast.next.next;
        }
        slow = head;
        if(cur == null){
            return null;
        }
        while(slow != cur){
            slow = slow.next;
            cur = cur.next;
        }
        return slow;
    }
}

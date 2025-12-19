package com.example.day03.leetcode_206;

class Solution {
    public ListNode2 reverseList(ListNode2 head) {
        ListNode2 cur = head;
        ListNode2 pre = null;
        while(cur != null){
            ListNode2 tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
}
 class ListNode2 {
      int val;
      ListNode2 next;
      ListNode2() {}
      ListNode2(int val) { this.val = val; }
      ListNode2(int val, ListNode2 next) { this.val = val; this.next = next; }
 }
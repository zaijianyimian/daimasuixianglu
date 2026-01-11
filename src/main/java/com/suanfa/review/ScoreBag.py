class Solution:
    def __init__(self,w: int,v : int):
        self.w = w
        self.v = v
    def fractionalKnapsack(self,wgt: list[int],val : list[int],cap : int) -> int:
        items = [Solution(w,v) for w , v in zip(wgt,val)]
        # 按照分数进行排序,价值密度越高越靠前
        items.sort(key=lambda item : item.v / item.w)
        res = 0
        for item in items:
            if item.w  <= cap:
                res +=  item.v
                cap -= item.w
            else:
                res += (item.v/item.w) * cap
                break
        return res
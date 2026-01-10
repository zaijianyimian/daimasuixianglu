# 回溯: 一般与递归一起使用
纯暴力搜索,不是高效算法,
组合,切割,子集,排列,棋盘
抽象成图形结构
回溯法通常可以抽象为n叉树结构
业界叫 backtracking
If(终止条件):
    # todo收集结果集
    return
for(集合元素):
    # 处理节点
    递归,
    回溯

递归函数参数返回值
确定终止条件
单层递归逻辑
void backtracking(参数) {
    一维数组、二维数组、字符串
if(满足结束条件){
    # todo 满足条件，处理结果
收集结果集
for(i = 0;i < 参数.length;i++){
path.add(参数[i])
backtracking(参数)
path.removeLast()
}
# 剪枝:

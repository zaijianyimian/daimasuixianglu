# 并查集理论基础
将两个元素添加到同一个集合
判断元素是否在同一个集合里
，
if father[x] == x:
    return x
int father = find(x);

bool isSameSet(int x, int y) {
a = find(a)
b = find(b)
if (a == b) { 
return true;
}}

void join(int x, int y) {
a = find(a)
b = find(b)
if (a != b) {
father[a] = b;
}}
层数压缩：
修改，改为只有一个根节点，其他节点都指向根节点,不再需要指向下层节点
优化：
int find (int x) {
if father[x] == x :
return x
father[x] = find(father[x]);}
无向图才可以使用并查集

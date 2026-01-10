# 分割ip地址:
难点:获取对应串
void backtracking(s,startindex,pointSum):
if pointSum == 3:
    if isValid(s,startindex,s.size()-1)
        result.add(s);
    return;
for i in range(startindex,min(startindex+3,s.size())):
if isValid(s,startindex,i)
模拟切割过程
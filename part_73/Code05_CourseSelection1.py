# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 选课，树上01背包的普通解法
# 在大学里每个学生，为了达到一定的学分，必须从很多课程里选择一些课程来学习
# 在课程里有些课程必须在某些课程之前学习，如高等数学总是在其它课程之前学习
# 现在有 N 门功课，每门课有个学分，每门课有一门或没有直接先修课
# 若课程 a 是课程 b 的先修课即只有学完了课程 a，才能学习课程 b
# 一个学生要从这些课程里选择 M 门课程学习
# 问他能获得的最大学分是多少
# 测试链接 : https://www.luogu.com.cn/problem/P2014
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 普通解法，邻接表建图 + 相对好懂的动态规划
# 几乎所有题解都是普通解法的思路，只不过优化了常数时间、做了空间压缩
# 但时间复杂度依然是O(n * 每个节点的孩子平均数量 * m的平方)
class Code05_CourseSelection1:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'graph': 'graph', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    MAXN = 0
    nums = None
    graph = None
    dp = None
    n = 0
    m = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i <= n):
            jcall(jcall(Code05_CourseSelection1.graph, 'get', i), 'clear')
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            # 节点编号从0~n
            Code05_CourseSelection1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_CourseSelection1.m = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            Code05_CourseSelection1.build(Code05_CourseSelection1.n)
            i = jcast('int', 1)
            pre = 0
            while (i <= Code05_CourseSelection1.n):
                jcall(in_, 'nextToken')
                pre = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(jcall(Code05_CourseSelection1.graph, 'get', pre), 'add', i)
                jcall(in_, 'nextToken')
                Code05_CourseSelection1.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code05_CourseSelection1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i <= Code05_CourseSelection1.n):
            jset(Code05_CourseSelection1.dp, i, jarray('int', [jcast('int', jadd(jcall(jcall(Code05_CourseSelection1.graph, 'get', i), 'size'), 1)), jcast('int', jadd(Code05_CourseSelection1.m, 1))]))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code05_CourseSelection1.n):
            j = jcast('int', 0)
            while (j < jget(Code05_CourseSelection1.dp[i], 'length')):
                k = jcast('int', 0)
                while (k <= Code05_CourseSelection1.m):
                    jset(Code05_CourseSelection1.dp[i][j], k, jcast('int', (-1)))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code05_CourseSelection1.f(0, jcall(jcall(Code05_CourseSelection1.graph, 'get', 0), 'size'), Code05_CourseSelection1.m))

    # 当前来到i号节点为头的子树
    # 只在i号节点、及其i号节点下方的前j棵子树上挑选节点
    # 一共挑选k个节点，并且保证挑选的节点连成一片
    # 返回最大的累加和
    @staticmethod
    def f(i, j, k):
        i = jcast('int', i)
        j = jcast('int', j)
        k = jcast('int', k)
        if (k == 0):
            return jcast('int', 0)
        if ((j == 0) or (k == 1)):
            return jcast('int', Code05_CourseSelection1.nums[i])
        if (Code05_CourseSelection1.dp[i][j][k] != jcast('int', (-1))):
            return jcast('int', Code05_CourseSelection1.dp[i][j][k])
        ans = jcast('int', Code05_CourseSelection1.f(i, jcast('int', (j - 1)), k))
        # 第j棵子树头节点v
        v = jcast('int', jcall(jcall(Code05_CourseSelection1.graph, 'get', i), 'get', jcast('int', (j - 1))))
        s = jcast('int', 1)
        while (s < k):
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code05_CourseSelection1.f(i, jcast('int', (j - 1)), jcast('int', (k - s))), Code05_CourseSelection1.f(v, jcall(jcall(Code05_CourseSelection1.graph, 'get', v), 'size'), s)))))
            s = jcast('int', (s + 1))
        jset(Code05_CourseSelection1.dp[i][j], k, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_CourseSelection1.MAXN = jcast('int', 301)
Code05_CourseSelection1.nums = jarray('int', [Code05_CourseSelection1.MAXN])
Code05_CourseSelection1.graph = None
Code05_CourseSelection1.graph = jnew('ArrayList')
i = jcast('int', 0)
while (i < Code05_CourseSelection1.MAXN):
    jcall(Code05_CourseSelection1.graph, 'add', jnew('ArrayList'))
    i = jcast('int', (i + 1))
Code05_CourseSelection1.dp = jarray('int', [Code05_CourseSelection1.MAXN, None, None])
Code05_CourseSelection1.n = jcast('int', 0)
Code05_CourseSelection1.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_CourseSelection1.main([])

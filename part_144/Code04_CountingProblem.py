# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 序列计数
# 有一个概念叫，最左端最大值位置，表示一段范围上
# 如果最大值有一个，那么最大值所在的位置，就是最左端最大值位置
# 如果最大值有多个，最左的那个所在的位置，就是最左端最大值位置
# 给定一个长度为n的数组A，那么必然存在等长的数组B，当选择同样的子范围时
# 两者在这段范围上，最左端最大值位置是相同的，不仅存在这样的数组B，而且数量无限多
# 现在要求，数组B中的每个值都在[1,m]范围，返回有多少个这样的数组，答案对 1000000007 取模
# 2 <= n、m <= 2 * 10^5    1 <= A[i] <= m    n * m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/CF1748E
# 测试链接 : https://codeforces.com/problemset/problem/1748/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_CountingProblem:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'arr': 'arr', 'left': 'left', 'right': 'right', 'stack': 'stack', 'tmp': 'tmp', 'n': 'n', 'm': 'm'}
    MOD = 0
    MAXN = 0
    # 所有数字
    arr = None
    # 笛卡尔树需要
    left = None
    right = None
    stack = None
    # tmp是动态规划的临时结果
    tmp = None
    n = 0
    m = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        top = jcast('int', 0)
        pos = 0
        while (i <= Code04_CountingProblem.n):
            pos = jcast('int', top)
            while ((pos > 0) and (Code04_CountingProblem.arr[Code04_CountingProblem.stack[pos]] < Code04_CountingProblem.arr[i])):
                pos = jcast('int', (pos - 1))
            if (pos > 0):
                jset(Code04_CountingProblem.right, Code04_CountingProblem.stack[pos], i)
            if (pos < top):
                Code04_CountingProblem.left[i] = jcast('int', Code04_CountingProblem.stack[jcast('int', jadd(pos, 1))])
            jset(Code04_CountingProblem.stack, (pos := jcast('int', (pos + (1)))), i)
            top = jcast('int', pos)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, dp):
        u = jcast('int', u)
        if (u == 0):
            return
        Code04_CountingProblem.dfs(Code04_CountingProblem.left[u], dp)
        Code04_CountingProblem.dfs(Code04_CountingProblem.right[u], dp)
        j = jcast('int', 1)
        while (j <= Code04_CountingProblem.m):
            Code04_CountingProblem.tmp[j] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', dp[Code04_CountingProblem.left[u]][jcast('int', (j - 1))]) * dp[Code04_CountingProblem.right[u]][j])), Code04_CountingProblem.MOD)))
            j = jcast('int', (j + 1))
        j = jcast('int', 1)
        while (j <= Code04_CountingProblem.m):
            jset(dp[u], j, jcast('int', jcast('long', jmod(jcast('long', jadd(dp[u][jcast('int', (j - 1))], Code04_CountingProblem.tmp[j])), Code04_CountingProblem.MOD))))
            j = jcast('int', (j + 1))

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code04_CountingProblem.left, 1, jcast('int', jadd(Code04_CountingProblem.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_CountingProblem.right, 1, jcast('int', jadd(Code04_CountingProblem.n, 1)), 0)

    @staticmethod
    def compute():
        Code04_CountingProblem.build()
        # 虽然n * m <= 10^6，但是n和m，单独都是2 * 10^5规模
        # 所以提前准备固定大小的表是不可能的，空间根本接受不了
        # 所以根据此时具体的n和m的大小，临时申请动态规划表，总大小不超过10^6
        dp = jarray('int', [jcast('int', jadd(Code04_CountingProblem.n, 1)), jcast('int', jadd(Code04_CountingProblem.m, 1))])
        j = jcast('int', 0)
        while (j <= Code04_CountingProblem.m):
            # 没有节点时，不管要求节点值是什么，都默认有1种形态
            # 因为没有节点时，根本不影响任何决策
            jset(dp[0], j, 1)
            j = jcast('int', (j + 1))
        Code04_CountingProblem.dfs(Code04_CountingProblem.stack[1], dp)
        Code04_CountingProblem.clear()
        return jcast('long', dp[Code04_CountingProblem.stack[1]][Code04_CountingProblem.m])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= cases):
            jcall(in_, 'nextToken')
            Code04_CountingProblem.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_CountingProblem.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code04_CountingProblem.n):
                jcall(in_, 'nextToken')
                Code04_CountingProblem.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_CountingProblem.compute())
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CountingProblem.MOD = jcast('int', 1000000007)
Code04_CountingProblem.MAXN = jcast('int', 1000001)
Code04_CountingProblem.arr = jarray('int', [Code04_CountingProblem.MAXN])
Code04_CountingProblem.left = jarray('int', [Code04_CountingProblem.MAXN])
Code04_CountingProblem.right = jarray('int', [Code04_CountingProblem.MAXN])
Code04_CountingProblem.stack = jarray('int', [Code04_CountingProblem.MAXN])
Code04_CountingProblem.tmp = jarray('long', [Code04_CountingProblem.MAXN])
Code04_CountingProblem.n = jcast('int', 0)
Code04_CountingProblem.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_CountingProblem.main([])

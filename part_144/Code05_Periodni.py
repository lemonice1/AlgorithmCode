# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 表格填数
# 给定一个长度为n的数组arr，arr[i]表示i位置上方的正方形格子数量
# 那么从1位置到n位置，每个位置就是一个直方图，所有的直方图紧靠在一起
# 在这片区域中，你要放入k个相同数字，不能有任意两个数字在同一行或者同一列
# 注意在这片区域中，如果某一行中间断开了，使得两个数字无法在这一行连通，则不算违规
# 返回填入数字的方法数，答案对 1000000007 取模
# 1 <= n、k <= 500    0 <= arr[i] <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P6453
# 因为本题给定的可用空间很少，所以数组为int类型，不用long类型
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Periodni:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'MAXH': 'MAXH', 'arr': 'arr', 'fac': 'fac', 'inv': 'inv', 'left': 'left', 'right': 'right', 'stack': 'stack', 'size': 'size', 'dp': 'dp', 'tmp': 'tmp', 'n': 'n', 'k': 'k'}
    MOD = 0
    MAXN = 0
    MAXH = 0
    # 所有数字
    arr = None
    # 阶乘余数表
    fac = None
    # 阶乘逆元表
    inv = None
    # 笛卡尔树需要
    left = None
    right = None
    stack = None
    # dfs需要
    size = None
    # dp是动态规划表
    dp = None
    # tmp是动态规划的临时结果
    tmp = None
    n = 0
    k = 0
    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code05_Periodni.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code05_Periodni.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('int', jcast('int', ans))

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('int', (0 if (n < k) else jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (jcast('long', Code05_Periodni.fac[n]) * Code05_Periodni.inv[k])), Code05_Periodni.MOD)) * Code05_Periodni.inv[jcast('int', (n - k))])), Code05_Periodni.MOD)))))

    @staticmethod
    def build():
        jset(Code05_Periodni.fac, 0, jset(Code05_Periodni.fac, 1, jset(Code05_Periodni.inv, 0, 1)))
        i = jcast('int', 2)
        while (i <= Code05_Periodni.MAXH):
            Code05_Periodni.fac[i] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', Code05_Periodni.fac[jcast('int', (i - 1))]) * i)), Code05_Periodni.MOD))))
            i = jcast('int', (i + 1))
        jset(Code05_Periodni.inv, Code05_Periodni.MAXH, Code05_Periodni.power(Code05_Periodni.fac[Code05_Periodni.MAXH], jcast('int', (Code05_Periodni.MOD - 2))))
        i = jcast('int', jcast('int', (Code05_Periodni.MAXH - 1)))
        while (i >= 1):
            Code05_Periodni.inv[i] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', Code05_Periodni.inv[jcast('int', jadd(i, 1))]) * jcast('int', jadd(i, 1)))), Code05_Periodni.MOD))))
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        top = jcast('int', 0)
        pos = 0
        while (i <= Code05_Periodni.n):
            pos = jcast('int', top)
            while ((pos > 0) and (Code05_Periodni.arr[Code05_Periodni.stack[pos]] > Code05_Periodni.arr[i])):
                pos = jcast('int', (pos - 1))
            if (pos > 0):
                jset(Code05_Periodni.right, Code05_Periodni.stack[pos], i)
            if (pos < top):
                Code05_Periodni.left[i] = jcast('int', Code05_Periodni.stack[jcast('int', jadd(pos, 1))])
            jset(Code05_Periodni.stack, (pos := jcast('int', (pos + (1)))), i)
            top = jcast('int', pos)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        if (u == 0):
            return
        Code05_Periodni.dfs(Code05_Periodni.left[u], u)
        Code05_Periodni.dfs(Code05_Periodni.right[u], u)
        Code05_Periodni.size[u] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_Periodni.size[Code05_Periodni.left[u]], Code05_Periodni.size[Code05_Periodni.right[u]])), 1)))
        jstatic('Arrays', 'fill', Code05_Periodni.tmp, 0, jcast('int', jadd(Code05_Periodni.k, 1)), 0)
        # 所有dfs过程都算上，这一部分的总复杂度O(n^2)
        l = jcast('int', 0)
        while (l <= jstatic('Math', 'min', Code05_Periodni.size[Code05_Periodni.left[u]], Code05_Periodni.k)):
            r = jcast('int', 0)
            while (r <= jstatic('Math', 'min', Code05_Periodni.size[Code05_Periodni.right[u]], jcast('int', (Code05_Periodni.k - l)))):
                Code05_Periodni.tmp[jcast('int', jadd(l, r))] = jcast('int', jcast('int', jmod(jcast('int', jcast('long', jadd(Code05_Periodni.tmp[jcast('int', jadd(l, r))], jcast('long', jmod(jcast('long', (jcast('long', Code05_Periodni.dp[Code05_Periodni.left[u]][l]) * Code05_Periodni.dp[Code05_Periodni.right[u]][r])), Code05_Periodni.MOD))))), Code05_Periodni.MOD)))
                r = jcast('int', (r + 1))
            l = jcast('int', (l + 1))
        # 所有dfs过程都算上，这一部分的总复杂度O(min(n的3次方, n * k平方))
        i = jcast('int', 0)
        while (i <= jstatic('Math', 'min', Code05_Periodni.size[u], Code05_Periodni.k)):
            p = jcast('int', 0)
            while (p <= i):
                jset(Code05_Periodni.dp[u], i, jcast('int', jmod(jcast('int', jcast('long', jadd(Code05_Periodni.dp[u][i], jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (jcast('long', Code05_Periodni.c(jcast('int', (Code05_Periodni.size[u] - p)), jcast('int', (i - p)))) * Code05_Periodni.c(jcast('int', (Code05_Periodni.arr[u] - Code05_Periodni.arr[fa])), jcast('int', (i - p))))), Code05_Periodni.MOD)) * Code05_Periodni.fac[jcast('int', (i - p))])), Code05_Periodni.MOD)) * Code05_Periodni.tmp[p])), Code05_Periodni.MOD))))), Code05_Periodni.MOD)))
                p = jcast('int', (p + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        Code05_Periodni.build()
        jset(Code05_Periodni.dp[0], 0, 1)
        Code05_Periodni.dfs(Code05_Periodni.stack[1], 0)
        return jcast('int', Code05_Periodni.dp[Code05_Periodni.stack[1]][Code05_Periodni.k])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_Periodni.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_Periodni.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_Periodni.n):
            jcall(in_, 'nextToken')
            Code05_Periodni.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_Periodni.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Periodni.MOD = jcast('int', 1000000007)
Code05_Periodni.MAXN = jcast('int', 501)
Code05_Periodni.MAXH = jcast('int', 1000000)
Code05_Periodni.arr = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.fac = jarray('int', [jcast('int', jadd(Code05_Periodni.MAXH, 1))])
Code05_Periodni.inv = jarray('int', [jcast('int', jadd(Code05_Periodni.MAXH, 1))])
Code05_Periodni.left = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.right = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.stack = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.size = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.dp = jarray('int', [Code05_Periodni.MAXN, Code05_Periodni.MAXN])
Code05_Periodni.tmp = jarray('int', [Code05_Periodni.MAXN])
Code05_Periodni.n = jcast('int', 0)
Code05_Periodni.k = jcast('int', 0)

if __name__ == '__main__':
    Code05_Periodni.main([])

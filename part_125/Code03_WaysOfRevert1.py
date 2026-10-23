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

# 还原数组的方法数(不优化枚举)
# 原本有一个长度为n的数组arr，下标从1开始，数组中都是<=200的正数
# 并且任意i位置的数字都满足 : arr[i] <= max(arr[i-1], arr[i+1])
# 特别的，arr[1] <= arr[2]，arr[n] <= arr[n-1]
# 但是输入的arr中有些数字丢失了，丢失的数字用0表示
# 返回还原成不违规的arr有多少种方法，答案对 998244353 取模
# 3 <= n <= 10^4
# 测试链接 : https://www.nowcoder.com/practice/49c5284278974cbda474ec13d8bd86a9
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 需要优化枚举以处理更大的数据规模，具体看本节课Code03_WaysOfRevert2文件的实现
class Code03_WaysOfRevert1:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'm': 'm'}
    MOD = 0
    MAXN = 0
    arr = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_WaysOfRevert1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code03_WaysOfRevert1.n):
                jcall(in_, 'nextToken')
                Code03_WaysOfRevert1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_WaysOfRevert1.compute1())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 递归 + 记忆化搜索，不优化枚举
    # 时间复杂度O(n * m平方)
    @staticmethod
    def compute1():
        dp = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert1.n, 1)), jcast('int', jadd(Code03_WaysOfRevert1.m, 1)), 2])
        i = jcast('int', 0)
        while (i <= Code03_WaysOfRevert1.n):
            j = jcast('int', 0)
            while (j <= Code03_WaysOfRevert1.m):
                jset(dp[i][j], 0, jcast('int', (-1)))
                jset(dp[i][j], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_WaysOfRevert1.f1(Code03_WaysOfRevert1.n, 0, 1, dp))

    # 1...i范围上去决定数字，i+1位置的数字已经变成了v
    # 如果s == 0, 表示i+1位置变成的数字v > i+2位置变成的数字
    # 如果s == 1, 表示i+1位置变成的数字v <= i+2位置变成的数字
    # 返回还原的方法数
    @staticmethod
    def f1(i, v, s, dp):
        i = jcast('int', i)
        v = jcast('int', v)
        s = jcast('int', s)
        if (i == 0):
            return jcast('int', s)
        if (dp[i][v][s] != jcast('int', (-1))):
            return jcast('int', dp[i][v][s])
        ans = jcast('int', 0)
        if (Code03_WaysOfRevert1.arr[i] != 0):
            if ((Code03_WaysOfRevert1.arr[i] >= v) or (s == 1)):
                ans = jcast('int', Code03_WaysOfRevert1.f1(jcast('int', (i - 1)), Code03_WaysOfRevert1.arr[i], (0 if (Code03_WaysOfRevert1.arr[i] > v) else 1), dp))
        else:
            cur = jcast('int', jcast('int', jadd(v, 1)))
            while (cur <= Code03_WaysOfRevert1.m):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert1.f1(jcast('int', (i - 1)), cur, 0, dp))), Code03_WaysOfRevert1.MOD)))
                cur = jcast('int', (cur + 1))
            if (v != 0):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert1.f1(jcast('int', (i - 1)), v, 1, dp))), Code03_WaysOfRevert1.MOD)))
            if (s == 1):
                cur = jcast('int', 1)
                while (cur < v):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert1.f1(jcast('int', (i - 1)), cur, 1, dp))), Code03_WaysOfRevert1.MOD)))
                    cur = jcast('int', (cur + 1))
        jset(dp[i][v], s, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划，不优化枚举
    # 时间复杂度O(n * m平方)
    @staticmethod
    def compute2():
        dp = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert1.n, 1)), jcast('int', jadd(Code03_WaysOfRevert1.m, 1)), 2])
        v = jcast('int', 0)
        while (v <= Code03_WaysOfRevert1.m):
            jset(dp[0][v], 0, 0)
            jset(dp[0][v], 1, 1)
            v = jcast('int', (v + 1))
        i = jcast('int', 1)
        while (i <= Code03_WaysOfRevert1.n):
            v = jcast('int', 0)
            while (v <= Code03_WaysOfRevert1.m):
                s = jcast('int', 0)
                while (s <= 1):
                    ans = jcast('int', 0)
                    if (Code03_WaysOfRevert1.arr[i] != 0):
                        if ((Code03_WaysOfRevert1.arr[i] >= v) or (s == 1)):
                            ans = jcast('int', dp[jcast('int', (i - 1))][Code03_WaysOfRevert1.arr[i]][(0 if (Code03_WaysOfRevert1.arr[i] > v) else 1)])
                    else:
                        cur = jcast('int', jcast('int', jadd(v, 1)))
                        while (cur <= Code03_WaysOfRevert1.m):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, dp[jcast('int', (i - 1))][cur][0])), Code03_WaysOfRevert1.MOD)))
                            cur = jcast('int', (cur + 1))
                        if (v != 0):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, dp[jcast('int', (i - 1))][v][1])), Code03_WaysOfRevert1.MOD)))
                        if (s == 1):
                            cur = jcast('int', 1)
                            while (cur < v):
                                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, dp[jcast('int', (i - 1))][cur][1])), Code03_WaysOfRevert1.MOD)))
                                cur = jcast('int', (cur + 1))
                    jset(dp[i][v], s, ans)
                    s = jcast('int', (s + 1))
                v = jcast('int', (v + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[Code03_WaysOfRevert1.n][0][1])

    # 空间压缩版本，不优化枚举
    # 时间复杂度O(n * m平方)
    @staticmethod
    def compute3():
        memo = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert1.m, 1)), 2])
        dp = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert1.m, 1)), 2])
        v = jcast('int', 0)
        while (v <= Code03_WaysOfRevert1.m):
            jset(memo[v], 0, 0)
            jset(memo[v], 1, 1)
            v = jcast('int', (v + 1))
        i = jcast('int', 1)
        while (i <= Code03_WaysOfRevert1.n):
            v = jcast('int', 0)
            while (v <= Code03_WaysOfRevert1.m):
                s = jcast('int', 0)
                while (s <= 1):
                    ans = jcast('int', 0)
                    if (Code03_WaysOfRevert1.arr[i] != 0):
                        if ((Code03_WaysOfRevert1.arr[i] >= v) or (s == 1)):
                            ans = jcast('int', memo[Code03_WaysOfRevert1.arr[i]][(0 if (Code03_WaysOfRevert1.arr[i] > v) else 1)])
                    else:
                        cur = jcast('int', jcast('int', jadd(v, 1)))
                        while (cur <= Code03_WaysOfRevert1.m):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, memo[cur][0])), Code03_WaysOfRevert1.MOD)))
                            cur = jcast('int', (cur + 1))
                        if (v != 0):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, memo[v][1])), Code03_WaysOfRevert1.MOD)))
                        if (s == 1):
                            cur = jcast('int', 1)
                            while (cur < v):
                                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, memo[cur][1])), Code03_WaysOfRevert1.MOD)))
                                cur = jcast('int', (cur + 1))
                    jset(dp[v], s, ans)
                    s = jcast('int', (s + 1))
                v = jcast('int', (v + 1))
            tmp = memo
            memo = dp
            dp = tmp
            i = jcast('int', (i + 1))
        return jcast('int', memo[0][1])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WaysOfRevert1.MOD = jcast('int', 998244353)
Code03_WaysOfRevert1.MAXN = jcast('int', 10001)
Code03_WaysOfRevert1.arr = jarray('int', [Code03_WaysOfRevert1.MAXN])
Code03_WaysOfRevert1.n = jcast('int', 0)
Code03_WaysOfRevert1.m = jcast('int', 200)

if __name__ == '__main__':
    Code03_WaysOfRevert1.main([])

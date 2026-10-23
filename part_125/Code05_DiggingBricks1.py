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

# 从上到下挖砖块(展示动态规划思路，不优化枚举，不进行空间压缩)
# 一堆组成倒三角形状的砖埋在地里，一共有n层，第1层有n块砖，每层递减，类似如下数据
# 4 2 9 5
# 3 1 7
# 2 4
# 8
# 需要从第1层开始挖，每挖开一块砖都可以获得数值作为收益，第1层的砖可以随意挖
# 但是挖到下面的砖是有条件的，想挖i层的j号砖，你需要确保i-1层的(j、j+1)块砖已经被挖开
# 最多可以挖m块砖，返回最大的收益
# 1 <= n <= 50
# 1 <= m <= 1300
# 砖块数值 <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P1437
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_DiggingBricks1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'grid': 'grid', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    grid = None
    dp = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_DiggingBricks1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_DiggingBricks1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        j = jcast('int', 1)
        while (j <= Code05_DiggingBricks1.n):
            i = jcast('int', Code05_DiggingBricks1.n)
            while (i >= j):
                jcall(in_, 'nextToken')
                jset(Code05_DiggingBricks1.grid[i], j, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i - 1))
            j = jcast('int', (j + 1))
        jcall(out, 'println', Code05_DiggingBricks1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 只展示核心思路，不优化枚举，不做空间压缩
    # 时间复杂度O(n^3 * m)
    @staticmethod
    def compute():
        ans = jcast('int', 0)
        i = jcast('int', 1)
        cur = 0
        max = 0
        while (i <= Code05_DiggingBricks1.n):
            # cur是当前行的收益
            cur = jcast('int', 0)
            j = jcast('int', 0)
            while (j <= i):
                cur = jcast('int', jcast('int', jadd(cur, Code05_DiggingBricks1.grid[i][j])))
                # 想挖到j号砖，总共挖的数量一定不少于
                # (j + 1) * j / 2，也就是等差数列
                # 如果k小于这个值无意义，认为收益是0
                k = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(j, 1)) * j)), 2)))
                while (k <= Code05_DiggingBricks1.m):
                    max = jcast('int', 0)
                    p = jcast('int', jstatic('Math', 'max', 0, jcast('int', (j - 1))))
                    while (p <= jcast('int', (i - 1))):
                        max = jcast('int', jstatic('Math', 'max', max, Code05_DiggingBricks1.dp[jcast('int', (i - 1))][p][jcast('int', (k - j))]))
                        p = jcast('int', (p + 1))
                    jset(Code05_DiggingBricks1.dp[i][j], k, jcast('int', jadd(max, cur)))
                    ans = jcast('int', jstatic('Math', 'max', ans, Code05_DiggingBricks1.dp[i][j][k]))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_DiggingBricks1.MAXN = jcast('int', 51)
Code05_DiggingBricks1.MAXM = jcast('int', 1301)
Code05_DiggingBricks1.grid = jarray('int', [Code05_DiggingBricks1.MAXN, Code05_DiggingBricks1.MAXN])
Code05_DiggingBricks1.dp = jarray('int', [Code05_DiggingBricks1.MAXN, Code05_DiggingBricks1.MAXN, Code05_DiggingBricks1.MAXM])
Code05_DiggingBricks1.n = jcast('int', 0)
Code05_DiggingBricks1.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_DiggingBricks1.main([])

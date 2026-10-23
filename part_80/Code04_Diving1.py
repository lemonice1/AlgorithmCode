# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 潜水的最大时间与方案
# 一共有n个工具，每个工具都有自己的重量a、阻力b、提升的停留时间c
# 因为背包有限，所以只能背重量不超过m的工具
# 因为力气有限，所以只能背阻力不超过v的工具
# 希望能在水下停留的时间最久
# 返回最久的停留时间和下标字典序最小的选择工具的方案
# 注意这道题的字典序设定（根据提交的结果推论的）：
# 下标方案整体构成的字符串保证字典序最小
# 比如下标方案"1 120"比下标方案"1 2"字典序小
# 测试链接 : https://www.luogu.com.cn/problem/P1759
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 讲解069 - 多维费用背包
# 不做空间压缩的版本
# 此版本用于展示算法思路，需进一步分析资源开销
# 这个题必须做空间压缩
# 空间压缩的实现在Code04_Diving2
class Code04_Diving1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'a': 'a', 'b': 'b', 'c': 'c', 'dp': 'dp', 'path': 'path', 'm': 'm', 'v': 'v', 'n': 'n'}
    MAXN = 0
    MAXM = 0
    a = None
    b = None
    c = None
    dp = None
    path = None
    m = 0
    v = 0
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code04_Diving1.n):
            j = jcast('int', 0)
            while (j <= Code04_Diving1.m):
                k = jcast('int', 0)
                while (k <= Code04_Diving1.v):
                    jset(Code04_Diving1.dp[i][j], k, 0)
                    jset(Code04_Diving1.path[i][j], k, None)
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_Diving1.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_Diving1.v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_Diving1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_Diving1.build()
            i = jcast('int', 1)
            while (i <= Code04_Diving1.n):
                jcall(in_, 'nextToken')
                Code04_Diving1.a[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code04_Diving1.b[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code04_Diving1.c[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            Code04_Diving1.compute()
            jcall(out, 'println', Code04_Diving1.dp[Code04_Diving1.n][Code04_Diving1.m][Code04_Diving1.v])
            jcall(out, 'println', Code04_Diving1.path[Code04_Diving1.n][Code04_Diving1.m][Code04_Diving1.v])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 普通版本的多维费用背包
    # 为了好懂先实现不进行空间压缩的版本
    @staticmethod
    def compute():
        p2 = None
        i = jcast('int', 1)
        while (i <= Code04_Diving1.n):
            j = jcast('int', 0)
            while (j <= Code04_Diving1.m):
                k = jcast('int', 0)
                while (k <= Code04_Diving1.v):
                    # 可能性1 : 不要i位置的货
                    # 先把可能性1的答案设置上
                    # 包括dp信息和path信息
                    jset(Code04_Diving1.dp[i][j], k, Code04_Diving1.dp[jcast('int', (i - 1))][j][k])
                    jset(Code04_Diving1.path[i][j], k, Code04_Diving1.path[jcast('int', (i - 1))][j][k])
                    if ((j >= Code04_Diving1.a[i]) and (k >= Code04_Diving1.b[i])):
                        # 可能性2 : 要i位置的货
                        # 那么需要:
                        # 背包总重量限制j >= a[i]
                        # 背包总阻力限制k >= b[i]
                        # 然后选了i位置的货，就可以获得收益c[i]了
                        # 可能性2收益 : dp[i-1][j-a[i]][k-b[i]] + c[i]
                        # 可能性2路径(p2) : path[i-1][j-a[i]][k-b[i]] + " " + i
                        if (Code04_Diving1.path[jcast('int', (i - 1))][jcast('int', (j - Code04_Diving1.a[i]))][jcast('int', (k - Code04_Diving1.b[i]))] == None):
                            p2 = jstatic('String', 'valueOf', i)
                        else:
                            p2 = jadd(jadd(Code04_Diving1.path[jcast('int', (i - 1))][jcast('int', (j - Code04_Diving1.a[i]))][jcast('int', (k - Code04_Diving1.b[i]))], ' '), jstatic('String', 'valueOf', i))
                        if (Code04_Diving1.dp[i][j][k] < jcast('int', jadd(Code04_Diving1.dp[jcast('int', (i - 1))][jcast('int', (j - Code04_Diving1.a[i]))][jcast('int', (k - Code04_Diving1.b[i]))], Code04_Diving1.c[i]))):
                            jset(Code04_Diving1.dp[i][j], k, jcast('int', jadd(Code04_Diving1.dp[jcast('int', (i - 1))][jcast('int', (j - Code04_Diving1.a[i]))][jcast('int', (k - Code04_Diving1.b[i]))], Code04_Diving1.c[i])))
                            jset(Code04_Diving1.path[i][j], k, p2)
                        else:
                            if (Code04_Diving1.dp[i][j][k] == jcast('int', jadd(Code04_Diving1.dp[jcast('int', (i - 1))][jcast('int', (j - Code04_Diving1.a[i]))][jcast('int', (k - Code04_Diving1.b[i]))], Code04_Diving1.c[i]))):
                                if (jcall(p2, 'compareTo', Code04_Diving1.path[i][j][k]) < 0):
                                    # 如果可能性2的路径，字典序小于，可能性1的路径
                                    # 那么把路径设置成可能性2的路径
                                    jset(Code04_Diving1.path[i][j], k, p2)
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Diving1.MAXN = jcast('int', 101)
Code04_Diving1.MAXM = jcast('int', 201)
Code04_Diving1.a = jarray('int', [Code04_Diving1.MAXN])
Code04_Diving1.b = jarray('int', [Code04_Diving1.MAXN])
Code04_Diving1.c = jarray('int', [Code04_Diving1.MAXN])
Code04_Diving1.dp = jarray('int', [Code04_Diving1.MAXN, Code04_Diving1.MAXM, Code04_Diving1.MAXM])
Code04_Diving1.path = jarray('String', [Code04_Diving1.MAXN, Code04_Diving1.MAXM, Code04_Diving1.MAXM])
Code04_Diving1.m = jcast('int', 0)
Code04_Diving1.v = jcast('int', 0)
Code04_Diving1.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_Diving1.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 砍树
# 一共有n棵树，每棵树都有两个信息：
# 第一天这棵树的初始重量、这棵树每天的增长重量
# 你每天最多能砍1棵树，砍下这棵树的收益为：
# 这棵树的初始重量 + 这棵树增长到这一天的总增重
# 从第1天开始，你一共有m天可以砍树，返回m天内你获得的最大收益
# 测试链接 : https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827367873
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 不过现在这个题收费了，验证很困难了，于是我找到了一个平替的题目
# 本节课Code06_CookingPlan文件就是平替题目，贪心的思路是非常类似的
class Code05_CuttingTree:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'dp': 'dp', 't': 't', 'n': 'n', 'm': 'm'}
    # 树的个数、天数最大值，不超过的量
    MAXN = 0
    # 树的编号为1 ~ n
    # tree[i][0] : 第i棵树第一天的初始重量
    # tree[i][1] : 第i棵树每天的增长重量
    tree = None
    # dp[i][j] : 在j天内，从前i棵树中选若干棵树进行砍伐，最大收益是多少
    dp = None
    t = 0
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_CuttingTree.t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_CuttingTree.t):
            jcall(in_, 'nextToken')
            Code05_CuttingTree.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_CuttingTree.m = jcast('int', jcast('int', jget(in_, 'nval')))
            j = jcast('int', 1)
            while (j <= Code05_CuttingTree.n):
                jcall(in_, 'nextToken')
                jset(Code05_CuttingTree.tree[j], 0, jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code05_CuttingTree.n):
                jcall(in_, 'nextToken')
                jset(Code05_CuttingTree.tree[j], 1, jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            jcall(out, 'println', Code05_CuttingTree.compute())
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 讲解073 - 01背包
    @staticmethod
    def compute():
        # 树的初始重量不决定树的顺序，因为任何树砍了，就获得固定的初始量，和砍伐的顺序无关
        # 根据增长速度排序，增长量小的在前，增长量大的在后
        # 认为越靠后的树，越要尽量晚的砍伐，课上的重点内容
        jstatic('Arrays', 'sort', Code05_CuttingTree.tree, 1, jcast('int', jadd(Code05_CuttingTree.n, 1)), (lambda o1, o2: (o1[1] - o2[1])))
        # dp[0][...] = 0 : 表示如果没有树，不管过去多少天，收益都是0
        # dp[...][0] = 0 : 表示不管有几棵树，没有时间砍树，收益都是0
        i = jcast('int', 1)
        while (i <= Code05_CuttingTree.n):
            j = jcast('int', 1)
            while (j <= Code05_CuttingTree.m):
                jset(Code05_CuttingTree.dp[i], j, jstatic('Math', 'max', Code05_CuttingTree.dp[jcast('int', (i - 1))][j], jcast('int', jadd(jcast('int', jadd(Code05_CuttingTree.dp[jcast('int', (i - 1))][jcast('int', (j - 1))], Code05_CuttingTree.tree[i][0])), jcast('int', (Code05_CuttingTree.tree[i][1] * jcast('int', (j - 1))))))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code05_CuttingTree.dp[Code05_CuttingTree.n][Code05_CuttingTree.m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_CuttingTree.MAXN = jcast('int', 251)
Code05_CuttingTree.tree = jarray('int', [Code05_CuttingTree.MAXN, 2])
Code05_CuttingTree.dp = jarray('int', [Code05_CuttingTree.MAXN, Code05_CuttingTree.MAXN])
Code05_CuttingTree.t = jcast('int', 0)
Code05_CuttingTree.n = jcast('int', 0)
Code05_CuttingTree.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_CuttingTree.main([])

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

# 最佳团体
# 给定一棵树，节点编号0~n，0号节点是整棵树的头
# 编号1~n的节点，每个节点都有招募花费和战斗值，0号节点这两个值都是0
# 给定每条边(a,b)，表示节点a的父节点是b，有些节点的父节点是0节点
# 当招募了某个节点，那么该节点及其上方的所有祖先节点都需要招募
# 除了0号节点之外，一共可以招募k个人，希望让
# 战斗值之和 / 招募花费之和，这个比值尽量大，答案只需保留三位小数，更大的精度舍弃
# 1 <= k <= n <= 2500
# 0 <= 招募花费、战斗值 <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P4322
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_BestTeam:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'NA': 'NA', 'sml': 'sml', 'head': 'head', 'next': 'next', 'to': 'to', 'edgeCnt': 'edgeCnt', 'cost': 'cost', 'strength': 'strength', 'dfn': 'dfn', 'dfnCnt': 'dfnCnt', 'value': 'value', 'size': 'size', 'dp': 'dp', 'k': 'k', 'n': 'n'}
    MAXN = 0
    LIMIT = 0
    NA = 0.0
    sml = 0.0
    # 链式前向星
    head = None
    next = None
    to = None
    edgeCnt = 0
    # 招募花费，下标为节点原始编号
    cost = None
    # 战斗值，下标为节点原始编号
    strength = None
    # dfn[a] = b，表示原始a号节点的dfn编号为b
    dfn = None
    # dfn序计数
    dfnCnt = 0
    # (战斗值 - x * 招募花费)的结余，下标为节点dfn编号
    value = None
    # 子树大小，下标为节点dfn编号
    size = None
    # 树型dp
    dp = None
    k = 0
    n = 0
    @staticmethod
    def prepare():
        Code05_BestTeam.edgeCnt = jcast('int', 1)
        Code05_BestTeam.dfnCnt = jcast('int', 0)
        jstatic('Arrays', 'fill', Code05_BestTeam.head, 1, jcast('int', jadd(Code05_BestTeam.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_BestTeam.next[Code05_BestTeam.edgeCnt] = jcast('int', Code05_BestTeam.head[u])
        Code05_BestTeam.to[Code05_BestTeam.edgeCnt] = jcast('int', v)
        jset(Code05_BestTeam.head, u, ((_java_obj_1 := Code05_BestTeam), (_java_key_2 := 'edgeCnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 记录节点u的dfn编号 + 返回u这棵子树的节点数
    # 如下实现和讲解079，题目5，选课问题的最优解，几乎完全一样
    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        i = jcast('int', ((_java_obj_4 := Code05_BestTeam), (_java_key_5 := 'dfnCnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code05_BestTeam.dfn[u] = jcast('int', i)
        Code05_BestTeam.size[i] = jcast('int', 1)
        e = jcast('int', Code05_BestTeam.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_BestTeam.to[e])
            ((_java_obj_7 := Code05_BestTeam.size), (_java_key_8 := i), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), Code05_BestTeam.dfs(v)))))[2]
            e = jcast('int', Code05_BestTeam.next[e])
        return jcast('int', Code05_BestTeam.size[i])

    # 根据x的值，计算节点的结余值，在树上选k+1个点
    # 一定要形成有效结构，返回最大的结余和
    # 核心逻辑完全来自讲解079，题目5，选课问题，重点介绍的最优解
    @staticmethod
    def check(x):
        x = jcast('double', x)
        # value[节点i的dfn编号] = 节点i的战斗值 - x * 节点i的招募花费
        i = jcast('int', 0)
        while (i <= Code05_BestTeam.n):
            jset(Code05_BestTeam.value, Code05_BestTeam.dfn[i], (jcast('double', Code05_BestTeam.strength[i]) - (x * Code05_BestTeam.cost[i])))
            i = jcast('int', (i + 1))
        # 越界位置认为都是无效解
        j = jcast('int', 1)
        while (j <= Code05_BestTeam.k):
            jset(Code05_BestTeam.dp[jcast('int', jadd(Code05_BestTeam.dfnCnt, 1))], j, Code05_BestTeam.NA)
            j = jcast('int', (j + 1))
        # 讲解079题目5的最优解逻辑
        i = jcast('int', Code05_BestTeam.dfnCnt)
        while (i >= 2):
            j = jcast('int', 1)
            while (j <= Code05_BestTeam.k):
                jset(Code05_BestTeam.dp[i], j, jstatic('Math', 'max', Code05_BestTeam.dp[jcast('int', jadd(i, Code05_BestTeam.size[i]))][j], jadd(Code05_BestTeam.value[i], Code05_BestTeam.dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        # 原始的0号节点，dfn编号是1，其他节点的dfn编号从2开始
        # 0号节点的战斗值和招募花费都是0，其他节点一共招募k个
        return jcast('boolean', (Code05_BestTeam.dp[2][Code05_BestTeam.k] >= 0))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_BestTeam.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_BestTeam.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_BestTeam.prepare()
        i = jcast('int', 1)
        while (i <= Code05_BestTeam.n):
            jcall(in_, 'nextToken')
            Code05_BestTeam.cost[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_BestTeam.strength[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_BestTeam.addEdge(jcast('int', jget(in_, 'nval')), i)
            i = jcast('int', (i + 1))
        Code05_BestTeam.dfs(0)
        l = jcast('double', 0)
        r = jcast('double', Code05_BestTeam.LIMIT)
        x = 0.0
        ans = jcast('double', 0)
        while ((l < r) and ((r - l) >= Code05_BestTeam.sml)):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Code05_BestTeam.check(x):
                ans = jcast('double', x)
                l = jcast('double', jadd(x, Code05_BestTeam.sml))
            else:
                r = jcast('double', (x - Code05_BestTeam.sml))
        jcall(out, 'printf', '%.3f\n', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_BestTeam.MAXN = jcast('int', 3001)
Code05_BestTeam.LIMIT = jcast('int', 10000)
Code05_BestTeam.NA = jcast('double', (-1000000000.0))
Code05_BestTeam.sml = jcast('double', 1e-06)
Code05_BestTeam.head = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.next = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.to = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.edgeCnt = jcast('int', 0)
Code05_BestTeam.cost = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.strength = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.dfn = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.dfnCnt = jcast('int', 0)
Code05_BestTeam.value = jarray('double', [Code05_BestTeam.MAXN])
Code05_BestTeam.size = jarray('int', [Code05_BestTeam.MAXN])
Code05_BestTeam.dp = jarray('double', [Code05_BestTeam.MAXN, Code05_BestTeam.MAXN])
Code05_BestTeam.k = jcast('int', 0)
Code05_BestTeam.n = jcast('int', 0)

if __name__ == '__main__':
    Code05_BestTeam.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 派遣，Python版
# 一共有n个忍者，每个忍者有上级编号、工资、能力，三个属性
# 输入保证，任何忍者的上级编号 < 这名忍者的编号，1号忍者是整棵忍者树的头
# 你一共有m的预算，可以在忍者树上随意选一棵子树，然后在这棵子树上挑选忍者
# 你选择某棵子树之后，不一定要选子树头的忍者，只要不超过m的预算，可以随意选择子树上的忍者
# 最终收益 = 雇佣人数 * 子树头忍者的能力，返回能取得的最大收益是多少
# 1 <= n <= 10^5           1 <= m <= 10^9
# 1 <= 每个忍者工资 <= m     1 <= 每个忍者领导力 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1552
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Dispatch1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'leader': 'leader', 'cost': 'cost', 'ability': 'ability', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father', 'size': 'size', 'sum': 'sum'}
    MAXN = 0
    n = 0
    m = 0
    # 上级
    leader = None
    # 薪水
    cost = None
    # 能力
    ability = None
    # 左孩子
    left = None
    # 右孩子
    right = None
    # 距离
    dist = None
    # 寻找堆顶需要
    father = None
    # 堆的大小
    size = None
    # 堆的费用和
    sum = None
    @staticmethod
    def prepare():
        Code04_Dispatch1.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code04_Dispatch1.n):
            jset(Code04_Dispatch1.left, i, jset(Code04_Dispatch1.right, i, jset(Code04_Dispatch1.dist, i, 0)))
            Code04_Dispatch1.size[i] = jcast('int', 1)
            Code04_Dispatch1.sum[i] = jcast('long', Code04_Dispatch1.cost[i])
            Code04_Dispatch1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code04_Dispatch1.father, i, (i if (Code04_Dispatch1.father[i] == i) else Code04_Dispatch1.find(Code04_Dispatch1.father[i])))
        return jcast('int', Code04_Dispatch1.father[i])

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 维护大根堆
        if (Code04_Dispatch1.cost[i] < Code04_Dispatch1.cost[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code04_Dispatch1.right, i, Code04_Dispatch1.merge(Code04_Dispatch1.right[i], j))
        if (Code04_Dispatch1.dist[Code04_Dispatch1.left[i]] < Code04_Dispatch1.dist[Code04_Dispatch1.right[i]]):
            tmp = jcast('int', Code04_Dispatch1.left[i])
            Code04_Dispatch1.left[i] = jcast('int', Code04_Dispatch1.right[i])
            Code04_Dispatch1.right[i] = jcast('int', tmp)
        Code04_Dispatch1.dist[i] = jcast('int', jcast('int', jadd(Code04_Dispatch1.dist[Code04_Dispatch1.right[i]], 1)))
        jset(Code04_Dispatch1.father, Code04_Dispatch1.left[i], jset(Code04_Dispatch1.father, Code04_Dispatch1.right[i], i))
        return jcast('int', i)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        jset(Code04_Dispatch1.father, Code04_Dispatch1.left[i], Code04_Dispatch1.left[i])
        jset(Code04_Dispatch1.father, Code04_Dispatch1.right[i], Code04_Dispatch1.right[i])
        jset(Code04_Dispatch1.father, i, Code04_Dispatch1.merge(Code04_Dispatch1.left[i], Code04_Dispatch1.right[i]))
        jset(Code04_Dispatch1.left, i, jset(Code04_Dispatch1.right, i, jset(Code04_Dispatch1.dist, i, 0)))
        return jcast('int', Code04_Dispatch1.father[i])

    @staticmethod
    def compute():
        ans = jcast('long', 0)
        p = 0
        psize = 0
        h = 0
        hsize = 0
        hsum = 0
        psum = 0
        i = jcast('int', Code04_Dispatch1.n)
        while (i >= 1):
            h = jcast('int', Code04_Dispatch1.find(i))
            hsize = jcast('int', Code04_Dispatch1.size[h])
            hsum = jcast('long', Code04_Dispatch1.sum[h])
            while (hsum > Code04_Dispatch1.m):
                Code04_Dispatch1.pop(h)
                hsize = jcast('int', (hsize - 1))
                hsum = jcast('long', jcast('long', (hsum - Code04_Dispatch1.cost[h])))
                h = jcast('int', Code04_Dispatch1.find(i))
            ans = jcast('long', jstatic('Math', 'max', ans, jcast('long', (jcast('long', hsize) * Code04_Dispatch1.ability[i]))))
            if (i > 1):
                p = jcast('int', Code04_Dispatch1.find(Code04_Dispatch1.leader[i]))
                psize = jcast('int', Code04_Dispatch1.size[p])
                psum = jcast('long', Code04_Dispatch1.sum[p])
                jset(Code04_Dispatch1.father, p, jset(Code04_Dispatch1.father, h, Code04_Dispatch1.merge(p, h)))
                jset(Code04_Dispatch1.size, Code04_Dispatch1.father[p], jcast('int', jadd(psize, hsize)))
                jset(Code04_Dispatch1.sum, Code04_Dispatch1.father[p], jcast('long', jadd(psum, hsum)))
            i = jcast('int', (i - 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Dispatch1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Dispatch1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_Dispatch1.n):
            jcall(in_, 'nextToken')
            Code04_Dispatch1.leader[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_Dispatch1.cost[i] = jcast('long', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_Dispatch1.ability[i] = jcast('long', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_Dispatch1.prepare()
        jcall(out, 'println', Code04_Dispatch1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Dispatch1.MAXN = jcast('int', 100001)
Code04_Dispatch1.n = jcast('int', 0)
Code04_Dispatch1.m = jcast('int', 0)
Code04_Dispatch1.leader = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.cost = jarray('long', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.ability = jarray('long', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.left = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.right = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.dist = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.father = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.size = jarray('int', [Code04_Dispatch1.MAXN])
Code04_Dispatch1.sum = jarray('long', [Code04_Dispatch1.MAXN])

if __name__ == '__main__':
    Code04_Dispatch1.main([])

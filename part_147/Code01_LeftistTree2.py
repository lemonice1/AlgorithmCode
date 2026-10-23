# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 左偏树模版题1，Python版
# 依次给定n个非负数字，表示有n个小根堆，每个堆只有一个数
# 实现如下两种操作，操作一共调用m次
# 1 x y : 第x个数字所在的堆和第y个数字所在的堆合并
# 如果两个数字已经在一个堆或者某个数字已经删除，不进行合并
# 2 x   : 打印第x个数字所在堆的最小值，并且在堆里删掉这个最小值
# 如果第x个数字已经被删除，也就是找不到所在的堆，打印-1
# 若有多个最小值，优先删除编号小的
# 1 <= n, m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3377
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LeftistTree2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'num': 'num', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father'}
    MAXN = 0
    n = 0
    m = 0
    # 左偏树需要
    num = None
    left = None
    right = None
    dist = None
    # 并查集需要father数组，方便快速找到树的头
    # father[i]不代表i在树上的父亲节点
    # father是并查集找代表节点的路径信息
    # 需要保证，并查集最上方的代表节点 = 树的头节点
    father = None
    @staticmethod
    def prepare():
        Code01_LeftistTree2.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code01_LeftistTree2.n):
            jset(Code01_LeftistTree2.left, i, jset(Code01_LeftistTree2.right, i, jset(Code01_LeftistTree2.dist, i, 0)))
            Code01_LeftistTree2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code01_LeftistTree2.father, i, (i if (Code01_LeftistTree2.father[i] == i) else Code01_LeftistTree2.find(Code01_LeftistTree2.father[i])))
        return jcast('int', Code01_LeftistTree2.father[i])

    # 编号为i的左偏树 与 编号为j的左偏树合并，返回新树的头节点编号
    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 维护小根堆，如果值一样，编号小的节点做头
        if ((Code01_LeftistTree2.num[i] > Code01_LeftistTree2.num[j]) or ((Code01_LeftistTree2.num[i] == Code01_LeftistTree2.num[j]) and (i > j))):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code01_LeftistTree2.right, i, Code01_LeftistTree2.merge(Code01_LeftistTree2.right[i], j))
        if (Code01_LeftistTree2.dist[Code01_LeftistTree2.left[i]] < Code01_LeftistTree2.dist[Code01_LeftistTree2.right[i]]):
            tmp = jcast('int', Code01_LeftistTree2.left[i])
            Code01_LeftistTree2.left[i] = jcast('int', Code01_LeftistTree2.right[i])
            Code01_LeftistTree2.right[i] = jcast('int', tmp)
        Code01_LeftistTree2.dist[i] = jcast('int', jcast('int', jadd(Code01_LeftistTree2.dist[Code01_LeftistTree2.right[i]], 1)))
        jset(Code01_LeftistTree2.father, Code01_LeftistTree2.left[i], jset(Code01_LeftistTree2.father, Code01_LeftistTree2.right[i], i))
        return jcast('int', i)

    # 节点i一定是左偏树的头，在左偏树上删掉节点i，返回新树的头节点编号
    @staticmethod
    def pop(i):
        i = jcast('int', i)
        jset(Code01_LeftistTree2.father, Code01_LeftistTree2.left[i], Code01_LeftistTree2.left[i])
        jset(Code01_LeftistTree2.father, Code01_LeftistTree2.right[i], Code01_LeftistTree2.right[i])
        # 并查集有路径压缩，所以i下方的某个节点x，可能有father[x] = i
        # 现在要删掉i了，所以x往上会找不到正确的头节点
        # 为了任何节点往上都能找到正确的头，所以要有下面这句
        jset(Code01_LeftistTree2.father, i, Code01_LeftistTree2.merge(Code01_LeftistTree2.left[i], Code01_LeftistTree2.right[i]))
        jset(Code01_LeftistTree2.left, i, jset(Code01_LeftistTree2.right, i, jset(Code01_LeftistTree2.dist, i, 0)))
        return jcast('int', Code01_LeftistTree2.father[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_LeftistTree2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_LeftistTree2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_LeftistTree2.prepare()
        i = jcast('int', 1)
        while (i <= Code01_LeftistTree2.n):
            jcall(in_, 'nextToken')
            Code01_LeftistTree2.num[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code01_LeftistTree2.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                if ((Code01_LeftistTree2.num[x] != jcast('int', (-1))) and (Code01_LeftistTree2.num[y] != jcast('int', (-1)))):
                    l = jcast('int', Code01_LeftistTree2.find(x))
                    r = jcast('int', Code01_LeftistTree2.find(y))
                    if (l != r):
                        Code01_LeftistTree2.merge(l, r)
            else:
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                if (Code01_LeftistTree2.num[x] == jcast('int', (-1))):
                    jcall(out, 'println', jcast('int', (-1)))
                else:
                    ans = jcast('int', Code01_LeftistTree2.find(x))
                    jcall(out, 'println', Code01_LeftistTree2.num[ans])
                    Code01_LeftistTree2.pop(ans)
                    Code01_LeftistTree2.num[ans] = jcast('int', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LeftistTree2.MAXN = jcast('int', 100001)
Code01_LeftistTree2.n = jcast('int', 0)
Code01_LeftistTree2.m = jcast('int', 0)
Code01_LeftistTree2.num = jarray('int', [Code01_LeftistTree2.MAXN])
Code01_LeftistTree2.left = jarray('int', [Code01_LeftistTree2.MAXN])
Code01_LeftistTree2.right = jarray('int', [Code01_LeftistTree2.MAXN])
Code01_LeftistTree2.dist = jarray('int', [Code01_LeftistTree2.MAXN])
Code01_LeftistTree2.father = jarray('int', [Code01_LeftistTree2.MAXN])

if __name__ == '__main__':
    Code01_LeftistTree2.main([])

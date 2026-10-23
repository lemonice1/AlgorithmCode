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

# 牛群聚集(迭代版)
# 一共有n个节点，编号1~n，每个点有牛的数量
# 一共有n-1条边把所有点连通起来形成一棵树，每条边有权值
# 想把所有的牛汇聚在一点，希望走过的总距离最小
# 返回总距离最小是多少
# 利用重心的性质：
# 树上的边权如果都>=0，不管边权怎么分布，所有节点都走向重心的总距离和最小
# 测试链接 : https://www.luogu.com.cn/problem/P2986
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_GreatCowGathering2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'cow': 'cow', 'cowSum': 'cowSum', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'best': 'best', 'center': 'center', 'size': 'size', 'path': 'path', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    n = 0
    cow = None
    cowSum = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    best = 0
    center = 0
    size = None
    path = None
    @staticmethod
    def build():
        Code03_GreatCowGathering2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_GreatCowGathering2.head, 1, jcast('int', jadd(Code03_GreatCowGathering2.n, 1)), 0)
        Code03_GreatCowGathering2.cowSum = jcast('int', 0)
        Code03_GreatCowGathering2.best = jcast('int', jget(Integer, 'MAX_VALUE'))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code03_GreatCowGathering2.next[Code03_GreatCowGathering2.cnt] = jcast('int', Code03_GreatCowGathering2.head[u])
        Code03_GreatCowGathering2.to[Code03_GreatCowGathering2.cnt] = jcast('int', v)
        Code03_GreatCowGathering2.weight[Code03_GreatCowGathering2.cnt] = jcast('int', w)
        jset(Code03_GreatCowGathering2.head, u, ((_java_obj_1 := Code03_GreatCowGathering2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # ufe是为了实现迭代版而准备的栈
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize], 0, u)
        jset(Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize], 1, f)
        jset(Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize], 2, e)
        Code03_GreatCowGathering2.stackSize = jcast('int', (Code03_GreatCowGathering2.stackSize + 1))

    @staticmethod
    def pop():
        Code03_GreatCowGathering2.stackSize = jcast('int', (Code03_GreatCowGathering2.stackSize - 1))
        Code03_GreatCowGathering2.u = jcast('int', Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize][0])
        Code03_GreatCowGathering2.f = jcast('int', Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize][1])
        Code03_GreatCowGathering2.e = jcast('int', Code03_GreatCowGathering2.ufe[Code03_GreatCowGathering2.stackSize][2])

    # 迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def findCenter(root):
        root = jcast('int', root)
        Code03_GreatCowGathering2.stackSize = jcast('int', 0)
        Code03_GreatCowGathering2.push(root, 0, jcast('int', (-1)))
        while (Code03_GreatCowGathering2.stackSize > 0):
            Code03_GreatCowGathering2.pop()
            # 如果第一次来到当前节点u
            if (Code03_GreatCowGathering2.e == jcast('int', (-1))):
                Code03_GreatCowGathering2.size[Code03_GreatCowGathering2.u] = jcast('int', Code03_GreatCowGathering2.cow[Code03_GreatCowGathering2.u])
                Code03_GreatCowGathering2.e = jcast('int', Code03_GreatCowGathering2.head[Code03_GreatCowGathering2.u])
                # 如果不是第一次来到当前节点u
            else:
                Code03_GreatCowGathering2.e = jcast('int', Code03_GreatCowGathering2.next[Code03_GreatCowGathering2.e])
            # 如果还有后续边、还有后续子节点
            if (Code03_GreatCowGathering2.e != 0):
                Code03_GreatCowGathering2.push(Code03_GreatCowGathering2.u, Code03_GreatCowGathering2.f, Code03_GreatCowGathering2.e)
                if (Code03_GreatCowGathering2.to[Code03_GreatCowGathering2.e] != Code03_GreatCowGathering2.f):
                    Code03_GreatCowGathering2.push(Code03_GreatCowGathering2.to[Code03_GreatCowGathering2.e], Code03_GreatCowGathering2.u, jcast('int', (-1)))
                # 如果没有后续边了，那么就做最后的统计工作
            else:
                maxsub = jcast('int', 0)
                i = jcast('int', Code03_GreatCowGathering2.head[Code03_GreatCowGathering2.u])
                v = 0
                while (i != 0):
                    v = jcast('int', Code03_GreatCowGathering2.to[i])
                    if (v != Code03_GreatCowGathering2.f):
                        Code03_GreatCowGathering2.size[Code03_GreatCowGathering2.u] = jcast('int', jcast('int', jadd(Code03_GreatCowGathering2.size[Code03_GreatCowGathering2.u], Code03_GreatCowGathering2.size[v])))
                        maxsub = jcast('int', jstatic('Math', 'max', maxsub, Code03_GreatCowGathering2.size[v]))
                    i = jcast('int', Code03_GreatCowGathering2.next[i])
                maxsub = jcast('int', jstatic('Math', 'max', maxsub, jcast('int', (Code03_GreatCowGathering2.cowSum - Code03_GreatCowGathering2.size[Code03_GreatCowGathering2.u]))))
                if (maxsub < Code03_GreatCowGathering2.best):
                    Code03_GreatCowGathering2.best = jcast('int', maxsub)
                    Code03_GreatCowGathering2.center = jcast('int', Code03_GreatCowGathering2.u)

    # 迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def setPath(root):
        root = jcast('int', root)
        Code03_GreatCowGathering2.stackSize = jcast('int', 0)
        Code03_GreatCowGathering2.push(root, 0, jcast('int', (-1)))
        while (Code03_GreatCowGathering2.stackSize > 0):
            Code03_GreatCowGathering2.pop()
            if (Code03_GreatCowGathering2.e == jcast('int', (-1))):
                Code03_GreatCowGathering2.e = jcast('int', Code03_GreatCowGathering2.head[Code03_GreatCowGathering2.u])
            else:
                Code03_GreatCowGathering2.e = jcast('int', Code03_GreatCowGathering2.next[Code03_GreatCowGathering2.e])
            if (Code03_GreatCowGathering2.e != 0):
                Code03_GreatCowGathering2.push(Code03_GreatCowGathering2.u, Code03_GreatCowGathering2.f, Code03_GreatCowGathering2.e)
                v = jcast('int', Code03_GreatCowGathering2.to[Code03_GreatCowGathering2.e])
                if (v != Code03_GreatCowGathering2.f):
                    Code03_GreatCowGathering2.path[v] = jcast('int', jcast('int', jadd(Code03_GreatCowGathering2.path[Code03_GreatCowGathering2.u], Code03_GreatCowGathering2.weight[Code03_GreatCowGathering2.e])))
                    Code03_GreatCowGathering2.push(v, Code03_GreatCowGathering2.u, jcast('int', (-1)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_GreatCowGathering2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_GreatCowGathering2.build()
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering2.n):
            jcall(in_, 'nextToken')
            Code03_GreatCowGathering2.cow[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_GreatCowGathering2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_GreatCowGathering2.addEdge(u, v, w)
            Code03_GreatCowGathering2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_GreatCowGathering2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering2.n):
            Code03_GreatCowGathering2.cowSum = jcast('int', jcast('int', jadd(Code03_GreatCowGathering2.cowSum, Code03_GreatCowGathering2.cow[i])))
            i = jcast('int', (i + 1))
        Code03_GreatCowGathering2.findCenter(1)
        Code03_GreatCowGathering2.path[Code03_GreatCowGathering2.center] = jcast('int', 0)
        Code03_GreatCowGathering2.setPath(Code03_GreatCowGathering2.center)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code03_GreatCowGathering2.n):
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', Code03_GreatCowGathering2.cow[i]) * Code03_GreatCowGathering2.path[i])))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_GreatCowGathering2.MAXN = jcast('int', 100001)
Code03_GreatCowGathering2.n = jcast('int', 0)
Code03_GreatCowGathering2.cow = jarray('int', [Code03_GreatCowGathering2.MAXN])
Code03_GreatCowGathering2.cowSum = jcast('int', 0)
Code03_GreatCowGathering2.head = jarray('int', [Code03_GreatCowGathering2.MAXN])
Code03_GreatCowGathering2.next = jarray('int', [jcast('int', (Code03_GreatCowGathering2.MAXN << (1 & 31)))])
Code03_GreatCowGathering2.to = jarray('int', [jcast('int', (Code03_GreatCowGathering2.MAXN << (1 & 31)))])
Code03_GreatCowGathering2.weight = jarray('int', [jcast('int', (Code03_GreatCowGathering2.MAXN << (1 & 31)))])
Code03_GreatCowGathering2.cnt = jcast('int', 0)
Code03_GreatCowGathering2.best = jcast('int', 0)
Code03_GreatCowGathering2.center = jcast('int', 0)
Code03_GreatCowGathering2.size = jarray('int', [Code03_GreatCowGathering2.MAXN])
Code03_GreatCowGathering2.path = jarray('int', [Code03_GreatCowGathering2.MAXN])
Code03_GreatCowGathering2.ufe = jarray('int', [Code03_GreatCowGathering2.MAXN, 3])
Code03_GreatCowGathering2.stackSize = jcast('int', 0)
Code03_GreatCowGathering2.u = jcast('int', 0)
Code03_GreatCowGathering2.f = jcast('int', 0)
Code03_GreatCowGathering2.e = jcast('int', 0)

if __name__ == '__main__':
    Code03_GreatCowGathering2.main([])

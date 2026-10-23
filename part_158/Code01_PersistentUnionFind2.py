# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 可持久化并查集模版题，Python版
# 数字从1到n，一开始每个数字所在的集合只有自己
# 实现如下三种操作，第i条操作发生后，所有数字的状况记为i版本，操作一共发生m次
# 操作 1 x y : 基于上个操作生成的版本，将x的集合与y的集合合并，生成当前的版本
# 操作 2 x   : 拷贝第x号版本的状况，生成当前的版本
# 操作 3 x y : 拷贝上个操作生成的版本，生成当前的版本，查询x和y是否属于一个集合
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3402
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PersistentUnionFind2:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'rootfa': 'rootfa', 'rootsiz': 'rootsiz', 'ls': 'ls', 'rs': 'rs', 'val': 'val', 'cnt': 'cnt'}
    MAXM = 0
    MAXT = 0
    n = 0
    m = 0
    # rootfa[i] = j，表示father数组，i版本的头节点编号为j
    rootfa = None
    # rootsiz[i] = j，表示siz数组，i版本的头节点编号为j
    rootsiz = None
    # 可持久化father数组和可持久化siz数组，共用一个ls、rs、val
    # 因为可持久化时，分配的节点编号不同，所以可以共用
    ls = None
    rs = None
    val = None
    cnt = 0
    # 建立可持久化的father数组
    @staticmethod
    def buildfa(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code01_PersistentUnionFind2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code01_PersistentUnionFind2.val[rt] = jcast('int', l)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code01_PersistentUnionFind2.ls, rt, Code01_PersistentUnionFind2.buildfa(l, mid))
            jset(Code01_PersistentUnionFind2.rs, rt, Code01_PersistentUnionFind2.buildfa(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 建立可持久化的siz数组
    @staticmethod
    def buildsiz(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_4 := Code01_PersistentUnionFind2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l == r):
            Code01_PersistentUnionFind2.val[rt] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code01_PersistentUnionFind2.ls, rt, Code01_PersistentUnionFind2.buildsiz(l, mid))
            jset(Code01_PersistentUnionFind2.rs, rt, Code01_PersistentUnionFind2.buildsiz(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 来自讲解157，题目1，修改数组中一个位置的值，生成新版本的数组
    # 如果i属于可持久化father数组的节点，那么修改的就是father数组
    # 如果i属于可持久化siz数组的节点，那么修改的就是siz数组
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_7 := Code01_PersistentUnionFind2), (_java_key_8 := 'cnt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code01_PersistentUnionFind2.ls[rt] = jcast('int', Code01_PersistentUnionFind2.ls[i])
        Code01_PersistentUnionFind2.rs[rt] = jcast('int', Code01_PersistentUnionFind2.rs[i])
        if (l == r):
            Code01_PersistentUnionFind2.val[rt] = jcast('int', jobv)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code01_PersistentUnionFind2.ls, rt, Code01_PersistentUnionFind2.update(jobi, jobv, l, mid, Code01_PersistentUnionFind2.ls[rt]))
            else:
                jset(Code01_PersistentUnionFind2.rs, rt, Code01_PersistentUnionFind2.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code01_PersistentUnionFind2.rs[rt]))
        return jcast('int', rt)

    # 来自讲解157，题目1，查询数组中一个位置的值
    # 如果i属于可持久化father数组的节点，那么查询的就是father数组
    # 如果i属于可持久化siz数组的节点，那么查询的就是siz数组
    @staticmethod
    def query(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', Code01_PersistentUnionFind2.val[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobi <= mid):
            return jcast('int', Code01_PersistentUnionFind2.query(jobi, l, mid, Code01_PersistentUnionFind2.ls[i]))
        else:
            return jcast('int', Code01_PersistentUnionFind2.query(jobi, jcast('int', jadd(mid, 1)), r, Code01_PersistentUnionFind2.rs[i]))

    # 基于v版本，查询x的集合头节点，不做扁平化
    @staticmethod
    def find(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        fa = jcast('int', Code01_PersistentUnionFind2.query(x, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootfa[v]))
        while (x != fa):
            x = jcast('int', fa)
            fa = jcast('int', Code01_PersistentUnionFind2.query(x, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootfa[v]))
        return jcast('int', x)

    # v版本已经拷贝了v-1版本，合并x所在的集合和y所在的集合，去更新v版本
    @staticmethod
    def union(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        fx = jcast('int', Code01_PersistentUnionFind2.find(x, v))
        fy = jcast('int', Code01_PersistentUnionFind2.find(y, v))
        if (fx != fy):
            xsiz = jcast('int', Code01_PersistentUnionFind2.query(fx, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootsiz[v]))
            ysiz = jcast('int', Code01_PersistentUnionFind2.query(fy, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootsiz[v]))
            if (xsiz >= ysiz):
                jset(Code01_PersistentUnionFind2.rootfa, v, Code01_PersistentUnionFind2.update(fy, fx, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootfa[v]))
                jset(Code01_PersistentUnionFind2.rootsiz, v, Code01_PersistentUnionFind2.update(fx, jcast('int', jadd(xsiz, ysiz)), 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootsiz[v]))
            else:
                jset(Code01_PersistentUnionFind2.rootfa, v, Code01_PersistentUnionFind2.update(fx, fy, 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootfa[v]))
                jset(Code01_PersistentUnionFind2.rootsiz, v, Code01_PersistentUnionFind2.update(fy, jcast('int', jadd(xsiz, ysiz)), 1, Code01_PersistentUnionFind2.n, Code01_PersistentUnionFind2.rootsiz[v]))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_PersistentUnionFind2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_PersistentUnionFind2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jset(Code01_PersistentUnionFind2.rootfa, 0, Code01_PersistentUnionFind2.buildfa(1, Code01_PersistentUnionFind2.n))
        jset(Code01_PersistentUnionFind2.rootsiz, 0, Code01_PersistentUnionFind2.buildsiz(1, Code01_PersistentUnionFind2.n))
        v = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (v <= Code01_PersistentUnionFind2.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_PersistentUnionFind2.rootfa[v] = jcast('int', Code01_PersistentUnionFind2.rootfa[jcast('int', (v - 1))])
            Code01_PersistentUnionFind2.rootsiz[v] = jcast('int', Code01_PersistentUnionFind2.rootsiz[jcast('int', (v - 1))])
            if (op == 1):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                Code01_PersistentUnionFind2.union(x, y, v)
            else:
                if (op == 2):
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code01_PersistentUnionFind2.rootfa[v] = jcast('int', Code01_PersistentUnionFind2.rootfa[x])
                    Code01_PersistentUnionFind2.rootsiz[v] = jcast('int', Code01_PersistentUnionFind2.rootsiz[x])
                else:
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    y = jcast('int', jcast('int', jget(in_, 'nval')))
                    if (Code01_PersistentUnionFind2.find(x, v) == Code01_PersistentUnionFind2.find(y, v)):
                        jcall(out, 'println', 1)
                    else:
                        jcall(out, 'println', 0)
            v = jcast('int', (v + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PersistentUnionFind2.MAXM = jcast('int', 200001)
Code01_PersistentUnionFind2.MAXT = jcast('int', 8000001)
Code01_PersistentUnionFind2.n = jcast('int', 0)
Code01_PersistentUnionFind2.m = jcast('int', 0)
Code01_PersistentUnionFind2.rootfa = jarray('int', [Code01_PersistentUnionFind2.MAXM])
Code01_PersistentUnionFind2.rootsiz = jarray('int', [Code01_PersistentUnionFind2.MAXM])
Code01_PersistentUnionFind2.ls = jarray('int', [Code01_PersistentUnionFind2.MAXT])
Code01_PersistentUnionFind2.rs = jarray('int', [Code01_PersistentUnionFind2.MAXT])
Code01_PersistentUnionFind2.val = jarray('int', [Code01_PersistentUnionFind2.MAXT])
Code01_PersistentUnionFind2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code01_PersistentUnionFind2.main([])

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

# 颜色平衡的子树，Python递归版
# 一共有n个节点，编号1~n，给定每个节点的颜色值和父亲节点编号
# 输入保证所有节点一定组成一棵树，并且1号节点是树头
# 如果一棵子树中，存在的每种颜色的节点个数都相同，这棵子树叫颜色平衡树
# 打印整棵树中有多少个子树是颜色平衡树
# 1 <= n、颜色值 <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P9233
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 因为树的深度太大，递归函数爆栈了，所以会有两个测试用例无法通过
# 迭代版可以完全通过，就是本节课Code02_ColorBanlance2文件
class Code02_ColorBanlance1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'color': 'color', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'siz': 'siz', 'son': 'son', 'colorCnt': 'colorCnt', 'colorNum': 'colorNum', 'ans': 'ans'}
    MAXN = 0
    n = 0
    color = None
    head = None
    next = None
    to = None
    cnt = 0
    siz = None
    son = None
    # colorCnt[i] = j，表示i这种颜色出现了j次
    colorCnt = None
    # colorNum[i] = j，表示出现次数为i的颜色一共有j种
    colorNum = None
    # 颜色平衡子树的个数
    ans = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_ColorBanlance1.next, ((_java_obj_1 := Code02_ColorBanlance1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_ColorBanlance1.head[u])
        Code02_ColorBanlance1.to[Code02_ColorBanlance1.cnt] = jcast('int', v)
        Code02_ColorBanlance1.head[u] = jcast('int', Code02_ColorBanlance1.cnt)

    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        Code02_ColorBanlance1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_ColorBanlance1.head[u])
        while (e > 0):
            Code02_ColorBanlance1.dfs1(Code02_ColorBanlance1.to[e])
            e = jcast('int', Code02_ColorBanlance1.next[e])
        e = jcast('int', Code02_ColorBanlance1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_ColorBanlance1.to[e])
            Code02_ColorBanlance1.siz[u] = jcast('int', jcast('int', jadd(Code02_ColorBanlance1.siz[u], Code02_ColorBanlance1.siz[v])))
            if ((Code02_ColorBanlance1.son[u] == 0) or (Code02_ColorBanlance1.siz[Code02_ColorBanlance1.son[u]] < Code02_ColorBanlance1.siz[v])):
                Code02_ColorBanlance1.son[u] = jcast('int', v)
            e = jcast('int', Code02_ColorBanlance1.next[e])

    @staticmethod
    def effect(u):
        u = jcast('int', u)
        ((_java_obj_4 := Code02_ColorBanlance1.colorCnt), (_java_key_5 := Code02_ColorBanlance1.color[u]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
        ((_java_obj_7 := Code02_ColorBanlance1.colorNum), (_java_key_8 := jcast('int', (Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]] - 1))), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
        ((_java_obj_10 := Code02_ColorBanlance1.colorNum), (_java_key_11 := Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
        e = jcast('int', Code02_ColorBanlance1.head[u])
        while (e > 0):
            Code02_ColorBanlance1.effect(Code02_ColorBanlance1.to[e])
            e = jcast('int', Code02_ColorBanlance1.next[e])

    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        ((_java_obj_13 := Code02_ColorBanlance1.colorCnt), (_java_key_14 := Code02_ColorBanlance1.color[u]), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]
        ((_java_obj_16 := Code02_ColorBanlance1.colorNum), (_java_key_17 := jcast('int', jadd(Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]], 1))), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]
        ((_java_obj_19 := Code02_ColorBanlance1.colorNum), (_java_key_20 := Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]]), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]
        e = jcast('int', Code02_ColorBanlance1.head[u])
        while (e > 0):
            Code02_ColorBanlance1.cancel(Code02_ColorBanlance1.to[e])
            e = jcast('int', Code02_ColorBanlance1.next[e])

    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        e = jcast('int', Code02_ColorBanlance1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_ColorBanlance1.to[e])
            if (v != Code02_ColorBanlance1.son[u]):
                Code02_ColorBanlance1.dfs2(v, 0)
            e = jcast('int', Code02_ColorBanlance1.next[e])
        if (Code02_ColorBanlance1.son[u] != 0):
            Code02_ColorBanlance1.dfs2(Code02_ColorBanlance1.son[u], 1)
        ((_java_obj_22 := Code02_ColorBanlance1.colorCnt), (_java_key_23 := Code02_ColorBanlance1.color[u]), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]
        ((_java_obj_25 := Code02_ColorBanlance1.colorNum), (_java_key_26 := jcast('int', (Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]] - 1))), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (-1)))), _java_old_27)[4]
        ((_java_obj_28 := Code02_ColorBanlance1.colorNum), (_java_key_29 := Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]]), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]
        e = jcast('int', Code02_ColorBanlance1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_ColorBanlance1.to[e])
            if (v != Code02_ColorBanlance1.son[u]):
                Code02_ColorBanlance1.effect(v)
            e = jcast('int', Code02_ColorBanlance1.next[e])
        if (jcast('int', (Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]] * Code02_ColorBanlance1.colorNum[Code02_ColorBanlance1.colorCnt[Code02_ColorBanlance1.color[u]]])) == Code02_ColorBanlance1.siz[u]):
            Code02_ColorBanlance1.ans = jcast('int', (Code02_ColorBanlance1.ans + 1))
        if (keep == 0):
            Code02_ColorBanlance1.cancel(u)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_ColorBanlance1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        father = 0
        while (i <= Code02_ColorBanlance1.n):
            jcall(in_, 'nextToken')
            Code02_ColorBanlance1.color[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            father = jcast('int', jcast('int', jget(in_, 'nval')))
            if (i != 1):
                Code02_ColorBanlance1.addEdge(father, i)
            i = jcast('int', (i + 1))
        Code02_ColorBanlance1.dfs1(1)
        Code02_ColorBanlance1.dfs2(1, 0)
        jcall(out, 'println', Code02_ColorBanlance1.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ColorBanlance1.MAXN = jcast('int', 200001)
Code02_ColorBanlance1.n = jcast('int', 0)
Code02_ColorBanlance1.color = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.head = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.next = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.to = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.cnt = jcast('int', 0)
Code02_ColorBanlance1.siz = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.son = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.colorCnt = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.colorNum = jarray('int', [Code02_ColorBanlance1.MAXN])
Code02_ColorBanlance1.ans = jcast('int', 0)

if __name__ == '__main__':
    Code02_ColorBanlance1.main([])

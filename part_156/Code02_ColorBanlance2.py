# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 颜色平衡的子树，Python迭代版
# 不会改迭代版，去看讲解118，详解了dfs从递归版改迭代版
# 测试链接 : https://www.luogu.com.cn/problem/P9233
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_ColorBanlance2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'color': 'color', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'siz': 'siz', 'son': 'son', 'colorCnt': 'colorCnt', 'colorNum': 'colorNum', 'ans': 'ans', 'stack1': 'stack1', 'size1': 'size1', 'cur1': 'cur1', 'edge1': 'edge1', 'stack2': 'stack2', 'size2': 'size2', 'cur2': 'cur2', 'keep2': 'keep2', 'edge2': 'edge2'}
    MAXN = 0
    n = 0
    color = None
    head = None
    next = None
    to = None
    cnt = 0
    siz = None
    son = None
    colorCnt = None
    colorNum = None
    ans = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_ColorBanlance2.next, ((_java_obj_1 := Code02_ColorBanlance2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_ColorBanlance2.head[u])
        Code02_ColorBanlance2.to[Code02_ColorBanlance2.cnt] = jcast('int', v)
        Code02_ColorBanlance2.head[u] = jcast('int', Code02_ColorBanlance2.cnt)

    # stack1、size1、cur1、edge1
    # 用于把effect、cancel、dfs1改成迭代版
    stack1 = None
    size1 = 0
    cur1 = 0
    edge1 = 0
    # stack2、size2、cur2、keep2、edge2
    # 用于把dfs2改成迭代版
    stack2 = None
    size2 = 0
    cur2 = 0
    keep2 = 0
    edge2 = 0
    @staticmethod
    def push1(u, e):
        u = jcast('int', u)
        e = jcast('int', e)
        jset(Code02_ColorBanlance2.stack1[Code02_ColorBanlance2.size1], 0, u)
        jset(Code02_ColorBanlance2.stack1[Code02_ColorBanlance2.size1], 1, e)
        Code02_ColorBanlance2.size1 = jcast('int', (Code02_ColorBanlance2.size1 + 1))

    @staticmethod
    def pop1():
        Code02_ColorBanlance2.size1 = jcast('int', (Code02_ColorBanlance2.size1 - 1))
        Code02_ColorBanlance2.cur1 = jcast('int', Code02_ColorBanlance2.stack1[Code02_ColorBanlance2.size1][0])
        Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.stack1[Code02_ColorBanlance2.size1][1])

    @staticmethod
    def push2(u, k, e):
        u = jcast('int', u)
        k = jcast('int', k)
        e = jcast('int', e)
        jset(Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2], 0, u)
        jset(Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2], 1, k)
        jset(Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2], 2, e)
        Code02_ColorBanlance2.size2 = jcast('int', (Code02_ColorBanlance2.size2 + 1))

    @staticmethod
    def pop2():
        Code02_ColorBanlance2.size2 = jcast('int', (Code02_ColorBanlance2.size2 - 1))
        Code02_ColorBanlance2.cur2 = jcast('int', Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2][0])
        Code02_ColorBanlance2.keep2 = jcast('int', Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2][1])
        Code02_ColorBanlance2.edge2 = jcast('int', Code02_ColorBanlance2.stack2[Code02_ColorBanlance2.size2][2])

    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        Code02_ColorBanlance2.size1 = jcast('int', 0)
        Code02_ColorBanlance2.push1(u, jcast('int', (-1)))
        while (Code02_ColorBanlance2.size1 > 0):
            Code02_ColorBanlance2.pop1()
            if (Code02_ColorBanlance2.edge1 == jcast('int', (-1))):
                Code02_ColorBanlance2.siz[Code02_ColorBanlance2.cur1] = jcast('int', 1)
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur1])
            else:
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.next[Code02_ColorBanlance2.edge1])
            if (Code02_ColorBanlance2.edge1 != 0):
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.cur1, Code02_ColorBanlance2.edge1)
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.to[Code02_ColorBanlance2.edge1], jcast('int', (-1)))
            else:
                e = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur1])
                v = 0
                while (e > 0):
                    v = jcast('int', Code02_ColorBanlance2.to[e])
                    Code02_ColorBanlance2.siz[Code02_ColorBanlance2.cur1] = jcast('int', jcast('int', jadd(Code02_ColorBanlance2.siz[Code02_ColorBanlance2.cur1], Code02_ColorBanlance2.siz[v])))
                    if ((Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur1] == 0) or (Code02_ColorBanlance2.siz[Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur1]] < Code02_ColorBanlance2.siz[v])):
                        Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur1] = jcast('int', v)
                    e = jcast('int', Code02_ColorBanlance2.next[e])

    @staticmethod
    def effect(root):
        root = jcast('int', root)
        Code02_ColorBanlance2.size1 = jcast('int', 0)
        Code02_ColorBanlance2.push1(root, jcast('int', (-1)))
        while (Code02_ColorBanlance2.size1 > 0):
            Code02_ColorBanlance2.pop1()
            if (Code02_ColorBanlance2.edge1 == jcast('int', (-1))):
                ((_java_obj_4 := Code02_ColorBanlance2.colorCnt), (_java_key_5 := Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
                ((_java_obj_7 := Code02_ColorBanlance2.colorNum), (_java_key_8 := jcast('int', (Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]] - 1))), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
                ((_java_obj_10 := Code02_ColorBanlance2.colorNum), (_java_key_11 := Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur1])
            else:
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.next[Code02_ColorBanlance2.edge1])
            if (Code02_ColorBanlance2.edge1 != 0):
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.cur1, Code02_ColorBanlance2.edge1)
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.to[Code02_ColorBanlance2.edge1], jcast('int', (-1)))

    @staticmethod
    def cancel(root):
        root = jcast('int', root)
        Code02_ColorBanlance2.size1 = jcast('int', 0)
        Code02_ColorBanlance2.push1(root, jcast('int', (-1)))
        while (Code02_ColorBanlance2.size1 > 0):
            Code02_ColorBanlance2.pop1()
            if (Code02_ColorBanlance2.edge1 == jcast('int', (-1))):
                ((_java_obj_13 := Code02_ColorBanlance2.colorCnt), (_java_key_14 := Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]
                ((_java_obj_16 := Code02_ColorBanlance2.colorNum), (_java_key_17 := jcast('int', jadd(Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]], 1))), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]
                ((_java_obj_19 := Code02_ColorBanlance2.colorNum), (_java_key_20 := Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur1]]), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur1])
            else:
                Code02_ColorBanlance2.edge1 = jcast('int', Code02_ColorBanlance2.next[Code02_ColorBanlance2.edge1])
            if (Code02_ColorBanlance2.edge1 != 0):
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.cur1, Code02_ColorBanlance2.edge1)
                Code02_ColorBanlance2.push1(Code02_ColorBanlance2.to[Code02_ColorBanlance2.edge1], jcast('int', (-1)))

    # 迭代版的dfs2，用edge2变量标记一个节点的不同阶段
    # edge2 == -1，表示第一次来到当前节点，接下来依次处理轻儿子的子树
    # edge2 > 0，表示正在依次处理轻儿子的子树
    # edge2 == 0，表示处理完了所有轻儿子的子树，接下来处理重儿子的子树
    # edge2 == -2，表示处理完了重儿子的子树，轮到启发式合并了
    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        Code02_ColorBanlance2.size2 = jcast('int', 0)
        Code02_ColorBanlance2.push2(u, keep, jcast('int', (-1)))
        while (Code02_ColorBanlance2.size2 > 0):
            Code02_ColorBanlance2.pop2()
            if (Code02_ColorBanlance2.edge2 != jcast('int', (-2))):
                if (Code02_ColorBanlance2.edge2 == jcast('int', (-1))):
                    Code02_ColorBanlance2.edge2 = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur2])
                else:
                    Code02_ColorBanlance2.edge2 = jcast('int', Code02_ColorBanlance2.next[Code02_ColorBanlance2.edge2])
                if (Code02_ColorBanlance2.edge2 > 0):
                    Code02_ColorBanlance2.push2(Code02_ColorBanlance2.cur2, Code02_ColorBanlance2.keep2, Code02_ColorBanlance2.edge2)
                    if (Code02_ColorBanlance2.to[Code02_ColorBanlance2.edge2] != Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur2]):
                        Code02_ColorBanlance2.push2(Code02_ColorBanlance2.to[Code02_ColorBanlance2.edge2], 0, jcast('int', (-1)))
                else:
                    Code02_ColorBanlance2.push2(Code02_ColorBanlance2.cur2, Code02_ColorBanlance2.keep2, jcast('int', (-2)))
                    if (Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur2] != 0):
                        Code02_ColorBanlance2.push2(Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur2], 1, jcast('int', (-1)))
            else:
                ((_java_obj_22 := Code02_ColorBanlance2.colorCnt), (_java_key_23 := Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur2]), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]
                ((_java_obj_25 := Code02_ColorBanlance2.colorNum), (_java_key_26 := jcast('int', (Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur2]] - 1))), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (-1)))), _java_old_27)[4]
                ((_java_obj_28 := Code02_ColorBanlance2.colorNum), (_java_key_29 := Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur2]]), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]
                e = jcast('int', Code02_ColorBanlance2.head[Code02_ColorBanlance2.cur2])
                v = 0
                while (e > 0):
                    v = jcast('int', Code02_ColorBanlance2.to[e])
                    if (v != Code02_ColorBanlance2.son[Code02_ColorBanlance2.cur2]):
                        Code02_ColorBanlance2.effect(v)
                    e = jcast('int', Code02_ColorBanlance2.next[e])
                if (jcast('int', (Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur2]] * Code02_ColorBanlance2.colorNum[Code02_ColorBanlance2.colorCnt[Code02_ColorBanlance2.color[Code02_ColorBanlance2.cur2]]])) == Code02_ColorBanlance2.siz[Code02_ColorBanlance2.cur2]):
                    Code02_ColorBanlance2.ans = jcast('int', (Code02_ColorBanlance2.ans + 1))
                if (Code02_ColorBanlance2.keep2 == 0):
                    Code02_ColorBanlance2.cancel(Code02_ColorBanlance2.cur2)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_ColorBanlance2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        father = 0
        while (i <= Code02_ColorBanlance2.n):
            jcall(in_, 'nextToken')
            Code02_ColorBanlance2.color[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            father = jcast('int', jcast('int', jget(in_, 'nval')))
            if (i != 1):
                Code02_ColorBanlance2.addEdge(father, i)
            i = jcast('int', (i + 1))
        Code02_ColorBanlance2.dfs1(1)
        Code02_ColorBanlance2.dfs2(1, 0)
        jcall(out, 'println', Code02_ColorBanlance2.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ColorBanlance2.MAXN = jcast('int', 200001)
Code02_ColorBanlance2.n = jcast('int', 0)
Code02_ColorBanlance2.color = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.head = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.next = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.to = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.cnt = jcast('int', 0)
Code02_ColorBanlance2.siz = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.son = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.colorCnt = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.colorNum = jarray('int', [Code02_ColorBanlance2.MAXN])
Code02_ColorBanlance2.ans = jcast('int', 0)
Code02_ColorBanlance2.stack1 = jarray('int', [Code02_ColorBanlance2.MAXN, 2])
Code02_ColorBanlance2.size1 = jcast('int', 0)
Code02_ColorBanlance2.cur1 = jcast('int', 0)
Code02_ColorBanlance2.edge1 = jcast('int', 0)
Code02_ColorBanlance2.stack2 = jarray('int', [Code02_ColorBanlance2.MAXN, 3])
Code02_ColorBanlance2.size2 = jcast('int', 0)
Code02_ColorBanlance2.cur2 = jcast('int', 0)
Code02_ColorBanlance2.keep2 = jcast('int', 0)
Code02_ColorBanlance2.edge2 = jcast('int', 0)

if __name__ == '__main__':
    Code02_ColorBanlance2.main([])

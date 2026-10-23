# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 没有上司的舞会
# 某大学有n个职员，编号为1...n
# 他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树
# 父结点就是子结点的直接上司
# 现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数
# 但是如果某个职员的直接上司来参加舞会了
# 那么这个职员就无论如何也不肯来参加舞会了
# 所以请你编程计算邀请哪些职员可以使快乐指数最大
# 返回最大的快乐指数。
# 测试链接 : https://www.luogu.com.cn/problem/P1352
# 本题和讲解037的题目7类似
# 链式链接 : https://leetcode.cn/problems/house-robber-iii/
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Dancing:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'boss': 'boss', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'no': 'no', 'yes': 'yes', 'n': 'n', 'h': 'h'}
    MAXN = 0
    nums = None
    boss = None
    # 链式前向星建图
    head = None
    next = None
    to = None
    cnt = 0
    # 动态规划表
    # no[i] : i为头的整棵树，在i不来的情况下，整棵树能得到的最大快乐值
    no = None
    # no[i] : i为头的整棵树，在i来的情况下，整棵树能得到的最大快乐值
    yes = None
    n = 0
    h = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jstatic('Arrays', 'fill', Code05_Dancing.boss, 1, jcast('int', jadd(n, 1)), True)
        jstatic('Arrays', 'fill', Code05_Dancing.head, 1, jcast('int', jadd(n, 1)), 0)
        Code05_Dancing.cnt = jcast('int', 1)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_Dancing.next[Code05_Dancing.cnt] = jcast('int', Code05_Dancing.head[u])
        Code05_Dancing.to[Code05_Dancing.cnt] = jcast('int', v)
        jset(Code05_Dancing.head, u, ((_java_obj_1 := Code05_Dancing), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            try:
                Code05_Dancing.n = jcast('int', jcast('int', jget(in_, 'nval')))
                Code05_Dancing.build(Code05_Dancing.n)
                i = jcast('int', 1)
                while (i <= Code05_Dancing.n):
                    jcall(in_, 'nextToken')
                    Code05_Dancing.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                low = 0
                high = 0
                while (i < Code05_Dancing.n):
                    jcall(in_, 'nextToken')
                    low = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    high = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code05_Dancing.addEdge(high, low)
                    Code05_Dancing.boss[low] = jcast('boolean', False)
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= Code05_Dancing.n):
                    try:
                        if Code05_Dancing.boss[i]:
                            Code05_Dancing.h = jcast('int', i)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                Code05_Dancing.f(Code05_Dancing.h)
                jcall(out, 'println', jstatic('Math', 'max', Code05_Dancing.no[Code05_Dancing.h], Code05_Dancing.yes[Code05_Dancing.h]))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def f(u):
        u = jcast('int', u)
        Code05_Dancing.no[u] = jcast('int', 0)
        Code05_Dancing.yes[u] = jcast('int', Code05_Dancing.nums[u])
        ei = jcast('int', Code05_Dancing.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code05_Dancing.to[ei])
            Code05_Dancing.f(v)
            ((_java_obj_6 := Code05_Dancing.no), (_java_key_7 := u), jset(_java_obj_6, _java_key_7, jcast('int', jadd(jget(_java_obj_6, _java_key_7), jstatic('Math', 'max', Code05_Dancing.no[v], Code05_Dancing.yes[v])))))[2]
            Code05_Dancing.yes[u] = jcast('int', jcast('int', jadd(Code05_Dancing.yes[u], Code05_Dancing.no[v])))
            ei = jcast('int', Code05_Dancing.next[ei])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Dancing.MAXN = jcast('int', 6001)
Code05_Dancing.nums = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.boss = jarray('boolean', [Code05_Dancing.MAXN])
Code05_Dancing.head = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.next = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.to = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.cnt = jcast('int', 0)
Code05_Dancing.no = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.yes = jarray('int', [Code05_Dancing.MAXN])
Code05_Dancing.n = jcast('int', 0)
Code05_Dancing.h = jcast('int', 0)

if __name__ == '__main__':
    Code05_Dancing.main([])

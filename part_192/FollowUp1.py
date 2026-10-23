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

# 有向图的基环树找环，Python版
# 这个文件课上没讲，有向图中找到基环，非常容易理解
# 无向图的入环节点u，可以发现环的末尾节点v，因为边是无向的
# 于是用dfn[u] < dfn[v]来判断环
# 但是对有向图来说，假设出现的环如下
# 入环节点a -> b -> c -> 环的末尾节点d -> 入环节点a
# 不能放在入环节点a处判断，因为环的末尾节点d，不一定在a的邻居列表里
# 边是有向的，也许只有d到a的边，不一定有a到d的边
# 所以有向图的基环树找环，判断的时机，放在环的末尾节点处，具体说明如下
# 节点一共三种状态，0表示没有访问，1表示在递归路径上，2表示递归执行完了
# 依然记录每个点，在递归路径的前一个节点，也就是课上讲的from信息
# 来到节点u时，判断儿子节点v，看看是否在递归路径上
# 是的话，从u开始通过from走回v，环路就找全了，v是入环节点，u是环末尾点
# 调用时扫过所有节点，没有访问过的节点去调用dfs，直到环被找到
class FollowUp1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'state': 'state', 'from': 'from_', 'cycle': 'cycle'}
    MAXN = 0
    # 建图
    head = None
    nxt = None
    to = None
    cntg = 0
    # 0表示没访问过，1表示在递归路径上，2表示递归执行完了
    state = None
    # 记录每个点在递归路径的前一个节点
    from_ = None
    # 标记环上节点
    cycle = None
    # 返回值表示是否找到了环
    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        FollowUp1.state[u] = jcast('int', 1)
        find = jcast('boolean', False)
        e = jcast('int', FollowUp1.head[u])
        while (e > 0):
            try:
                v = jcast('int', FollowUp1.to[e])
                if (FollowUp1.state[v] == 0):
                    FollowUp1.from_[v] = jcast('int', u)
                    if FollowUp1.dfs(v):
                        find = jcast('boolean', True)
                else:
                    if (FollowUp1.state[v] == 1):
                        # u -> v，此时v在递归路径上，说明发现了环
                        # v是入环节点，u是环末尾点，利用from得到整个环
                        # 这里执行的操作是标记环上节点，当然也可以生成环的其他信息
                        FollowUp1.cycle[v] = jcast('boolean', True)
                        i = jcast('int', u)
                        while (i != v):
                            FollowUp1.cycle[i] = jcast('boolean', True)
                            i = jcast('int', FollowUp1.from_[i])
                        find = jcast('boolean', True)
                if find:
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            e = jcast('int', FollowUp1.nxt[e])
        FollowUp1.state[u] = jcast('int', 2)
        return jcast('boolean', find)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUp1.MAXN = jcast('int', 100001)
FollowUp1.head = jarray('int', [FollowUp1.MAXN])
FollowUp1.nxt = jarray('int', [FollowUp1.MAXN])
FollowUp1.to = jarray('int', [FollowUp1.MAXN])
FollowUp1.cntg = jcast('int', 0)
FollowUp1.state = jarray('int', [FollowUp1.MAXN])
FollowUp1.from_ = jarray('int', [FollowUp1.MAXN])
FollowUp1.cycle = jarray('boolean', [FollowUp1.MAXN])

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

# 仙人掌遍历和找环的过程，Python版
class ShowDetail2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'fromWeight': 'fromWeight'}
    MAXN = 0
    MAXM = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    fromWeight = None
    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(ShowDetail2.dfn, u, jset(ShowDetail2.low, u, ((_java_obj_1 := ShowDetail2), (_java_key_2 := 'cntd'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]))
        jset(ShowDetail2.sta, ((_java_obj_4 := ShowDetail2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        e = jcast('int', ShowDetail2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', ShowDetail2.to[e])
                w = jcast('int', ShowDetail2.weight[e])
                if (ShowDetail2.dfn[v] == 0):
                    ShowDetail2.tarjan(v, e)
                    # 设置v的from信息
                    ShowDetail2.fromWeight[v] = jcast('int', w)
                    # 没有扎起口袋
                    if (ShowDetail2.low[v] < ShowDetail2.dfn[u]):
                        jset(ShowDetail2.low, u, jstatic('Math', 'min', ShowDetail2.low[u], ShowDetail2.low[v]))
                    else:
                        if (ShowDetail2.low[v] > ShowDetail2.dfn[u]):
                            # 发现割边，实现有关割边的处理
                            ShowDetail2.top = jcast('int', (ShowDetail2.top - 1))
                        else:
                            None
                            # 发现了环，实现有关环的处理
                else:
                    # 发现回边
                    if (ShowDetail2.dfn[v] < ShowDetail2.dfn[u]):
                        # 闭合边的信息给入环节点
                        ShowDetail2.fromWeight[v] = jcast('int', w)
                        jset(ShowDetail2.low, u, jstatic('Math', 'min', ShowDetail2.low[u], ShowDetail2.dfn[v]))
                    # 如果发现弃边，一般什么也不做
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            e = jcast('int', ShowDetail2.nxt[e])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetail2.MAXN = jcast('int', 100001)
ShowDetail2.MAXM = jcast('int', 200001)
ShowDetail2.head = jarray('int', [ShowDetail2.MAXN])
ShowDetail2.nxt = jarray('int', [ShowDetail2.MAXM])
ShowDetail2.to = jarray('int', [ShowDetail2.MAXM])
ShowDetail2.weight = jarray('int', [ShowDetail2.MAXM])
ShowDetail2.cntg = jcast('int', 0)
ShowDetail2.dfn = jarray('int', [ShowDetail2.MAXN])
ShowDetail2.low = jarray('int', [ShowDetail2.MAXN])
ShowDetail2.cntd = jcast('int', 0)
ShowDetail2.sta = jarray('int', [ShowDetail2.MAXN])
ShowDetail2.top = jcast('int', 0)
ShowDetail2.fromWeight = jarray('int', [ShowDetail2.MAXN])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 仙人掌遍历和找环的过程，Python版
class ShowDetail1:
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
        jset(ShowDetail1.dfn, u, jset(ShowDetail1.low, u, ((_java_obj_1 := ShowDetail1), (_java_key_2 := 'cntd'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]))
        jset(ShowDetail1.sta, ((_java_obj_4 := ShowDetail1), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        e = jcast('int', ShowDetail1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', ShowDetail1.to[e])
                w = jcast('int', ShowDetail1.weight[e])
                if (ShowDetail1.dfn[v] == 0):
                    ShowDetail1.tarjan(v, e)
                    # 设置v的from信息
                    ShowDetail1.fromWeight[v] = jcast('int', w)
                    # 没有扎起口袋
                    if (ShowDetail1.low[v] < ShowDetail1.dfn[u]):
                        jset(ShowDetail1.low, u, jstatic('Math', 'min', ShowDetail1.low[u], ShowDetail1.low[v]))
                    else:
                        if (ShowDetail1.low[v] > ShowDetail1.dfn[u]):
                            # 发现割边，实现有关割边的处理
                            ShowDetail1.top = jcast('int', (ShowDetail1.top - 1))
                        else:
                            None
                            # 发现了环，实现有关环的处理
                else:
                    # 发现回边
                    if (ShowDetail1.dfn[v] < ShowDetail1.dfn[u]):
                        # 闭合边的信息给入环节点
                        ShowDetail1.fromWeight[v] = jcast('int', w)
                        jset(ShowDetail1.low, u, jstatic('Math', 'min', ShowDetail1.low[u], ShowDetail1.dfn[v]))
                    # 如果发现弃边，一般什么也不做
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            e = jcast('int', ShowDetail1.nxt[e])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetail1.MAXN = jcast('int', 100001)
ShowDetail1.MAXM = jcast('int', 200001)
ShowDetail1.head = jarray('int', [ShowDetail1.MAXN])
ShowDetail1.nxt = jarray('int', [ShowDetail1.MAXM])
ShowDetail1.to = jarray('int', [ShowDetail1.MAXM])
ShowDetail1.weight = jarray('int', [ShowDetail1.MAXM])
ShowDetail1.cntg = jcast('int', 0)
ShowDetail1.dfn = jarray('int', [ShowDetail1.MAXN])
ShowDetail1.low = jarray('int', [ShowDetail1.MAXN])
ShowDetail1.cntd = jcast('int', 0)
ShowDetail1.sta = jarray('int', [ShowDetail1.MAXN])
ShowDetail1.top = jcast('int', 0)
ShowDetail1.fromWeight = jarray('int', [ShowDetail1.MAXN])

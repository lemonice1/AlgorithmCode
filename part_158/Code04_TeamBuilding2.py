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

# 团建，Python版
# 一共有n个人，每个人给定组号，一共有m条边，代表两人之间有矛盾
# 一共有k个小组，可能有的组没人，但是组依然存在
# 假设组a和组b，两个组的人一起去团建，组a和组b的所有人，可以重新打乱
# 如果所有人最多分成两个集团，每人都要参加划分，并且每个集团的内部不存在矛盾
# 那么组a和组b就叫做一个"合法组对"，注意，组b和组a就不用重复计算了
# 一共有k个组，随意选两个组的情况很多，计算一共有多少个"合法组对"
# 1 <= n、m、k <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1444C
# 测试链接 : https://codeforces.com/problemset/problem/1444/C
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TeamBuilding2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'k': 'k', 'team': 'team', 'edge': 'edge', 'crossEdge': 'crossEdge', 'cnt': 'cnt', 'conflict': 'conflict', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize'}
    MAXN = 0
    n = 0
    m = 0
    k = 0
    # 每个节点的组号
    team = None
    # 每条边有两个端点
    edge = None
    # 两个端点为不同组的边，u、uteam、v、vteam
    crossEdge = None
    # 两个端点为不同组的边的数量
    cnt = 0
    # conflict[i] = true，表示i号组自己去划分二分图，依然有冲突
    # conflict[i] = false，表示i号组自己去划分二分图，没有冲突
    conflict = None
    # 可撤销并查集
    father = None
    siz = None
    rollback = None
    opsize = 0
    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code04_TeamBuilding2.father[i]):
            i = jcast('int', Code04_TeamBuilding2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code04_TeamBuilding2.find(x))
        fy = jcast('int', Code04_TeamBuilding2.find(y))
        if (Code04_TeamBuilding2.siz[fx] < Code04_TeamBuilding2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code04_TeamBuilding2.father[fy] = jcast('int', fx)
        Code04_TeamBuilding2.siz[fx] = jcast('int', jcast('int', jadd(Code04_TeamBuilding2.siz[fx], Code04_TeamBuilding2.siz[fy])))
        jset(Code04_TeamBuilding2.rollback[((_java_obj_1 := Code04_TeamBuilding2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
        jset(Code04_TeamBuilding2.rollback[Code04_TeamBuilding2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code04_TeamBuilding2.rollback[Code04_TeamBuilding2.opsize][0])
        fy = jcast('int', Code04_TeamBuilding2.rollback[((_java_obj_4 := Code04_TeamBuilding2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]][1])
        Code04_TeamBuilding2.father[fy] = jcast('int', fy)
        Code04_TeamBuilding2.siz[fx] = jcast('int', jcast('int', (Code04_TeamBuilding2.siz[fx] - Code04_TeamBuilding2.siz[fy])))

    @staticmethod
    def filter():
        i = jcast('int', 1)
        while (i <= jcast('int', (2 * Code04_TeamBuilding2.n))):
            Code04_TeamBuilding2.father[i] = jcast('int', i)
            Code04_TeamBuilding2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_TeamBuilding2.m):
            try:
                u = jcast('int', Code04_TeamBuilding2.edge[i][0])
                v = jcast('int', Code04_TeamBuilding2.edge[i][1])
                if (Code04_TeamBuilding2.team[u] < Code04_TeamBuilding2.team[v]):
                    jset(Code04_TeamBuilding2.crossEdge[((_java_obj_8 := Code04_TeamBuilding2), (_java_key_9 := 'cnt'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3]], 0, u)
                    jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 1, Code04_TeamBuilding2.team[u])
                    jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 2, v)
                    jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 3, Code04_TeamBuilding2.team[v])
                else:
                    if (Code04_TeamBuilding2.team[u] > Code04_TeamBuilding2.team[v]):
                        jset(Code04_TeamBuilding2.crossEdge[((_java_obj_11 := Code04_TeamBuilding2), (_java_key_12 := 'cnt'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3]], 0, v)
                        jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 1, Code04_TeamBuilding2.team[v])
                        jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 2, u)
                        jset(Code04_TeamBuilding2.crossEdge[Code04_TeamBuilding2.cnt], 3, Code04_TeamBuilding2.team[u])
                    else:
                        if Code04_TeamBuilding2.conflict[Code04_TeamBuilding2.team[u]]:
                            raise JContinue(None)
                        if (Code04_TeamBuilding2.find(u) == Code04_TeamBuilding2.find(v)):
                            Code04_TeamBuilding2.k = jcast('int', (Code04_TeamBuilding2.k - 1))
                            jset(Code04_TeamBuilding2.conflict, Code04_TeamBuilding2.team[u], True)
                        else:
                            Code04_TeamBuilding2.union(u, jcast('int', jadd(v, Code04_TeamBuilding2.n)))
                            Code04_TeamBuilding2.union(v, jcast('int', jadd(u, Code04_TeamBuilding2.n)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code04_TeamBuilding2.crossEdge, 1, jcast('int', jadd(Code04_TeamBuilding2.cnt, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else (a[3] - b[3]))))
        ans = jcast('long', jcast('long', jdiv(jcast('long', (jcast('long', Code04_TeamBuilding2.k) * jcast('int', (Code04_TeamBuilding2.k - 1)))), 2)))
        u = 0
        uteam = 0
        v = 0
        vteam = 0
        unionCnt = 0
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code04_TeamBuilding2.cnt):
            try:
                uteam = jcast('int', Code04_TeamBuilding2.crossEdge[l][1])
                vteam = jcast('int', Code04_TeamBuilding2.crossEdge[l][3])
                while (((jcast('int', jadd(r, 1)) <= Code04_TeamBuilding2.cnt) and (Code04_TeamBuilding2.crossEdge[jcast('int', jadd(r, 1))][1] == uteam)) and (Code04_TeamBuilding2.crossEdge[jcast('int', jadd(r, 1))][3] == vteam)):
                    r = jcast('int', (r + 1))
                if (Code04_TeamBuilding2.conflict[uteam] or Code04_TeamBuilding2.conflict[vteam]):
                    raise JContinue(None)
                unionCnt = jcast('int', 0)
                i = jcast('int', l)
                while (i <= r):
                    try:
                        u = jcast('int', Code04_TeamBuilding2.crossEdge[i][0])
                        v = jcast('int', Code04_TeamBuilding2.crossEdge[i][2])
                        if (Code04_TeamBuilding2.find(u) == Code04_TeamBuilding2.find(v)):
                            ans = jcast('long', (ans - 1))
                            raise JBreak(None)
                        else:
                            Code04_TeamBuilding2.union(u, jcast('int', jadd(v, Code04_TeamBuilding2.n)))
                            Code04_TeamBuilding2.union(v, jcast('int', jadd(u, Code04_TeamBuilding2.n)))
                            unionCnt = jcast('int', jcast('int', jadd(unionCnt, 2)))
                    except JContinue as _java_control_15:
                        if _java_control_15.label not in (None,):
                            raise
                    except JBreak as _java_control_15:
                        if _java_control_15.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= unionCnt):
                    Code04_TeamBuilding2.undo()
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_14:
                if _java_control_14.label not in (None,):
                    raise
            except JBreak as _java_control_14:
                if _java_control_14.label not in (None,):
                    raise
                break
            l = jcast('int', (r := jcast('int', (r + (1)))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_TeamBuilding2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_TeamBuilding2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_TeamBuilding2.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_TeamBuilding2.n):
            jcall(in_, 'nextToken')
            Code04_TeamBuilding2.team[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_TeamBuilding2.m):
            jcall(in_, 'nextToken')
            jset(Code04_TeamBuilding2.edge[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_TeamBuilding2.edge[i], 1, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_TeamBuilding2.filter()
        jcall(out, 'println', Code04_TeamBuilding2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TeamBuilding2.MAXN = jcast('int', 500001)
Code04_TeamBuilding2.n = jcast('int', 0)
Code04_TeamBuilding2.m = jcast('int', 0)
Code04_TeamBuilding2.k = jcast('int', 0)
Code04_TeamBuilding2.team = jarray('int', [Code04_TeamBuilding2.MAXN])
Code04_TeamBuilding2.edge = jarray('int', [Code04_TeamBuilding2.MAXN, 2])
Code04_TeamBuilding2.crossEdge = jarray('int', [Code04_TeamBuilding2.MAXN, 4])
Code04_TeamBuilding2.cnt = jcast('int', 0)
Code04_TeamBuilding2.conflict = jarray('boolean', [Code04_TeamBuilding2.MAXN])
Code04_TeamBuilding2.father = jarray('int', [jcast('int', (Code04_TeamBuilding2.MAXN << (1 & 31)))])
Code04_TeamBuilding2.siz = jarray('int', [jcast('int', (Code04_TeamBuilding2.MAXN << (1 & 31)))])
Code04_TeamBuilding2.rollback = jarray('int', [jcast('int', (Code04_TeamBuilding2.MAXN << (1 & 31))), 2])
Code04_TeamBuilding2.opsize = jcast('int', 0)

if __name__ == '__main__':
    Code04_TeamBuilding2.main([])

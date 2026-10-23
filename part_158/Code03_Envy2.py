# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 同在最小生成树里，Python版
# 一共有n个点，m条无向边，每条边有边权，图保证是连通的
# 一共有q次查询，每条查询都给定参数k，表示该查询涉及k条边
# 然后依次给出k条边的编号，打印这k条边能否同时出现在一颗最小生成树上
# 1 <= n、m、q、所有查询涉及边的总量 <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF891C
# 测试链接 : https://codeforces.com/problemset/problem/891/C
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Envy2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'q': 'q', 'k': 'k', 'edge': 'edge', 'queries': 'queries', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    q = 0
    k = 0
    # 节点u、节点v、边权w
    edge = None
    # 节点u、节点v、边权w、问题编号i
    queries = None
    # 可撤销并查集
    father = None
    siz = None
    rollback = None
    opsize = 0
    # 答案数组
    ans = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code03_Envy2.father[i]):
            i = jcast('int', Code03_Envy2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code03_Envy2.find(x))
        fy = jcast('int', Code03_Envy2.find(y))
        if (Code03_Envy2.siz[fx] < Code03_Envy2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code03_Envy2.father[fy] = jcast('int', fx)
        Code03_Envy2.siz[fx] = jcast('int', jcast('int', jadd(Code03_Envy2.siz[fx], Code03_Envy2.siz[fy])))
        jset(Code03_Envy2.rollback[((_java_obj_1 := Code03_Envy2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
        jset(Code03_Envy2.rollback[Code03_Envy2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code03_Envy2.rollback[Code03_Envy2.opsize][0])
        fy = jcast('int', Code03_Envy2.rollback[((_java_obj_4 := Code03_Envy2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]][1])
        Code03_Envy2.father[fy] = jcast('int', fy)
        Code03_Envy2.siz[fx] = jcast('int', jcast('int', (Code03_Envy2.siz[fx] - Code03_Envy2.siz[fy])))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code03_Envy2.n):
            Code03_Envy2.father[i] = jcast('int', i)
            Code03_Envy2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_Envy2.edge, 1, jcast('int', jadd(Code03_Envy2.m, 1)), (lambda a, b: (a[2] - b[2])))
        jstatic('Arrays', 'sort', Code03_Envy2.queries, 1, jcast('int', jadd(Code03_Envy2.k, 1)), (lambda a, b: ((a[2] - b[2]) if (a[2] != b[2]) else (a[3] - b[3]))))
        jstatic('Arrays', 'fill', Code03_Envy2.ans, 1, jcast('int', jadd(Code03_Envy2.q, 1)), True)

    @staticmethod
    def compute():
        ei = jcast('int', 1)
        queryId = 0
        unionCnt = 0
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code03_Envy2.k):
            try:
                while (((jcast('int', jadd(r, 1)) <= Code03_Envy2.k) and (Code03_Envy2.queries[l][2] == Code03_Envy2.queries[jcast('int', jadd(r, 1))][2])) and (Code03_Envy2.queries[l][3] == Code03_Envy2.queries[jcast('int', jadd(r, 1))][3])):
                    r = jcast('int', (r + 1))
                # 添加小于当前边权的边，利用Kruskal算法增加连通性，ei是不回退的
                while ((ei <= Code03_Envy2.m) and (Code03_Envy2.edge[ei][2] < Code03_Envy2.queries[l][2])):
                    if (Code03_Envy2.find(Code03_Envy2.edge[ei][0]) != Code03_Envy2.find(Code03_Envy2.edge[ei][1])):
                        Code03_Envy2.union(Code03_Envy2.edge[ei][0], Code03_Envy2.edge[ei][1])
                    ei = jcast('int', (ei + 1))
                queryId = jcast('int', Code03_Envy2.queries[l][3])
                if (not Code03_Envy2.ans[queryId]):
                    raise JContinue(None)
                unionCnt = jcast('int', 0)
                i = jcast('int', l)
                while (i <= r):
                    try:
                        if (Code03_Envy2.find(Code03_Envy2.queries[i][0]) == Code03_Envy2.find(Code03_Envy2.queries[i][1])):
                            Code03_Envy2.ans[queryId] = jcast('boolean', False)
                            raise JBreak(None)
                        else:
                            Code03_Envy2.union(Code03_Envy2.queries[i][0], Code03_Envy2.queries[i][1])
                            unionCnt = jcast('int', (unionCnt + 1))
                    except JContinue as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                    except JBreak as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= unionCnt):
                    Code03_Envy2.undo()
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_Envy2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_Envy2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_Envy2.m):
            jcall(in_, 'nextToken')
            jset(Code03_Envy2.edge[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code03_Envy2.edge[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code03_Envy2.edge[i], 2, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(in_, 'nextToken')
        Code03_Envy2.q = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_Envy2.k = jcast('int', 0)
        i = jcast('int', 1)
        s = 0
        while (i <= Code03_Envy2.q):
            jcall(in_, 'nextToken')
            s = jcast('int', jcast('int', jget(in_, 'nval')))
            j = jcast('int', 1)
            ei = 0
            while (j <= s):
                jcall(in_, 'nextToken')
                ei = jcast('int', jcast('int', jget(in_, 'nval')))
                jset(Code03_Envy2.queries[((_java_obj_9 := Code03_Envy2), (_java_key_10 := 'k'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3]], 0, Code03_Envy2.edge[ei][0])
                jset(Code03_Envy2.queries[Code03_Envy2.k], 1, Code03_Envy2.edge[ei][1])
                jset(Code03_Envy2.queries[Code03_Envy2.k], 2, Code03_Envy2.edge[ei][2])
                jset(Code03_Envy2.queries[Code03_Envy2.k], 3, i)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code03_Envy2.prepare()
        Code03_Envy2.compute()
        i = jcast('int', 1)
        while (i <= Code03_Envy2.q):
            if Code03_Envy2.ans[i]:
                jcall(out, 'println', 'YES')
            else:
                jcall(out, 'println', 'NO')
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Envy2.MAXN = jcast('int', 500001)
Code03_Envy2.n = jcast('int', 0)
Code03_Envy2.m = jcast('int', 0)
Code03_Envy2.q = jcast('int', 0)
Code03_Envy2.k = jcast('int', 0)
Code03_Envy2.edge = jarray('int', [Code03_Envy2.MAXN, 3])
Code03_Envy2.queries = jarray('int', [Code03_Envy2.MAXN, 4])
Code03_Envy2.father = jarray('int', [Code03_Envy2.MAXN])
Code03_Envy2.siz = jarray('int', [Code03_Envy2.MAXN])
Code03_Envy2.rollback = jarray('int', [jcast('int', (Code03_Envy2.MAXN << (1 & 31))), 2])
Code03_Envy2.opsize = jcast('int', 0)
Code03_Envy2.ans = jarray('boolean', [Code03_Envy2.MAXN])

if __name__ == '__main__':
    Code03_Envy2.main([])

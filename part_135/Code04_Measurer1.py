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

# 倍杀测量者
# 如果 A的分数 >= B的分数 * k，k是正实数，就称 A k倍杀 B，或称 B被A k倍杀了
# 一场比赛中，一共有n个选手，有m1条誓言记录，有m2条选手得分记录，得分只可能是正实数
# 类型1的誓言 u v k : 选手u 没有k倍杀 选手v，那么选手u就穿女装
# 类型2的誓言 u v k : 选手u 被选手v k倍杀了，那么选手u就穿女装
# 选手的得分    u w : 选手u得了w分，如果某选手没有得分记录，按照尽量不穿女装的情况推测
# 你希望看到比赛后有人穿女装，但不想看到很多人穿女装，于是想制定正实数ans，效果如下
# 类型1的誓言，比例调整成(k-ans)，类型2的誓言，比例调整成(k+ans)，即提高了穿女装的条件
# 计算ans最大多少，依然有人穿女装，保留小数点后4位，如果不干预也没人穿女装，返回-1
# 1 <= n, m1, m2 <= 1000
# 1 <= k <= 10
# 1 <= w <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4926
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Measurer1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'sml': 'sml', 'n': 'n', 'm1': 'm1', 'm2': 'm2', 'vow': 'vow', 'score': 'score', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'dist': 'dist', 'update': 'update', 'MAXQ': 'MAXQ', 'queue': 'queue', 'h': 'h', 't': 't', 'enter': 'enter'}
    MAXN = 0
    MAXM = 0
    INF = 0.0
    sml = 0.0
    n = 0
    m1 = 0
    m2 = 0
    # 誓言记录(誓言类型, u, v, k)
    vow = None
    # 得分记录(u, w)
    score = None
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # spfa需要
    dist = None
    update = None
    MAXQ = 0
    queue = None
    h = 0
    t = 0
    enter = None
    @staticmethod
    def prepare():
        Code04_Measurer1.cnt = jcast('int', 1)
        Code04_Measurer1.h = jcast('int', jset(Code04_Measurer1, 't', 0))
        jstatic('Arrays', 'fill', Code04_Measurer1.head, 0, jcast('int', jadd(Code04_Measurer1.n, 2)), 0)
        jstatic('Arrays', 'fill', Code04_Measurer1.dist, 0, jcast('int', jadd(Code04_Measurer1.n, 2)), Code04_Measurer1.INF)
        jstatic('Arrays', 'fill', Code04_Measurer1.update, 0, jcast('int', jadd(Code04_Measurer1.n, 2)), 0)
        jstatic('Arrays', 'fill', Code04_Measurer1.enter, 0, jcast('int', jadd(Code04_Measurer1.n, 2)), False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('double', w)
        Code04_Measurer1.next[Code04_Measurer1.cnt] = jcast('int', Code04_Measurer1.head[u])
        Code04_Measurer1.to[Code04_Measurer1.cnt] = jcast('int', v)
        Code04_Measurer1.weight[Code04_Measurer1.cnt] = jcast('double', w)
        jset(Code04_Measurer1.head, u, ((_java_obj_1 := Code04_Measurer1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def compute():
        l = jcast('double', 0)
        r = jcast('double', Code04_Measurer1.INF)
        m = 0.0
        ans = jcast('double', 0)
        while ((r - l) >= Code04_Measurer1.sml):
            m = jcast('double', jdiv(jadd(l, r), 2))
            if Code04_Measurer1.check(m):
                ans = jcast('double', m)
                l = jcast('double', jadd(m, Code04_Measurer1.sml))
            else:
                r = jcast('double', (m - Code04_Measurer1.sml))
        return jcast('double', ans)

    # 是否有人穿女装
    @staticmethod
    def check(limit):
        limit = jcast('double', limit)
        Code04_Measurer1.prepare()
        # 0号点是连通超级源点，保证图的连通
        i = jcast('int', 1)
        while (i <= Code04_Measurer1.n):
            Code04_Measurer1.addEdge(0, i, 0)
            i = jcast('int', (i + 1))
        # 倍杀关系的建边
        i = jcast('int', 1)
        while (i <= Code04_Measurer1.m1):
            if (Code04_Measurer1.vow[i][0] == 1):
                # 课上的代码没有这个判断，加上才是正确的，防止log里出现负数
                if (jadd((-limit), Code04_Measurer1.vow[i][3]) >= 0):
                    Code04_Measurer1.addEdge(Code04_Measurer1.vow[i][1], Code04_Measurer1.vow[i][2], (-jstatic('Math', 'log', jadd((-limit), Code04_Measurer1.vow[i][3]))))
            else:
                # 因为类型2的誓言是<关系，所以减去最小精度后，就可以认为是<=关系
                Code04_Measurer1.addEdge(Code04_Measurer1.vow[i][1], Code04_Measurer1.vow[i][2], jstatic('Math', 'log', (jadd(limit, Code04_Measurer1.vow[i][3]) - Code04_Measurer1.sml)))
            i = jcast('int', (i + 1))
        # n+1号点是限制超级源点，保证确定得分的选手之间的关系
        # 此实现合并了两个超级源点；比较算法时需注意这一图模型差异
        # 原理上两个超级源点一定要分开，课上进行了重点讲解
        i = jcast('int', 1)
        while (i <= Code04_Measurer1.m2):
            Code04_Measurer1.addEdge(jcast('int', jadd(Code04_Measurer1.n, 1)), Code04_Measurer1.score[i][0], jstatic('Math', 'log', Code04_Measurer1.score[i][1]))
            Code04_Measurer1.addEdge(Code04_Measurer1.score[i][0], jcast('int', jadd(Code04_Measurer1.n, 1)), (-jstatic('Math', 'log', Code04_Measurer1.score[i][1])))
            i = jcast('int', (i + 1))
        return jcast('boolean', Code04_Measurer1.spfa(0))

    @staticmethod
    def spfa(s):
        s = jcast('int', s)
        Code04_Measurer1.dist[s] = jcast('double', 0)
        Code04_Measurer1.update[s] = jcast('int', 1)
        jset(Code04_Measurer1.queue, ((_java_obj_4 := Code04_Measurer1), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], s)
        Code04_Measurer1.enter[s] = jcast('boolean', True)
        while (Code04_Measurer1.h < Code04_Measurer1.t):
            u = jcast('int', Code04_Measurer1.queue[((_java_obj_7 := Code04_Measurer1), (_java_key_8 := 'h'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            Code04_Measurer1.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code04_Measurer1.head[u])
            while (ei > 0):
                v = jcast('int', Code04_Measurer1.to[ei])
                w = jcast('double', Code04_Measurer1.weight[ei])
                if (Code04_Measurer1.dist[v] > jadd(Code04_Measurer1.dist[u], w)):
                    Code04_Measurer1.dist[v] = jcast('double', jadd(Code04_Measurer1.dist[u], w))
                    if (not Code04_Measurer1.enter[v]):
                        # 0...n+1号点，一共n+2个点，所以这里判断 > n + 1
                        if (((_java_obj_10 := Code04_Measurer1.update), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] > jcast('int', jadd(Code04_Measurer1.n, 1))):
                            return jcast('boolean', True)
                        jset(Code04_Measurer1.queue, ((_java_obj_13 := Code04_Measurer1), (_java_key_14 := 't'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4], v)
                        Code04_Measurer1.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code04_Measurer1.next[ei])
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Measurer1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Measurer1.m1 = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Measurer1.m2 = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_Measurer1.m1):
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.vow[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.vow[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.vow[i], 2, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.vow[i], 3, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Measurer1.m2):
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.score[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_Measurer1.score[i], 1, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        ans = jcast('double', Code04_Measurer1.compute())
        if (ans == 0):
            jcall(out, 'println', '-1')
        else:
            jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Measurer1.MAXN = jcast('int', 1002)
Code04_Measurer1.MAXM = jcast('int', 3001)
Code04_Measurer1.INF = jcast('double', 10000000000.0)
Code04_Measurer1.sml = jcast('double', 1e-06)
Code04_Measurer1.n = jcast('int', 0)
Code04_Measurer1.m1 = jcast('int', 0)
Code04_Measurer1.m2 = jcast('int', 0)
Code04_Measurer1.vow = jarray('int', [Code04_Measurer1.MAXN, 4])
Code04_Measurer1.score = jarray('int', [Code04_Measurer1.MAXN, 2])
Code04_Measurer1.head = jarray('int', [Code04_Measurer1.MAXN])
Code04_Measurer1.next = jarray('int', [Code04_Measurer1.MAXM])
Code04_Measurer1.to = jarray('int', [Code04_Measurer1.MAXM])
Code04_Measurer1.weight = jarray('double', [Code04_Measurer1.MAXM])
Code04_Measurer1.cnt = jcast('int', 0)
Code04_Measurer1.dist = jarray('double', [Code04_Measurer1.MAXN])
Code04_Measurer1.update = jarray('int', [Code04_Measurer1.MAXN])
Code04_Measurer1.MAXQ = jcast('int', 1000001)
Code04_Measurer1.queue = jarray('int', [Code04_Measurer1.MAXQ])
Code04_Measurer1.h = jcast('int', 0)
Code04_Measurer1.t = jcast('int', 0)
Code04_Measurer1.enter = jarray('boolean', [Code04_Measurer1.MAXN])

if __name__ == '__main__':
    Code04_Measurer1.main([])

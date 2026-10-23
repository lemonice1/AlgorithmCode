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

# 游戏，Python版
# 地面有x、a、b、c四种类型，赛车有A、B、C三辆
# 类型a不能跑车A，类型b不能跑车B、类型c不能跑车C，类型x没有限制
# 一共有n个地点，给定每个地点的地面类型，其中x类型的地面有d个
# 一共有m个限制，格式 pos1 car1 pos2 car2，含义如下
# 如果pos1号地点使用car1赛车，那么pos2号地点一定要使用car2赛车
# 每辆赛车可以使用无限次，需要满足以上的规则和限制来安排比赛
# 如果有方案，找到任意一种方案，打印每个地点用什么车，无方案打印-1
# 1 <= n <= 5 * 10^4    1 <= m <= 10^5    0 <= d <= 8
# 测试链接 : https://www.luogu.com.cn/problem/P3825
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Game1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'd': 'd', 'm': 'm', 'ban': 'ban', 'first': 'first', 'second': 'second', 'groundType': 'groundType', 'pos1': 'pos1', 'car1': 'car1', 'pos2': 'pos2', 'car2': 'car2', 'posx': 'posx', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'ans': 'ans', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    d = 0
    m = 0
    ban = None
    first = None
    second = None
    groundType = None
    pos1 = None
    car1 = None
    pos2 = None
    car2 = None
    posx = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    ans = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stau = None
    stas = None
    stae = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        Code04_Game1.stau[Code04_Game1.stacksize] = jcast('int', u)
        Code04_Game1.stas[Code04_Game1.stacksize] = jcast('int', status)
        Code04_Game1.stae[Code04_Game1.stacksize] = jcast('int', e)
        Code04_Game1.stacksize = jcast('int', (Code04_Game1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_Game1.stacksize = jcast('int', (Code04_Game1.stacksize - 1))
        Code04_Game1.u = jcast('int', Code04_Game1.stau[Code04_Game1.stacksize])
        Code04_Game1.status = jcast('int', Code04_Game1.stas[Code04_Game1.stacksize])
        Code04_Game1.e = jcast('int', Code04_Game1.stae[Code04_Game1.stacksize])

    @staticmethod
    def prepare():
        Code04_Game1.ban[jchar('a')] = jcast('char', jchar('A'))
        Code04_Game1.ban[jchar('b')] = jcast('char', jchar('B'))
        Code04_Game1.ban[jchar('c')] = jcast('char', jchar('C'))
        Code04_Game1.first[jchar('a')] = jcast('char', jchar('B'))
        Code04_Game1.first[jchar('b')] = jcast('char', jchar('A'))
        Code04_Game1.first[jchar('c')] = jcast('char', jchar('A'))
        Code04_Game1.second[jchar('a')] = jcast('char', jchar('C'))
        Code04_Game1.second[jchar('b')] = jcast('char', jchar('C'))
        Code04_Game1.second[jchar('c')] = jcast('char', jchar('B'))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Game1.nxt, ((_java_obj_1 := Code04_Game1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Game1.head[u])
        Code04_Game1.to[Code04_Game1.cntg] = jcast('int', v)
        Code04_Game1.head[u] = jcast('int', Code04_Game1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code04_Game1.dfn, u, jset(Code04_Game1.low, u, ((_java_obj_4 := Code04_Game1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_Game1.sta, ((_java_obj_7 := Code04_Game1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_Game1.head[u])
        while (e > 0):
            v = jcast('int', Code04_Game1.to[e])
            if (Code04_Game1.dfn[v] == 0):
                Code04_Game1.tarjan1(v)
                jset(Code04_Game1.low, u, jstatic('Math', 'min', Code04_Game1.low[u], Code04_Game1.low[v]))
            else:
                if (Code04_Game1.belong[v] == 0):
                    jset(Code04_Game1.low, u, jstatic('Math', 'min', Code04_Game1.low[u], Code04_Game1.dfn[v]))
            e = jcast('int', Code04_Game1.nxt[e])
        if (Code04_Game1.dfn[u] == Code04_Game1.low[u]):
            Code04_Game1.sccCnt = jcast('int', (Code04_Game1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code04_Game1.sta[((_java_obj_10 := Code04_Game1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code04_Game1.belong[pop] = jcast('int', Code04_Game1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code04_Game1.stacksize = jcast('int', 0)
        Code04_Game1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code04_Game1.stacksize > 0):
            Code04_Game1.pop()
            if (Code04_Game1.status == jcast('int', (-1))):
                jset(Code04_Game1.dfn, Code04_Game1.u, jset(Code04_Game1.low, Code04_Game1.u, ((_java_obj_13 := Code04_Game1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code04_Game1.sta, ((_java_obj_16 := Code04_Game1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code04_Game1.u)
                Code04_Game1.e = jcast('int', Code04_Game1.head[Code04_Game1.u])
            else:
                v = jcast('int', Code04_Game1.to[Code04_Game1.e])
                if (Code04_Game1.status == 0):
                    jset(Code04_Game1.low, Code04_Game1.u, jstatic('Math', 'min', Code04_Game1.low[Code04_Game1.u], Code04_Game1.low[v]))
                if ((Code04_Game1.status == 1) and (Code04_Game1.belong[v] == 0)):
                    jset(Code04_Game1.low, Code04_Game1.u, jstatic('Math', 'min', Code04_Game1.low[Code04_Game1.u], Code04_Game1.dfn[v]))
                Code04_Game1.e = jcast('int', Code04_Game1.nxt[Code04_Game1.e])
            if (Code04_Game1.e != 0):
                v = jcast('int', Code04_Game1.to[Code04_Game1.e])
                if (Code04_Game1.dfn[v] == 0):
                    Code04_Game1.push(Code04_Game1.u, 0, Code04_Game1.e)
                    Code04_Game1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code04_Game1.push(Code04_Game1.u, 1, Code04_Game1.e)
            else:
                if (Code04_Game1.dfn[Code04_Game1.u] == Code04_Game1.low[Code04_Game1.u]):
                    Code04_Game1.sccCnt = jcast('int', (Code04_Game1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code04_Game1.sta[((_java_obj_19 := Code04_Game1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code04_Game1.belong[pop] = jcast('int', Code04_Game1.sccCnt)
                        if not ((pop != Code04_Game1.u)):
                            break

    @staticmethod
    def other(i):
        i = jcast('int', i)
        return jcast('int', (jcast('int', jadd(i, Code04_Game1.n)) if (i <= Code04_Game1.n) else jcast('int', (i - Code04_Game1.n))))

    @staticmethod
    def buildGraph(stax):
        stax = jcast('int', stax)
        bit = jcast('int', 0)
        idx = jcast('int', 1)
        while (bit < Code04_Game1.d):
            if (jcast('int', (jcast('int', (stax >> (bit & 31))) & 1)) == 1):
                jset(Code04_Game1.groundType, Code04_Game1.posx[idx], jchar('a'))
            else:
                jset(Code04_Game1.groundType, Code04_Game1.posx[idx], jchar('b'))
            bit = jcast('int', (bit + 1))
            idx = jcast('int', (idx + 1))
        i = jcast('int', 1)
        while (i <= Code04_Game1.m):
            try:
                p1 = jcast('int', Code04_Game1.pos1[i])
                g1 = jcast('char', Code04_Game1.groundType[p1])
                c1 = jcast('char', Code04_Game1.car1[i])
                if (Code04_Game1.ban[g1] == c1):
                    raise JContinue(None)
                id1 = jcast('int', (p1 if (c1 == Code04_Game1.first[g1]) else jcast('int', jadd(p1, Code04_Game1.n))))
                p2 = jcast('int', Code04_Game1.pos2[i])
                g2 = jcast('char', Code04_Game1.groundType[p2])
                c2 = jcast('char', Code04_Game1.car2[i])
                if (Code04_Game1.ban[g2] == c2):
                    Code04_Game1.addEdge(id1, Code04_Game1.other(id1))
                else:
                    id2 = jcast('int', (p2 if (c2 == Code04_Game1.first[g2]) else jcast('int', jadd(p2, Code04_Game1.n))))
                    Code04_Game1.addEdge(id1, id2)
                    Code04_Game1.addEdge(Code04_Game1.other(id2), Code04_Game1.other(id1))
            except JContinue as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
            except JBreak as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= jcast('int', (Code04_Game1.n << (1 & 31)))):
            jset(Code04_Game1.head, i, jset(Code04_Game1.dfn, i, jset(Code04_Game1.belong, i, 0)))
            i = jcast('int', (i + 1))
        Code04_Game1.cntg = jcast('int', jset(Code04_Game1, 'cntd', jset(Code04_Game1, 'top', jset(Code04_Game1, 'sccCnt', 0))))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        sizx = jcast('int', 0)
        while (i <= Code04_Game1.n):
            if (Code04_Game1.groundType[i] == jchar('x')):
                jset(Code04_Game1.posx, (sizx := jcast('int', (sizx + (1)))), i)
            i = jcast('int', (i + 1))
        stax = jcast('int', 0)
        while (stax < jcast('int', (1 << (Code04_Game1.d & 31)))):
            try:
                Code04_Game1.buildGraph(stax)
                i = jcast('int', 1)
                while (i <= jcast('int', (Code04_Game1.n << (1 & 31)))):
                    if (Code04_Game1.dfn[i] == 0):
                        if (Code04_Game1.head[i] == 0):
                            # 孤立点直接分配强联通分量
                            # 减少常数开销，保持算法的渐进复杂度不变
                            jset(Code04_Game1.dfn, i, jset(Code04_Game1.low, i, ((_java_obj_24 := Code04_Game1), (_java_key_25 := 'cntd'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))))[3]))
                            jset(Code04_Game1.belong, i, ((_java_obj_27 := Code04_Game1), (_java_key_28 := 'sccCnt'), (_java_old_29 := jget(_java_obj_27, _java_key_28)), jset(_java_obj_27, _java_key_28, jcast('int', (_java_old_29 + (1)))))[3])
                        else:
                            # tarjan1(i);
                            Code04_Game1.tarjan2(i)
                    i = jcast('int', (i + 1))
                check = jcast('boolean', True)
                i = jcast('int', 1)
                while (i <= Code04_Game1.n):
                    try:
                        if (Code04_Game1.belong[i] == Code04_Game1.belong[jcast('int', jadd(i, Code04_Game1.n))]):
                            check = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_30:
                        if _java_control_30.label not in (None,):
                            raise
                    except JBreak as _java_control_30:
                        if _java_control_30.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                if check:
                    i = jcast('int', 1)
                    while (i <= Code04_Game1.n):
                        ground = jcast('char', Code04_Game1.groundType[i])
                        if (Code04_Game1.belong[i] < Code04_Game1.belong[jcast('int', jadd(i, Code04_Game1.n))]):
                            Code04_Game1.ans[i] = jcast('char', Code04_Game1.first[ground])
                        else:
                            Code04_Game1.ans[i] = jcast('char', Code04_Game1.second[ground])
                        i = jcast('int', (i + 1))
                    return jcast('boolean', True)
                Code04_Game1.clear()
            except JContinue as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
            except JBreak as _java_control_23:
                if _java_control_23.label not in (None,):
                    raise
                break
            stax = jcast('int', (stax + 1))
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        in_ = Code04_Game1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Game1.prepare()
        Code04_Game1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Game1.d = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Game1.n):
            jset(Code04_Game1.groundType, i, jcall(in_, 'nextChar'))
            i = jcast('int', (i + 1))
        Code04_Game1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Game1.m):
            jset(Code04_Game1.pos1, i, jcall(in_, 'nextInt'))
            jset(Code04_Game1.car1, i, jcall(in_, 'nextChar'))
            jset(Code04_Game1.pos2, i, jcall(in_, 'nextInt'))
            jset(Code04_Game1.car2, i, jcall(in_, 'nextChar'))
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code04_Game1.compute())
        if check:
            i = jcast('int', 1)
            while (i <= Code04_Game1.n):
                jcall(out, 'print', Code04_Game1.ans[i])
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', jcast('int', (-1)))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_31 := self), (_java_key_32 := 'ptr'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))), _java_old_33)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((not ((c > jchar(' ')) and (c != jcast('int', (-1)))))):
                    break
            return jcast('char', jcast('char', c))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_Game1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Game1.MAXN = jcast('int', 200001)
Code04_Game1.n = jcast('int', 0)
Code04_Game1.d = jcast('int', 0)
Code04_Game1.m = jcast('int', 0)
Code04_Game1.ban = jarray('char', [128])
Code04_Game1.first = jarray('char', [128])
Code04_Game1.second = jarray('char', [128])
Code04_Game1.groundType = jarray('char', [Code04_Game1.MAXN])
Code04_Game1.pos1 = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.car1 = jarray('char', [Code04_Game1.MAXN])
Code04_Game1.pos2 = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.car2 = jarray('char', [Code04_Game1.MAXN])
Code04_Game1.posx = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.head = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.nxt = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.to = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.cntg = jcast('int', 0)
Code04_Game1.dfn = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.low = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.cntd = jcast('int', 0)
Code04_Game1.sta = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.top = jcast('int', 0)
Code04_Game1.belong = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.sccCnt = jcast('int', 0)
Code04_Game1.ans = jarray('char', [Code04_Game1.MAXN])
Code04_Game1.stau = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.stas = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.stae = jarray('int', [Code04_Game1.MAXN])
Code04_Game1.u = jcast('int', 0)
Code04_Game1.status = jcast('int', 0)
Code04_Game1.e = jcast('int', 0)
Code04_Game1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code04_Game1.main([])

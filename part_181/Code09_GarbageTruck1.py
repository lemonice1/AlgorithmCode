# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 垃圾车，Python版
# 一共有n个点，m条无向边，所有点不保证连通
# 每条边的属性为 u v s t : u和v是端点，s是初始状态，t是最终状态
# 状态的数值只有0和1两种，当一辆车通过一条无向边，那么状态会翻转
# 一辆车的路线中，可以指定一个起点，最终回到起点，沿途的其他点不能重复经过
# 所有的边都要达成最终状态，所以需要若干辆车来完成这个目标
# 如果存在方案，提供任何一种方案即可，首先打印需要几辆车
# 然后对每辆车，先打印通过的边数，再打印依次到达了哪些点
# 如果不存在方案，打印"NIE"
# 1 <= n <= 10^5    1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P3520
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_GarbageTruck1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'eid': 'eid', 'cntg': 'cntg', 'deg': 'deg', 'cur': 'cur', 'visNode': 'visNode', 'visEdge': 'visEdge', 'inpath': 'inpath', 'path': 'path', 'cntp': 'cntp', 'ansArr': 'ansArr', 'ansl': 'ansl', 'ansr': 'ansr', 'idx': 'idx', 'cnta': 'cnta', 'sta': 'sta', 'top': 'top'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    eid = None
    cntg = 0
    deg = None
    cur = None
    # 区分多个连通区
    visNode = None
    # 标记无向边是否已经使用
    visEdge = None
    inpath = None
    path = None
    cntp = 0
    ansArr = None
    ansl = None
    ansr = None
    idx = 0
    cnta = 0
    @staticmethod
    def addEdge(u, v, id):
        u = jcast('int', u)
        v = jcast('int', v)
        id = jcast('int', id)
        jset(Code09_GarbageTruck1.nxt, ((_java_obj_1 := Code09_GarbageTruck1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code09_GarbageTruck1.head[u])
        Code09_GarbageTruck1.to[Code09_GarbageTruck1.cntg] = jcast('int', v)
        Code09_GarbageTruck1.eid[Code09_GarbageTruck1.cntg] = jcast('int', id)
        Code09_GarbageTruck1.head[u] = jcast('int', Code09_GarbageTruck1.cntg)

    @staticmethod
    def popCircle(u):
        u = jcast('int', u)
        Code09_GarbageTruck1.cnta = jcast('int', (Code09_GarbageTruck1.cnta + 1))
        jset(Code09_GarbageTruck1.ansArr, ((_java_obj_4 := Code09_GarbageTruck1), (_java_key_5 := 'idx'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        Code09_GarbageTruck1.ansl[Code09_GarbageTruck1.cnta] = jcast('int', Code09_GarbageTruck1.idx)
        pop = jcast('int', Code09_GarbageTruck1.path[((_java_obj_7 := Code09_GarbageTruck1), (_java_key_8 := 'cntp'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]])
        while (pop != u):
            Code09_GarbageTruck1.inpath[pop] = jcast('boolean', False)
            jset(Code09_GarbageTruck1.ansArr, ((_java_obj_10 := Code09_GarbageTruck1), (_java_key_11 := 'idx'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], pop)
            pop = jcast('int', Code09_GarbageTruck1.path[((_java_obj_13 := Code09_GarbageTruck1), (_java_key_14 := 'cntp'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
        Code09_GarbageTruck1.inpath[u] = jcast('boolean', False)
        jset(Code09_GarbageTruck1.ansArr, ((_java_obj_16 := Code09_GarbageTruck1), (_java_key_17 := 'idx'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], u)
        Code09_GarbageTruck1.ansr[Code09_GarbageTruck1.cnta] = jcast('int', Code09_GarbageTruck1.idx)

    @staticmethod
    def euler1(u):
        u = jcast('int', u)
        Code09_GarbageTruck1.visNode[u] = jcast('boolean', True)
        e = jcast('int', Code09_GarbageTruck1.cur[u])
        while (e > 0):
            Code09_GarbageTruck1.cur[u] = jcast('int', Code09_GarbageTruck1.nxt[e])
            if (not Code09_GarbageTruck1.visEdge[Code09_GarbageTruck1.eid[e]]):
                jset(Code09_GarbageTruck1.visEdge, Code09_GarbageTruck1.eid[e], True)
                Code09_GarbageTruck1.euler1(Code09_GarbageTruck1.to[e])
            e = jcast('int', Code09_GarbageTruck1.cur[u])
        if Code09_GarbageTruck1.inpath[u]:
            Code09_GarbageTruck1.popCircle(u)
        Code09_GarbageTruck1.inpath[u] = jcast('boolean', True)
        jset(Code09_GarbageTruck1.path, ((_java_obj_19 := Code09_GarbageTruck1), (_java_key_20 := 'cntp'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], u)

    sta = None
    top = 0
    @staticmethod
    def euler2(node):
        node = jcast('int', node)
        Code09_GarbageTruck1.top = jcast('int', 0)
        jset(Code09_GarbageTruck1.sta, ((_java_obj_22 := Code09_GarbageTruck1), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], node)
        while (Code09_GarbageTruck1.top > 0):
            u = jcast('int', Code09_GarbageTruck1.sta[((_java_obj_25 := Code09_GarbageTruck1), (_java_key_26 := 'top'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (-1)))), _java_old_27)[4]])
            Code09_GarbageTruck1.visNode[u] = jcast('boolean', True)
            e = jcast('int', Code09_GarbageTruck1.cur[u])
            if (e != 0):
                Code09_GarbageTruck1.cur[u] = jcast('int', Code09_GarbageTruck1.nxt[e])
                if (not Code09_GarbageTruck1.visEdge[Code09_GarbageTruck1.eid[e]]):
                    jset(Code09_GarbageTruck1.visEdge, Code09_GarbageTruck1.eid[e], True)
                    jset(Code09_GarbageTruck1.sta, ((_java_obj_28 := Code09_GarbageTruck1), (_java_key_29 := 'top'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3], u)
                    jset(Code09_GarbageTruck1.sta, ((_java_obj_31 := Code09_GarbageTruck1), (_java_key_32 := 'top'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3], Code09_GarbageTruck1.to[e])
                else:
                    jset(Code09_GarbageTruck1.sta, ((_java_obj_34 := Code09_GarbageTruck1), (_java_key_35 := 'top'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3], u)
            else:
                if Code09_GarbageTruck1.inpath[u]:
                    Code09_GarbageTruck1.popCircle(u)
                Code09_GarbageTruck1.inpath[u] = jcast('boolean', True)
                jset(Code09_GarbageTruck1.path, ((_java_obj_37 := Code09_GarbageTruck1), (_java_key_38 := 'cntp'), (_java_old_39 := jget(_java_obj_37, _java_key_38)), jset(_java_obj_37, _java_key_38, jcast('int', (_java_old_39 + (1)))))[3], u)

    @staticmethod
    def main(args):
        in_ = Code09_GarbageTruck1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_GarbageTruck1.n = jcast('int', jcall(in_, 'nextInt'))
        Code09_GarbageTruck1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        s = 0
        t = 0
        while (i <= Code09_GarbageTruck1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            s = jcast('int', jcall(in_, 'nextInt'))
            t = jcast('int', jcall(in_, 'nextInt'))
            if (s != t):
                Code09_GarbageTruck1.deg[u] = jcast('int', (Code09_GarbageTruck1.deg[u] + 1))
                Code09_GarbageTruck1.deg[v] = jcast('int', (Code09_GarbageTruck1.deg[v] + 1))
                Code09_GarbageTruck1.addEdge(u, v, i)
                Code09_GarbageTruck1.addEdge(v, u, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_GarbageTruck1.n):
            Code09_GarbageTruck1.cur[i] = jcast('int', Code09_GarbageTruck1.head[i])
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code09_GarbageTruck1.n):
            try:
                if (jcast('int', (Code09_GarbageTruck1.deg[i] & 1)) == 1):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_40:
                if _java_control_40.label not in (None,):
                    raise
            except JBreak as _java_control_40:
                if _java_control_40.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (not check):
            jcall(out, 'println', 'NIE')
        else:
            i = jcast('int', 1)
            while (i <= Code09_GarbageTruck1.n):
                if (not Code09_GarbageTruck1.visNode[i]):
                    # euler1(i);
                    Code09_GarbageTruck1.euler2(i)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code09_GarbageTruck1.cnta)
            i = jcast('int', 1)
            while (i <= Code09_GarbageTruck1.cnta):
                jcall(out, 'print', jadd(jcast('int', (Code09_GarbageTruck1.ansr[i] - Code09_GarbageTruck1.ansl[i])), ' '))
                j = jcast('int', Code09_GarbageTruck1.ansl[i])
                while (j <= Code09_GarbageTruck1.ansr[i]):
                    jcall(out, 'print', jadd(Code09_GarbageTruck1.ansArr[j], ' '))
                    j = jcast('int', (j + 1))
                jcall(out, 'println')
                i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_41 := self), (_java_key_42 := 'ptr'), (_java_old_43 := jget(_java_obj_41, _java_key_42)), jset(_java_obj_41, _java_key_42, jcast('int', (_java_old_43 + (1)))), _java_old_43)[4]])

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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code09_GarbageTruck1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_GarbageTruck1.MAXN = jcast('int', 100001)
Code09_GarbageTruck1.MAXM = jcast('int', 2000001)
Code09_GarbageTruck1.n = jcast('int', 0)
Code09_GarbageTruck1.m = jcast('int', 0)
Code09_GarbageTruck1.head = jarray('int', [Code09_GarbageTruck1.MAXN])
Code09_GarbageTruck1.nxt = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.to = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.eid = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.cntg = jcast('int', 0)
Code09_GarbageTruck1.deg = jarray('int', [Code09_GarbageTruck1.MAXN])
Code09_GarbageTruck1.cur = jarray('int', [Code09_GarbageTruck1.MAXN])
Code09_GarbageTruck1.visNode = jarray('boolean', [Code09_GarbageTruck1.MAXN])
Code09_GarbageTruck1.visEdge = jarray('boolean', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.inpath = jarray('boolean', [Code09_GarbageTruck1.MAXN])
Code09_GarbageTruck1.path = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.cntp = jcast('int', 0)
Code09_GarbageTruck1.ansArr = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.ansl = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.ansr = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.idx = jcast('int', 0)
Code09_GarbageTruck1.cnta = jcast('int', 0)
Code09_GarbageTruck1.sta = jarray('int', [Code09_GarbageTruck1.MAXM])
Code09_GarbageTruck1.top = jcast('int', 0)

if __name__ == '__main__':
    Code09_GarbageTruck1.main([])

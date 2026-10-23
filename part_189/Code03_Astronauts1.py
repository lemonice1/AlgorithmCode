# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 宇航员，Python版
# 一共n个人，一共A、B、C三个任务，所有人都能执行C任务，给定每人的年龄，假设平均年龄为f
# 年龄 >= f 的人可以执行A任务，年龄 < f 的人可以执行B任务
# 给定m个厌恶关系，格式 x y，代表编号x和编号y的两人相互讨厌
# 每个人必须选一个任务，相互讨厌的人不能分配相同任务，允许某个任务无人执行
# 如果存在分配任务的方案，打印每个人分配了什么任务，任何一种方案都可以
# 如果不存在方案，打印"No solution."
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/UVA1391
# 测试链接 : https://vjudge.net/problem/UVA-1391
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Astronauts1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'age': 'age', 'sumAge': 'sumAge', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    age = None
    sumAge = 0
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
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code03_Astronauts1.stack[Code03_Astronauts1.stacksize], 0, u)
        jset(Code03_Astronauts1.stack[Code03_Astronauts1.stacksize], 1, status)
        jset(Code03_Astronauts1.stack[Code03_Astronauts1.stacksize], 2, e)
        Code03_Astronauts1.stacksize = jcast('int', (Code03_Astronauts1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Astronauts1.stacksize = jcast('int', (Code03_Astronauts1.stacksize - 1))
        Code03_Astronauts1.u = jcast('int', Code03_Astronauts1.stack[Code03_Astronauts1.stacksize][0])
        Code03_Astronauts1.status = jcast('int', Code03_Astronauts1.stack[Code03_Astronauts1.stacksize][1])
        Code03_Astronauts1.e = jcast('int', Code03_Astronauts1.stack[Code03_Astronauts1.stacksize][2])

    @staticmethod
    def prepare():
        Code03_Astronauts1.sumAge = jcast('int', jset(Code03_Astronauts1, 'cntg', jset(Code03_Astronauts1, 'cntd', jset(Code03_Astronauts1, 'sccCnt', 0))))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code03_Astronauts1.n << (1 & 31)))):
            jset(Code03_Astronauts1.head, i, jset(Code03_Astronauts1.dfn, i, jset(Code03_Astronauts1.low, i, jset(Code03_Astronauts1.belong, i, 0))))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_Astronauts1.nxt, ((_java_obj_1 := Code03_Astronauts1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Astronauts1.head[u])
        Code03_Astronauts1.to[Code03_Astronauts1.cntg] = jcast('int', v)
        Code03_Astronauts1.head[u] = jcast('int', Code03_Astronauts1.cntg)

    @staticmethod
    def older(x):
        x = jcast('int', x)
        return jcast('boolean', (jcast('int', (Code03_Astronauts1.age[x] * Code03_Astronauts1.n)) >= Code03_Astronauts1.sumAge))

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code03_Astronauts1.dfn, u, jset(Code03_Astronauts1.low, u, ((_java_obj_4 := Code03_Astronauts1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code03_Astronauts1.sta, ((_java_obj_7 := Code03_Astronauts1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code03_Astronauts1.head[u])
        while (e > 0):
            v = jcast('int', Code03_Astronauts1.to[e])
            if (Code03_Astronauts1.dfn[v] == 0):
                Code03_Astronauts1.tarjan1(v)
                jset(Code03_Astronauts1.low, u, jstatic('Math', 'min', Code03_Astronauts1.low[u], Code03_Astronauts1.low[v]))
            else:
                if (Code03_Astronauts1.belong[v] == 0):
                    jset(Code03_Astronauts1.low, u, jstatic('Math', 'min', Code03_Astronauts1.low[u], Code03_Astronauts1.dfn[v]))
            e = jcast('int', Code03_Astronauts1.nxt[e])
        if (Code03_Astronauts1.dfn[u] == Code03_Astronauts1.low[u]):
            Code03_Astronauts1.sccCnt = jcast('int', (Code03_Astronauts1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code03_Astronauts1.sta[((_java_obj_10 := Code03_Astronauts1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code03_Astronauts1.belong[pop] = jcast('int', Code03_Astronauts1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code03_Astronauts1.stacksize = jcast('int', 0)
        Code03_Astronauts1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_Astronauts1.stacksize > 0):
            Code03_Astronauts1.pop()
            if (Code03_Astronauts1.status == jcast('int', (-1))):
                jset(Code03_Astronauts1.dfn, Code03_Astronauts1.u, jset(Code03_Astronauts1.low, Code03_Astronauts1.u, ((_java_obj_13 := Code03_Astronauts1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code03_Astronauts1.sta, ((_java_obj_16 := Code03_Astronauts1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code03_Astronauts1.u)
                Code03_Astronauts1.e = jcast('int', Code03_Astronauts1.head[Code03_Astronauts1.u])
            else:
                v = jcast('int', Code03_Astronauts1.to[Code03_Astronauts1.e])
                if (Code03_Astronauts1.status == 0):
                    jset(Code03_Astronauts1.low, Code03_Astronauts1.u, jstatic('Math', 'min', Code03_Astronauts1.low[Code03_Astronauts1.u], Code03_Astronauts1.low[v]))
                if ((Code03_Astronauts1.status == 1) and (Code03_Astronauts1.belong[v] == 0)):
                    jset(Code03_Astronauts1.low, Code03_Astronauts1.u, jstatic('Math', 'min', Code03_Astronauts1.low[Code03_Astronauts1.u], Code03_Astronauts1.dfn[v]))
                Code03_Astronauts1.e = jcast('int', Code03_Astronauts1.nxt[Code03_Astronauts1.e])
            if (Code03_Astronauts1.e != 0):
                v = jcast('int', Code03_Astronauts1.to[Code03_Astronauts1.e])
                if (Code03_Astronauts1.dfn[v] == 0):
                    Code03_Astronauts1.push(Code03_Astronauts1.u, 0, Code03_Astronauts1.e)
                    Code03_Astronauts1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_Astronauts1.push(Code03_Astronauts1.u, 1, Code03_Astronauts1.e)
            else:
                if (Code03_Astronauts1.dfn[Code03_Astronauts1.u] == Code03_Astronauts1.low[Code03_Astronauts1.u]):
                    Code03_Astronauts1.sccCnt = jcast('int', (Code03_Astronauts1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code03_Astronauts1.sta[((_java_obj_19 := Code03_Astronauts1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code03_Astronauts1.belong[pop] = jcast('int', Code03_Astronauts1.sccCnt)
                        if not ((pop != Code03_Astronauts1.u)):
                            break

    @staticmethod
    def main(args):
        in_ = Code03_Astronauts1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Astronauts1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Astronauts1.m = jcast('int', jcall(in_, 'nextInt'))
        while ((Code03_Astronauts1.n != 0) and (Code03_Astronauts1.m != 0)):
            try:
                Code03_Astronauts1.prepare()
                i = jcast('int', 1)
                while (i <= Code03_Astronauts1.n):
                    jset(Code03_Astronauts1.age, i, jcall(in_, 'nextInt'))
                    Code03_Astronauts1.sumAge = jcast('int', jcast('int', jadd(Code03_Astronauts1.sumAge, Code03_Astronauts1.age[i])))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                x = 0
                y = 0
                while (i <= Code03_Astronauts1.m):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    Code03_Astronauts1.addEdge(jcast('int', jadd(x, Code03_Astronauts1.n)), y)
                    Code03_Astronauts1.addEdge(jcast('int', jadd(y, Code03_Astronauts1.n)), x)
                    if (Code03_Astronauts1.older(x) == Code03_Astronauts1.older(y)):
                        Code03_Astronauts1.addEdge(x, jcast('int', jadd(y, Code03_Astronauts1.n)))
                        Code03_Astronauts1.addEdge(y, jcast('int', jadd(x, Code03_Astronauts1.n)))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= jcast('int', (Code03_Astronauts1.n << (1 & 31)))):
                    if (Code03_Astronauts1.dfn[i] == 0):
                        # tarjan1(i);
                        Code03_Astronauts1.tarjan2(i)
                    i = jcast('int', (i + 1))
                check = jcast('boolean', True)
                i = jcast('int', 1)
                while (i <= Code03_Astronauts1.n):
                    try:
                        if (Code03_Astronauts1.belong[i] == Code03_Astronauts1.belong[jcast('int', jadd(i, Code03_Astronauts1.n))]):
                            check = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_23:
                        if _java_control_23.label not in (None,):
                            raise
                    except JBreak as _java_control_23:
                        if _java_control_23.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                if check:
                    i = jcast('int', 1)
                    while (i <= Code03_Astronauts1.n):
                        if (Code03_Astronauts1.belong[i] < Code03_Astronauts1.belong[jcast('int', jadd(i, Code03_Astronauts1.n))]):
                            if Code03_Astronauts1.older(i):
                                jcall(out, 'println', 'A')
                            else:
                                jcall(out, 'println', 'B')
                        else:
                            jcall(out, 'println', 'C')
                        i = jcast('int', (i + 1))
                else:
                    jcall(out, 'println', 'No solution.')
                Code03_Astronauts1.n = jcast('int', jcall(in_, 'nextInt'))
                Code03_Astronauts1.m = jcast('int', jcall(in_, 'nextInt'))
            except JContinue as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
            except JBreak as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
                break
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
            return jcast('int', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

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
            raise TypeError("No matching overload for Code03_Astronauts1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Astronauts1.MAXN = jcast('int', 200001)
Code03_Astronauts1.MAXM = jcast('int', 500001)
Code03_Astronauts1.n = jcast('int', 0)
Code03_Astronauts1.m = jcast('int', 0)
Code03_Astronauts1.age = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.sumAge = jcast('int', 0)
Code03_Astronauts1.head = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.nxt = jarray('int', [Code03_Astronauts1.MAXM])
Code03_Astronauts1.to = jarray('int', [Code03_Astronauts1.MAXM])
Code03_Astronauts1.cntg = jcast('int', 0)
Code03_Astronauts1.dfn = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.low = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.cntd = jcast('int', 0)
Code03_Astronauts1.sta = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.top = jcast('int', 0)
Code03_Astronauts1.belong = jarray('int', [Code03_Astronauts1.MAXN])
Code03_Astronauts1.sccCnt = jcast('int', 0)
Code03_Astronauts1.stack = jarray('int', [Code03_Astronauts1.MAXN, 3])
Code03_Astronauts1.u = jcast('int', 0)
Code03_Astronauts1.status = jcast('int', 0)
Code03_Astronauts1.e = jcast('int', 0)
Code03_Astronauts1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_Astronauts1.main([])

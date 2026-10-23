# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 杀人游戏，Python版
# 一共n个人，只有一个杀手，每个人是杀手的概率均等，其他人都是平民
# 给定m个知晓关系，如果x知晓y，那么y是不是杀手，x就知道情况了
# 知晓关系是单向且可传递的，比如a知晓b，b知晓c，那么a知晓c
# 你可以盘问任何人，不仅能知道对方身份，并且对方知晓的所有情况都能获得
# 但是如果你直接盘问到杀手的话，杀手会原地爆炸，炸死所有人
# 你一定要确定所有人的身份，而且你充分了解知晓关系网，会用最优的盘问策略
# 返回最优盘问策略下，杀手不爆炸还能被揪出来的概率，保留小数点后面6位
# 1 <= n <= 10^5
# 0 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4819
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_KillingGame2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccSiz': 'sccSiz', 'sccCnt': 'sccCnt', 'edgeArr': 'edgeArr', 'cnte': 'cnte', 'indegree': 'indegree', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    a = None
    b = None
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
    sccSiz = None
    sccCnt = 0
    edgeArr = None
    cnte = 0
    indegree = None
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
        jset(Code09_KillingGame2.stack[Code09_KillingGame2.stacksize], 0, u)
        jset(Code09_KillingGame2.stack[Code09_KillingGame2.stacksize], 1, status)
        jset(Code09_KillingGame2.stack[Code09_KillingGame2.stacksize], 2, e)
        Code09_KillingGame2.stacksize = jcast('int', (Code09_KillingGame2.stacksize + 1))

    @staticmethod
    def pop():
        Code09_KillingGame2.stacksize = jcast('int', (Code09_KillingGame2.stacksize - 1))
        Code09_KillingGame2.u = jcast('int', Code09_KillingGame2.stack[Code09_KillingGame2.stacksize][0])
        Code09_KillingGame2.status = jcast('int', Code09_KillingGame2.stack[Code09_KillingGame2.stacksize][1])
        Code09_KillingGame2.e = jcast('int', Code09_KillingGame2.stack[Code09_KillingGame2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code09_KillingGame2.nxt, ((_java_obj_1 := Code09_KillingGame2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code09_KillingGame2.head[u])
        Code09_KillingGame2.to[Code09_KillingGame2.cntg] = jcast('int', v)
        Code09_KillingGame2.head[u] = jcast('int', Code09_KillingGame2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code09_KillingGame2.dfn, u, jset(Code09_KillingGame2.low, u, ((_java_obj_4 := Code09_KillingGame2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code09_KillingGame2.sta, ((_java_obj_7 := Code09_KillingGame2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code09_KillingGame2.head[u])
        while (e > 0):
            v = jcast('int', Code09_KillingGame2.to[e])
            if (Code09_KillingGame2.dfn[v] == 0):
                Code09_KillingGame2.tarjan1(v)
                jset(Code09_KillingGame2.low, u, jstatic('Math', 'min', Code09_KillingGame2.low[u], Code09_KillingGame2.low[v]))
            else:
                if (Code09_KillingGame2.belong[v] == 0):
                    jset(Code09_KillingGame2.low, u, jstatic('Math', 'min', Code09_KillingGame2.low[u], Code09_KillingGame2.dfn[v]))
            e = jcast('int', Code09_KillingGame2.nxt[e])
        if (Code09_KillingGame2.dfn[u] == Code09_KillingGame2.low[u]):
            Code09_KillingGame2.sccCnt = jcast('int', (Code09_KillingGame2.sccCnt + 1))
            Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] = jcast('int', 0)
            pop = 0
            while True:
                pop = jcast('int', Code09_KillingGame2.sta[((_java_obj_10 := Code09_KillingGame2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code09_KillingGame2.belong[pop] = jcast('int', Code09_KillingGame2.sccCnt)
                Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] = jcast('int', (Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] + 1))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code09_KillingGame2.stacksize = jcast('int', 0)
        Code09_KillingGame2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code09_KillingGame2.stacksize > 0):
            Code09_KillingGame2.pop()
            if (Code09_KillingGame2.status == jcast('int', (-1))):
                jset(Code09_KillingGame2.dfn, Code09_KillingGame2.u, jset(Code09_KillingGame2.low, Code09_KillingGame2.u, ((_java_obj_13 := Code09_KillingGame2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code09_KillingGame2.sta, ((_java_obj_16 := Code09_KillingGame2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code09_KillingGame2.u)
                Code09_KillingGame2.e = jcast('int', Code09_KillingGame2.head[Code09_KillingGame2.u])
            else:
                v = jcast('int', Code09_KillingGame2.to[Code09_KillingGame2.e])
                if (Code09_KillingGame2.status == 0):
                    jset(Code09_KillingGame2.low, Code09_KillingGame2.u, jstatic('Math', 'min', Code09_KillingGame2.low[Code09_KillingGame2.u], Code09_KillingGame2.low[v]))
                if ((Code09_KillingGame2.status == 1) and (Code09_KillingGame2.belong[v] == 0)):
                    jset(Code09_KillingGame2.low, Code09_KillingGame2.u, jstatic('Math', 'min', Code09_KillingGame2.low[Code09_KillingGame2.u], Code09_KillingGame2.dfn[v]))
                Code09_KillingGame2.e = jcast('int', Code09_KillingGame2.nxt[Code09_KillingGame2.e])
            if (Code09_KillingGame2.e != 0):
                v = jcast('int', Code09_KillingGame2.to[Code09_KillingGame2.e])
                if (Code09_KillingGame2.dfn[v] == 0):
                    Code09_KillingGame2.push(Code09_KillingGame2.u, 0, Code09_KillingGame2.e)
                    Code09_KillingGame2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code09_KillingGame2.push(Code09_KillingGame2.u, 1, Code09_KillingGame2.e)
            else:
                if (Code09_KillingGame2.dfn[Code09_KillingGame2.u] == Code09_KillingGame2.low[Code09_KillingGame2.u]):
                    Code09_KillingGame2.sccCnt = jcast('int', (Code09_KillingGame2.sccCnt + 1))
                    Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] = jcast('int', 0)
                    pop = 0
                    while True:
                        pop = jcast('int', Code09_KillingGame2.sta[((_java_obj_19 := Code09_KillingGame2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code09_KillingGame2.belong[pop] = jcast('int', Code09_KillingGame2.sccCnt)
                        Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] = jcast('int', (Code09_KillingGame2.sccSiz[Code09_KillingGame2.sccCnt] + 1))
                        if not ((pop != Code09_KillingGame2.u)):
                            break

    @staticmethod
    def condense():
        Code09_KillingGame2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.sccCnt):
            Code09_KillingGame2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.m):
            scc1 = jcast('int', Code09_KillingGame2.belong[Code09_KillingGame2.a[i]])
            scc2 = jcast('int', Code09_KillingGame2.belong[Code09_KillingGame2.b[i]])
            if (scc1 != scc2):
                jset(Code09_KillingGame2.edgeArr, ((_java_obj_22 := Code09_KillingGame2), (_java_key_23 := 'cnte'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], jcast('long', (jcast('long', (jcast('long', scc1) << (32 & 63))) | scc2)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code09_KillingGame2.edgeArr, 1, jcast('int', jadd(Code09_KillingGame2.cnte, 1)))
        pre = jcast('long', 0)
        cur = 0
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.cnte):
            cur = jcast('long', Code09_KillingGame2.edgeArr[i])
            if (cur != pre):
                scc1 = jcast('int', jcast('int', jcast('long', jushr(cur, 32, 64))))
                scc2 = jcast('int', jcast('int', jcast('long', (cur & 4294967295))))
                Code09_KillingGame2.indegree[scc2] = jcast('int', (Code09_KillingGame2.indegree[scc2] + 1))
                Code09_KillingGame2.addEdge(scc1, scc2)
                pre = jcast('long', cur)
            i = jcast('int', (i + 1))

    @staticmethod
    def isolated(i):
        i = jcast('int', i)
        if ((Code09_KillingGame2.indegree[i] > 0) or (Code09_KillingGame2.sccSiz[i] > 1)):
            return jcast('boolean', False)
        if (Code09_KillingGame2.head[i] == 0):
            return jcast('boolean', True)
        e = jcast('int', Code09_KillingGame2.head[i])
        while (e > 0):
            v = jcast('int', Code09_KillingGame2.to[e])
            if (Code09_KillingGame2.indegree[v] == 1):
                return jcast('boolean', False)
            e = jcast('int', Code09_KillingGame2.nxt[e])
        return jcast('boolean', True)

    @staticmethod
    def compute():
        inZero = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.sccCnt):
            if (Code09_KillingGame2.indegree[i] == 0):
                inZero = jcast('int', (inZero + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.sccCnt):
            try:
                if Code09_KillingGame2.isolated(i):
                    inZero = jcast('int', (inZero - 1))
                    raise JBreak(None)
            except JContinue as _java_control_25:
                if _java_control_25.label not in (None,):
                    raise
            except JBreak as _java_control_25:
                if _java_control_25.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('double', (1.0 - jdiv(jcast('double', inZero), Code09_KillingGame2.n)))

    @staticmethod
    def main(args):
        in_ = Code09_KillingGame2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_KillingGame2.n = jcast('int', jcall(in_, 'nextInt'))
        Code09_KillingGame2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.m):
            jset(Code09_KillingGame2.a, i, jcall(in_, 'nextInt'))
            jset(Code09_KillingGame2.b, i, jcall(in_, 'nextInt'))
            Code09_KillingGame2.addEdge(Code09_KillingGame2.a[i], Code09_KillingGame2.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_KillingGame2.n):
            if (Code09_KillingGame2.dfn[i] == 0):
                # tarjan1(i);
                Code09_KillingGame2.tarjan2(i)
            i = jcast('int', (i + 1))
        Code09_KillingGame2.condense()
        ans = jcast('double', Code09_KillingGame2.compute())
        jcall(out, 'printf', '%.6f\n', ans)
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
            return jcast('int', self.buffer[((_java_obj_26 := self), (_java_key_27 := 'ptr'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))), _java_old_28)[4]])

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
            raise TypeError("No matching overload for Code09_KillingGame2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_KillingGame2.MAXN = jcast('int', 100001)
Code09_KillingGame2.MAXM = jcast('int', 300001)
Code09_KillingGame2.n = jcast('int', 0)
Code09_KillingGame2.m = jcast('int', 0)
Code09_KillingGame2.a = jarray('int', [Code09_KillingGame2.MAXM])
Code09_KillingGame2.b = jarray('int', [Code09_KillingGame2.MAXM])
Code09_KillingGame2.head = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.nxt = jarray('int', [Code09_KillingGame2.MAXM])
Code09_KillingGame2.to = jarray('int', [Code09_KillingGame2.MAXM])
Code09_KillingGame2.cntg = jcast('int', 0)
Code09_KillingGame2.dfn = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.low = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.cntd = jcast('int', 0)
Code09_KillingGame2.sta = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.top = jcast('int', 0)
Code09_KillingGame2.belong = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.sccSiz = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.sccCnt = jcast('int', 0)
Code09_KillingGame2.edgeArr = jarray('long', [Code09_KillingGame2.MAXM])
Code09_KillingGame2.cnte = jcast('int', 0)
Code09_KillingGame2.indegree = jarray('int', [Code09_KillingGame2.MAXN])
Code09_KillingGame2.stack = jarray('int', [Code09_KillingGame2.MAXN, 3])
Code09_KillingGame2.u = jcast('int', 0)
Code09_KillingGame2.status = jcast('int', 0)
Code09_KillingGame2.e = jcast('int', 0)
Code09_KillingGame2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code09_KillingGame2.main([])

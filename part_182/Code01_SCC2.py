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

# 强连通分量模版题1，Python版
# 给定一张n个点，m条边的有向图
# 求出所有强连通分量，先打印强连通分量的数量
# 然后打印1号点所在的强连通分量，然后打印2号点所在的强连通分量，以此类推
# 如果当前节点属于之前的强连通分量，那就跳过，直到打印所有强连通分量
# 打印每个强连通分量时，按照节点编号从小到大打印
# 1 <= n <= 10^4
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/B3609
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SCC2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccArr': 'sccArr', 'sccl': 'sccl', 'sccr': 'sccr', 'idx': 'idx', 'sccCnt': 'sccCnt', 'sccPrint': 'sccPrint', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
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
    sccArr = None
    sccl = None
    sccr = None
    idx = 0
    sccCnt = 0
    sccPrint = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_SCC2.nxt, ((_java_obj_1 := Code01_SCC2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_SCC2.head[u])
        Code01_SCC2.to[Code01_SCC2.cntg] = jcast('int', v)
        Code01_SCC2.head[u] = jcast('int', Code01_SCC2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code01_SCC2.dfn, u, jset(Code01_SCC2.low, u, ((_java_obj_4 := Code01_SCC2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_SCC2.sta, ((_java_obj_7 := Code01_SCC2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_SCC2.head[u])
        while (e > 0):
            v = jcast('int', Code01_SCC2.to[e])
            # 树边
            if (Code01_SCC2.dfn[v] == 0):
                Code01_SCC2.tarjan1(v)
                jset(Code01_SCC2.low, u, jstatic('Math', 'min', Code01_SCC2.low[u], Code01_SCC2.low[v]))
            else:
                # 回边
                if (Code01_SCC2.belong[v] == 0):
                    jset(Code01_SCC2.low, u, jstatic('Math', 'min', Code01_SCC2.low[u], Code01_SCC2.dfn[v]))
                # 如果 belong[v] != 0 就是遇到了弃边，什么也不做
            e = jcast('int', Code01_SCC2.nxt[e])
        if (Code01_SCC2.dfn[u] == Code01_SCC2.low[u]):
            Code01_SCC2.sccCnt = jcast('int', (Code01_SCC2.sccCnt + 1))
            Code01_SCC2.sccl[Code01_SCC2.sccCnt] = jcast('int', jcast('int', jadd(Code01_SCC2.idx, 1)))
            pop = 0
            while True:
                pop = jcast('int', Code01_SCC2.sta[((_java_obj_10 := Code01_SCC2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code01_SCC2.belong[pop] = jcast('int', Code01_SCC2.sccCnt)
                jset(Code01_SCC2.sccArr, ((_java_obj_13 := Code01_SCC2), (_java_key_14 := 'idx'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], pop)
                if not ((pop != u)):
                    break
            Code01_SCC2.sccr[Code01_SCC2.sccCnt] = jcast('int', Code01_SCC2.idx)

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
        jset(Code01_SCC2.stack[Code01_SCC2.stacksize], 0, u)
        jset(Code01_SCC2.stack[Code01_SCC2.stacksize], 1, status)
        jset(Code01_SCC2.stack[Code01_SCC2.stacksize], 2, e)
        Code01_SCC2.stacksize = jcast('int', (Code01_SCC2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_SCC2.stacksize = jcast('int', (Code01_SCC2.stacksize - 1))
        Code01_SCC2.u = jcast('int', Code01_SCC2.stack[Code01_SCC2.stacksize][0])
        Code01_SCC2.status = jcast('int', Code01_SCC2.stack[Code01_SCC2.stacksize][1])
        Code01_SCC2.e = jcast('int', Code01_SCC2.stack[Code01_SCC2.stacksize][2])

    # 迭代版
    # u表示当前节点
    # e表示u当前处理的边，如果e == 0，说明所有边都处理完了
    # status的具体说明如下
    # 如果status == -1，表示u没有遍历过任何儿子
    # 如果status == 0，表示u遍历到儿子v，然后发现dfn[v] == 0
    # 并且执行完了tarjan(v)，对应递归版for循环中的第一个分支
    # 如果status == 1，表示u遍历到儿子v，然后发现dfn[v] != 0
    # 对应递归版for循环中的第二个分支
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code01_SCC2.stacksize = jcast('int', 0)
        Code01_SCC2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code01_SCC2.stacksize > 0):
            Code01_SCC2.pop()
            if (Code01_SCC2.status == jcast('int', (-1))):
                jset(Code01_SCC2.dfn, Code01_SCC2.u, jset(Code01_SCC2.low, Code01_SCC2.u, ((_java_obj_16 := Code01_SCC2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code01_SCC2.sta, ((_java_obj_19 := Code01_SCC2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code01_SCC2.u)
                Code01_SCC2.e = jcast('int', Code01_SCC2.head[Code01_SCC2.u])
            else:
                v = jcast('int', Code01_SCC2.to[Code01_SCC2.e])
                if (Code01_SCC2.status == 0):
                    jset(Code01_SCC2.low, Code01_SCC2.u, jstatic('Math', 'min', Code01_SCC2.low[Code01_SCC2.u], Code01_SCC2.low[v]))
                if ((Code01_SCC2.status == 1) and (Code01_SCC2.belong[v] == 0)):
                    jset(Code01_SCC2.low, Code01_SCC2.u, jstatic('Math', 'min', Code01_SCC2.low[Code01_SCC2.u], Code01_SCC2.dfn[v]))
                Code01_SCC2.e = jcast('int', Code01_SCC2.nxt[Code01_SCC2.e])
            if (Code01_SCC2.e != 0):
                v = jcast('int', Code01_SCC2.to[Code01_SCC2.e])
                if (Code01_SCC2.dfn[v] == 0):
                    # (当前节点, 状态, 边)先进入栈
                    # (儿子节点, 状态, 边)再进入栈
                    # 那么儿子节点的tarjan过程会先执行
                    # 等到处理当前节点时，low[儿子节点]信息就生成好了
                    Code01_SCC2.push(Code01_SCC2.u, 0, Code01_SCC2.e)
                    Code01_SCC2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code01_SCC2.push(Code01_SCC2.u, 1, Code01_SCC2.e)
            else:
                if (Code01_SCC2.dfn[Code01_SCC2.u] == Code01_SCC2.low[Code01_SCC2.u]):
                    Code01_SCC2.sccCnt = jcast('int', (Code01_SCC2.sccCnt + 1))
                    Code01_SCC2.sccl[Code01_SCC2.sccCnt] = jcast('int', jcast('int', jadd(Code01_SCC2.idx, 1)))
                    pop = 0
                    while True:
                        pop = jcast('int', Code01_SCC2.sta[((_java_obj_22 := Code01_SCC2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                        Code01_SCC2.belong[pop] = jcast('int', Code01_SCC2.sccCnt)
                        jset(Code01_SCC2.sccArr, ((_java_obj_25 := Code01_SCC2), (_java_key_26 := 'idx'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], pop)
                        if not ((pop != Code01_SCC2.u)):
                            break
                    Code01_SCC2.sccr[Code01_SCC2.sccCnt] = jcast('int', Code01_SCC2.idx)

    @staticmethod
    def main(args):
        in_ = Code01_SCC2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_SCC2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_SCC2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code01_SCC2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_SCC2.addEdge(u, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_SCC2.n):
            if (Code01_SCC2.dfn[i] == 0):
                # tarjan1(i);
                Code01_SCC2.tarjan2(i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_SCC2.sccCnt)
        i = jcast('int', 1)
        while (i <= Code01_SCC2.sccCnt):
            jstatic('Arrays', 'sort', Code01_SCC2.sccArr, Code01_SCC2.sccl[i], jcast('int', jadd(Code01_SCC2.sccr[i], 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_SCC2.n):
            scc = jcast('int', Code01_SCC2.belong[i])
            if (not Code01_SCC2.sccPrint[scc]):
                Code01_SCC2.sccPrint[scc] = jcast('boolean', True)
                j = jcast('int', Code01_SCC2.sccl[scc])
                while (j <= Code01_SCC2.sccr[scc]):
                    jcall(out, 'print', jadd(Code01_SCC2.sccArr[j], ' '))
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
            return jcast('int', self.buffer[((_java_obj_28 := self), (_java_key_29 := 'ptr'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]])

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
            raise TypeError("No matching overload for Code01_SCC2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SCC2.MAXN = jcast('int', 10001)
Code01_SCC2.MAXM = jcast('int', 100001)
Code01_SCC2.n = jcast('int', 0)
Code01_SCC2.m = jcast('int', 0)
Code01_SCC2.head = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.nxt = jarray('int', [Code01_SCC2.MAXM])
Code01_SCC2.to = jarray('int', [Code01_SCC2.MAXM])
Code01_SCC2.cntg = jcast('int', 0)
Code01_SCC2.dfn = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.low = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.cntd = jcast('int', 0)
Code01_SCC2.sta = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.top = jcast('int', 0)
Code01_SCC2.belong = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.sccArr = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.sccl = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.sccr = jarray('int', [Code01_SCC2.MAXN])
Code01_SCC2.idx = jcast('int', 0)
Code01_SCC2.sccCnt = jcast('int', 0)
Code01_SCC2.sccPrint = jarray('boolean', [Code01_SCC2.MAXN])
Code01_SCC2.stack = jarray('int', [Code01_SCC2.MAXN, 3])
Code01_SCC2.u = jcast('int', 0)
Code01_SCC2.status = jcast('int', 0)
Code01_SCC2.e = jcast('int', 0)
Code01_SCC2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_SCC2.main([])

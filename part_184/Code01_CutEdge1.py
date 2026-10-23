# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 割边模版题1，Python版
# 给定一张无向图，一共n个点、m条边
# 图中可能存在多个连通区，对每个连通区求割边
# 先打印割边的总数量，然后从小到大打印所有割边的序号
# 请保证原图即使有重边和自环，答案依然正确
# 1 <= n <= 5 * 10^5
# 1 <= m <= 2 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/U582665
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CutEdge1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'cutEdge': 'cutEdge', 'stack': 'stack', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    cutEdge = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code01_CutEdge1.stack[Code01_CutEdge1.stacksize], 0, u)
        jset(Code01_CutEdge1.stack[Code01_CutEdge1.stacksize], 1, preEdge)
        jset(Code01_CutEdge1.stack[Code01_CutEdge1.stacksize], 2, status)
        jset(Code01_CutEdge1.stack[Code01_CutEdge1.stacksize], 3, e)
        Code01_CutEdge1.stacksize = jcast('int', (Code01_CutEdge1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_CutEdge1.stacksize = jcast('int', (Code01_CutEdge1.stacksize - 1))
        Code01_CutEdge1.u = jcast('int', Code01_CutEdge1.stack[Code01_CutEdge1.stacksize][0])
        Code01_CutEdge1.preEdge = jcast('int', Code01_CutEdge1.stack[Code01_CutEdge1.stacksize][1])
        Code01_CutEdge1.status = jcast('int', Code01_CutEdge1.stack[Code01_CutEdge1.stacksize][2])
        Code01_CutEdge1.e = jcast('int', Code01_CutEdge1.stack[Code01_CutEdge1.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_CutEdge1.nxt, ((_java_obj_1 := Code01_CutEdge1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_CutEdge1.head[u])
        Code01_CutEdge1.to[Code01_CutEdge1.cntg] = jcast('int', v)
        Code01_CutEdge1.head[u] = jcast('int', Code01_CutEdge1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code01_CutEdge1.dfn, u, jset(Code01_CutEdge1.low, u, ((_java_obj_4 := Code01_CutEdge1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        e = jcast('int', Code01_CutEdge1.head[u])
        while (e > 0):
            try:
                # 从哪条边来的要忽略
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code01_CutEdge1.to[e])
                # 树边
                if (Code01_CutEdge1.dfn[v] == 0):
                    Code01_CutEdge1.tarjan1(v, e)
                    jset(Code01_CutEdge1.low, u, jstatic('Math', 'min', Code01_CutEdge1.low[u], Code01_CutEdge1.low[v]))
                    if (Code01_CutEdge1.low[v] > Code01_CutEdge1.dfn[u]):
                        Code01_CutEdge1.cutEdge[jcast('int', (e >> (1 & 31)))] = jcast('boolean', True)
                    # 回边或弃边
                else:
                    # 回边是dfn[v] < dfn[u]，弃边是dfn[v] > dfn[u]
                    # 因为low[u]初始值就是dfn[u]，所以弃边出现时，无法更新low[u]
                    jset(Code01_CutEdge1.low, u, jstatic('Math', 'min', Code01_CutEdge1.low[u], Code01_CutEdge1.dfn[v]))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            e = jcast('int', Code01_CutEdge1.nxt[e])

    # 迭代版
    # u表示当前节点，preEdge表示来边
    # e表示u当前处理的边
    # 如果(e ^ 1) == preEdge，跳过当前边，对应递归版中的第一个if
    # 如果e == 0，说明所有边都处理完了
    # status的具体说明如下
    # 如果status == -1，表示u没有遍历过任何儿子
    # 如果status == 0，表示u遍历到儿子v，然后发现dfn[v] == 0
    # 并且执行完了tarjan(v, e)，对应递归版for循环的第二个if
    # 如果status == 1，表示u遍历到儿子v，然后发现dfn[v] != 0
    # 对应递归版for循环中的else分支
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code01_CutEdge1.stacksize = jcast('int', 0)
        Code01_CutEdge1.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code01_CutEdge1.stacksize > 0):
            Code01_CutEdge1.pop()
            if (Code01_CutEdge1.status == jcast('int', (-1))):
                jset(Code01_CutEdge1.dfn, Code01_CutEdge1.u, jset(Code01_CutEdge1.low, Code01_CutEdge1.u, ((_java_obj_8 := Code01_CutEdge1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3]))
                Code01_CutEdge1.e = jcast('int', Code01_CutEdge1.head[Code01_CutEdge1.u])
            else:
                v = jcast('int', Code01_CutEdge1.to[Code01_CutEdge1.e])
                if (Code01_CutEdge1.status == 0):
                    jset(Code01_CutEdge1.low, Code01_CutEdge1.u, jstatic('Math', 'min', Code01_CutEdge1.low[Code01_CutEdge1.u], Code01_CutEdge1.low[v]))
                    if (Code01_CutEdge1.low[v] > Code01_CutEdge1.dfn[Code01_CutEdge1.u]):
                        Code01_CutEdge1.cutEdge[jcast('int', (Code01_CutEdge1.e >> (1 & 31)))] = jcast('boolean', True)
                else:
                    jset(Code01_CutEdge1.low, Code01_CutEdge1.u, jstatic('Math', 'min', Code01_CutEdge1.low[Code01_CutEdge1.u], Code01_CutEdge1.dfn[v]))
                Code01_CutEdge1.e = jcast('int', Code01_CutEdge1.nxt[Code01_CutEdge1.e])
            if (jcast('int', (Code01_CutEdge1.e ^ 1)) == Code01_CutEdge1.preEdge):
                Code01_CutEdge1.e = jcast('int', Code01_CutEdge1.nxt[Code01_CutEdge1.e])
            if (Code01_CutEdge1.e != 0):
                v = jcast('int', Code01_CutEdge1.to[Code01_CutEdge1.e])
                if (Code01_CutEdge1.dfn[v] == 0):
                    Code01_CutEdge1.push(Code01_CutEdge1.u, Code01_CutEdge1.preEdge, 0, Code01_CutEdge1.e)
                    Code01_CutEdge1.push(v, Code01_CutEdge1.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code01_CutEdge1.push(Code01_CutEdge1.u, Code01_CutEdge1.preEdge, 1, Code01_CutEdge1.e)

    @staticmethod
    def main(args):
        in_ = Code01_CutEdge1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_CutEdge1.cntg = jcast('int', 1)
        Code01_CutEdge1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_CutEdge1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code01_CutEdge1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_CutEdge1.addEdge(u, v)
            Code01_CutEdge1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CutEdge1.n):
            if (Code01_CutEdge1.dfn[i] == 0):
                # tarjan1(i, 0);
                Code01_CutEdge1.tarjan2(i, 0)
            i = jcast('int', (i + 1))
        ansCnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_CutEdge1.m):
            if Code01_CutEdge1.cutEdge[i]:
                ansCnt = jcast('int', (ansCnt + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ansCnt)
        i = jcast('int', 1)
        while (i <= Code01_CutEdge1.m):
            if Code01_CutEdge1.cutEdge[i]:
                jcall(out, 'print', jadd(i, ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code01_CutEdge1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CutEdge1.MAXN = jcast('int', 500001)
Code01_CutEdge1.MAXM = jcast('int', 2000001)
Code01_CutEdge1.n = jcast('int', 0)
Code01_CutEdge1.m = jcast('int', 0)
Code01_CutEdge1.head = jarray('int', [Code01_CutEdge1.MAXN])
Code01_CutEdge1.nxt = jarray('int', [jcast('int', (Code01_CutEdge1.MAXM << (1 & 31)))])
Code01_CutEdge1.to = jarray('int', [jcast('int', (Code01_CutEdge1.MAXM << (1 & 31)))])
Code01_CutEdge1.cntg = jcast('int', 0)
Code01_CutEdge1.dfn = jarray('int', [Code01_CutEdge1.MAXN])
Code01_CutEdge1.low = jarray('int', [Code01_CutEdge1.MAXN])
Code01_CutEdge1.cntd = jcast('int', 0)
Code01_CutEdge1.cutEdge = jarray('boolean', [Code01_CutEdge1.MAXM])
Code01_CutEdge1.stack = jarray('int', [Code01_CutEdge1.MAXN, 4])
Code01_CutEdge1.u = jcast('int', 0)
Code01_CutEdge1.preEdge = jcast('int', 0)
Code01_CutEdge1.status = jcast('int', 0)
Code01_CutEdge1.e = jcast('int', 0)
Code01_CutEdge1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_CutEdge1.main([])

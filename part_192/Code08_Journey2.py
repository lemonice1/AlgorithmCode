# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 旅行，Python版
# 图中有n个点、m条无向边，节点编号1~n，图是普通树或者基环树
# 对于普通树，从1号节点开始，选择不同的遍历顺序，会形成不同的dfs序列
# 其中字典序最小的dfs序列，叫做普通树的答案
# 对于基环树，可以删掉环上的任何一条边，让基环树变成某棵普通树
# 众多普通树的答案中，字典序最小的结果，叫做基环树的答案
# 图如果是普通树，打印普通树的答案，图如果是基环树，打印基环树的答案
# 1 <= n <= 5 * 10^5
# 普通版测试 : https://www.luogu.com.cn/problem/P5022
# 加强版测试 : https://www.luogu.com.cn/problem/P5049
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Journey2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'from': 'from_', 'cycle': 'cycle', 'turn': 'turn', 'vis': 'vis', 'ans': 'ans', 'cnta': 'cnta'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    cntd = 0
    from_ = None
    cycle = None
    turn = False
    vis = None
    ans = None
    cnta = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_Journey2.nxt, ((_java_obj_1 := Code08_Journey2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_Journey2.head[u])
        Code08_Journey2.to[Code08_Journey2.cntg] = jcast('int', v)
        Code08_Journey2.head[u] = jcast('int', Code08_Journey2.cntg)

    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        jset(Code08_Journey2.dfn, u, ((_java_obj_4 := Code08_Journey2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code08_Journey2.head[u])
        while (e > 0):
            v = jcast('int', Code08_Journey2.to[e])
            if (Code08_Journey2.dfn[v] == 0):
                Code08_Journey2.from_[v] = jcast('int', u)
                Code08_Journey2.dfs(v)
            else:
                if (Code08_Journey2.dfn[u] < Code08_Journey2.dfn[v]):
                    Code08_Journey2.cycle[u] = jcast('boolean', True)
                    i = jcast('int', v)
                    while (i != u):
                        Code08_Journey2.cycle[i] = jcast('boolean', True)
                        i = jcast('int', Code08_Journey2.from_[i])
            e = jcast('int', Code08_Journey2.nxt[e])

    @staticmethod
    def path(u, back):
        u = jcast('int', u)
        back = jcast('int', back)
        Code08_Journey2.vis[u] = jcast('boolean', True)
        jset(Code08_Journey2.ans, ((_java_obj_7 := Code08_Journey2), (_java_key_8 := 'cnta'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        if ((not Code08_Journey2.cycle[u]) or Code08_Journey2.turn):
            # u不在环上 或者 已经回过头了
            # 那么像在树上遍历即可
            e = jcast('int', Code08_Journey2.head[u])
            while (e > 0):
                v = jcast('int', Code08_Journey2.to[e])
                if (not Code08_Journey2.vis[v]):
                    Code08_Journey2.path(v, jcast('int', jadd(Code08_Journey2.n, 1)))
                e = jcast('int', Code08_Journey2.nxt[e])
            return
        # u在环上 并且 还没回过头
        # 考察最后一个儿子是否符合回头需要
        end = jcast('int', 0)
        e = jcast('int', Code08_Journey2.head[u])
        while (e > 0):
            v = jcast('int', Code08_Journey2.to[e])
            if (not Code08_Journey2.vis[v]):
                end = jcast('int', v)
            e = jcast('int', Code08_Journey2.nxt[e])
        Code08_Journey2.turn = jcast('boolean', (Code08_Journey2.cycle[end] and (end > back)))
        if Code08_Journey2.turn:
            # 回头成功
            # 无视最后一个儿子
            # 因为会从环的另一侧到达
            # 其他儿子像在树上遍历即可
            e = jcast('int', Code08_Journey2.head[u])
            while (e > 0):
                v = jcast('int', Code08_Journey2.to[e])
                if ((not Code08_Journey2.vis[v]) and (v != end)):
                    Code08_Journey2.path(v, jcast('int', jadd(Code08_Journey2.n, 1)))
                e = jcast('int', Code08_Journey2.nxt[e])
            return
        # 回头不成功
        e = jcast('int', Code08_Journey2.head[u])
        while (e > 0):
            try:
                v = jcast('int', Code08_Journey2.to[e])
                if (not Code08_Journey2.vis[v]):
                    if (not Code08_Journey2.cycle[v]):
                        # 当前儿子v不在环上
                        # 像在树上遍历即可
                        Code08_Journey2.path(v, jcast('int', jadd(Code08_Journey2.n, 1)))
                    else:
                        # 当前儿子v在环上
                        # 设置好后续的back
                        # 回头可能发生在后续的环上
                        # 因为节点u最多两个环上的孩子
                        # 所以如下for循环最多发生两次
                        # 所以时间复杂度不会变高
                        next = jcast('int', back)
                        ne = jcast('int', Code08_Journey2.nxt[e])
                        while (ne > 0):
                            try:
                                nv = jcast('int', Code08_Journey2.to[ne])
                                if (not Code08_Journey2.vis[nv]):
                                    next = jcast('int', nv)
                                    raise JBreak(None)
                            except JContinue as _java_control_11:
                                if _java_control_11.label not in (None,):
                                    raise
                            except JBreak as _java_control_11:
                                if _java_control_11.label not in (None,):
                                    raise
                                break
                            ne = jcast('int', Code08_Journey2.nxt[ne])
                        Code08_Journey2.path(v, next)
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code08_Journey2.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code08_Journey2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_Journey2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_Journey2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code08_Journey2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jset(Code08_Journey2.arr[i], 0, u)
            jset(Code08_Journey2.arr[i], 1, v)
            jset(Code08_Journey2.arr[jcast('int', jadd(i, Code08_Journey2.m))], 0, v)
            jset(Code08_Journey2.arr[jcast('int', jadd(i, Code08_Journey2.m))], 1, u)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code08_Journey2.arr, 1, jcast('int', jadd(jcast('int', (Code08_Journey2.m * 2)), 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (b[1] - a[1]))))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code08_Journey2.m * 2))):
            Code08_Journey2.addEdge(Code08_Journey2.arr[i][0], Code08_Journey2.arr[i][1])
            i = jcast('int', (i + 1))
        Code08_Journey2.dfs(1)
        Code08_Journey2.path(1, jcast('int', jadd(Code08_Journey2.n, 1)))
        i = jcast('int', 1)
        while (i <= Code08_Journey2.n):
            jcall(out, 'print', jadd(Code08_Journey2.ans[i], ' '))
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code08_Journey2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Journey2.MAXN = jcast('int', 500001)
Code08_Journey2.n = jcast('int', 0)
Code08_Journey2.m = jcast('int', 0)
Code08_Journey2.arr = jarray('int', [jcast('int', (Code08_Journey2.MAXN << (1 & 31))), 2])
Code08_Journey2.head = jarray('int', [Code08_Journey2.MAXN])
Code08_Journey2.nxt = jarray('int', [jcast('int', (Code08_Journey2.MAXN << (1 & 31)))])
Code08_Journey2.to = jarray('int', [jcast('int', (Code08_Journey2.MAXN << (1 & 31)))])
Code08_Journey2.cntg = jcast('int', 0)
Code08_Journey2.dfn = jarray('int', [Code08_Journey2.MAXN])
Code08_Journey2.cntd = jcast('int', 0)
Code08_Journey2.from_ = jarray('int', [Code08_Journey2.MAXN])
Code08_Journey2.cycle = jarray('boolean', [Code08_Journey2.MAXN])
Code08_Journey2.turn = jcast('boolean', False)
Code08_Journey2.vis = jarray('boolean', [Code08_Journey2.MAXN])
Code08_Journey2.ans = jarray('int', [Code08_Journey2.MAXN])
Code08_Journey2.cnta = jcast('int', 0)

if __name__ == '__main__':
    Code08_Journey2.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 距离为k的点对是否存在，Python版
# 一共有n个节点，给定n-1条边，每条边有边权，所有节点组成一棵树
# 一共有m条查询，每条查询给定数字k，打印树上距离为k的点对是否存在
# 1 <= n <= 10^4    1 <= 边权 <= 10^4
# 1 <= m <= 100     1 <= k <= 10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3806
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Exist2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'query': 'query', 'maxk': 'maxk', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'cur': 'cur', 'cntc': 'cntc', 'all': 'all', 'cnta': 'cnta', 'exist': 'exist', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXV = 0
    n = 0
    m = 0
    query = None
    maxk = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    # 从u出发，到当前子树的每个节点，收集路径权值和
    cur = None
    cntc = 0
    # 从u出发，到之前所有子树的每个节点，收集路径权值和
    all = None
    cnta = 0
    # 使用数组替代哈希表，因为哈希表常数时间大，会超时
    exist = None
    ans = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_Exist2.nxt, ((_java_obj_1 := Code02_Exist2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Exist2.head[u])
        Code02_Exist2.to[Code02_Exist2.cntg] = jcast('int', v)
        Code02_Exist2.weight[Code02_Exist2.cntg] = jcast('int', w)
        Code02_Exist2.head[u] = jcast('int', Code02_Exist2.cntg)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Exist2.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_Exist2.head[u])
        while (e > 0):
            v = jcast('int', Code02_Exist2.to[e])
            if ((v != fa) and (not Code02_Exist2.vis[v])):
                Code02_Exist2.getSize(v, u)
                Code02_Exist2.siz[u] = jcast('int', jcast('int', jadd(Code02_Exist2.siz[u], Code02_Exist2.siz[v])))
            e = jcast('int', Code02_Exist2.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Exist2.getSize(u, fa)
        half = jcast('int', jcast('int', (Code02_Exist2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code02_Exist2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code02_Exist2.to[e])
                        if (((v != fa) and (not Code02_Exist2.vis[v])) and (Code02_Exist2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code02_Exist2.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa, dis):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        if (dis > Code02_Exist2.maxk):
            return
        jset(Code02_Exist2.cur, ((_java_obj_6 := Code02_Exist2), (_java_key_7 := 'cntc'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], dis)
        e = jcast('int', Code02_Exist2.head[u])
        while (e > 0):
            v = jcast('int', Code02_Exist2.to[e])
            if ((v != fa) and (not Code02_Exist2.vis[v])):
                Code02_Exist2.dfs(v, u, jcast('int', jadd(dis, Code02_Exist2.weight[e])))
            e = jcast('int', Code02_Exist2.nxt[e])

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code02_Exist2.cnta = jcast('int', 0)
        Code02_Exist2.exist[0] = jcast('boolean', True)
        e = jcast('int', Code02_Exist2.head[u])
        while (e > 0):
            v = jcast('int', Code02_Exist2.to[e])
            if (not Code02_Exist2.vis[v]):
                Code02_Exist2.cntc = jcast('int', 0)
                Code02_Exist2.dfs(v, u, Code02_Exist2.weight[e])
                i = jcast('int', 1)
                while (i <= Code02_Exist2.m):
                    j = jcast('int', 1)
                    while ((not Code02_Exist2.ans[i]) and (j <= Code02_Exist2.cntc)):
                        if (jcast('int', (Code02_Exist2.query[i] - Code02_Exist2.cur[j])) >= 0):
                            Code02_Exist2.ans[i] = jcast('boolean', (Code02_Exist2.ans[i] | Code02_Exist2.exist[jcast('int', (Code02_Exist2.query[i] - Code02_Exist2.cur[j]))]))
                        j = jcast('int', (j + 1))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= Code02_Exist2.cntc):
                    jset(Code02_Exist2.all, ((_java_obj_9 := Code02_Exist2), (_java_key_10 := 'cnta'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], Code02_Exist2.cur[i])
                    jset(Code02_Exist2.exist, Code02_Exist2.cur[i], True)
                    i = jcast('int', (i + 1))
            e = jcast('int', Code02_Exist2.nxt[e])
        i = jcast('int', 1)
        while (i <= Code02_Exist2.cnta):
            jset(Code02_Exist2.exist, Code02_Exist2.all[i], False)
            i = jcast('int', (i + 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code02_Exist2.vis[u] = jcast('boolean', True)
        Code02_Exist2.calc(u)
        e = jcast('int', Code02_Exist2.head[u])
        while (e > 0):
            v = jcast('int', Code02_Exist2.to[e])
            if (not Code02_Exist2.vis[v]):
                Code02_Exist2.solve(Code02_Exist2.getCentroid(v, u))
            e = jcast('int', Code02_Exist2.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code02_Exist2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Exist2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Exist2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code02_Exist2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code02_Exist2.addEdge(u, v, w)
            Code02_Exist2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Exist2.m):
            jset(Code02_Exist2.query, i, jcall(in_, 'nextInt'))
            Code02_Exist2.maxk = jcast('int', jstatic('Math', 'max', Code02_Exist2.maxk, Code02_Exist2.query[i]))
            i = jcast('int', (i + 1))
        Code02_Exist2.solve(Code02_Exist2.getCentroid(1, 0))
        i = jcast('int', 1)
        while (i <= Code02_Exist2.m):
            if Code02_Exist2.ans[i]:
                jcall(out, 'println', 'AYE')
            else:
                jcall(out, 'println', 'NAY')
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
            raise TypeError("No matching overload for Code02_Exist2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Exist2.MAXN = jcast('int', 10001)
Code02_Exist2.MAXM = jcast('int', 101)
Code02_Exist2.MAXV = jcast('int', 10000001)
Code02_Exist2.n = jcast('int', 0)
Code02_Exist2.m = jcast('int', 0)
Code02_Exist2.query = jarray('int', [Code02_Exist2.MAXM])
Code02_Exist2.maxk = jcast('int', 0)
Code02_Exist2.head = jarray('int', [Code02_Exist2.MAXN])
Code02_Exist2.nxt = jarray('int', [jcast('int', (Code02_Exist2.MAXN << (1 & 31)))])
Code02_Exist2.to = jarray('int', [jcast('int', (Code02_Exist2.MAXN << (1 & 31)))])
Code02_Exist2.weight = jarray('int', [jcast('int', (Code02_Exist2.MAXN << (1 & 31)))])
Code02_Exist2.cntg = jcast('int', 0)
Code02_Exist2.vis = jarray('boolean', [Code02_Exist2.MAXN])
Code02_Exist2.siz = jarray('int', [Code02_Exist2.MAXN])
Code02_Exist2.cur = jarray('int', [Code02_Exist2.MAXN])
Code02_Exist2.cntc = jcast('int', 0)
Code02_Exist2.all = jarray('int', [Code02_Exist2.MAXN])
Code02_Exist2.cnta = jcast('int', 0)
Code02_Exist2.exist = jarray('boolean', [Code02_Exist2.MAXV])
Code02_Exist2.ans = jarray('boolean', [Code02_Exist2.MAXM])

if __name__ == '__main__':
    Code02_Exist2.main([])

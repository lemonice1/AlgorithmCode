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

# 模式字符串，Python版
# 一共有n个点，给定n-1条边，所有节点组成一棵树
# 每个点有点权，是一个大写字母，只考虑大写字母A到Z
# 给定一个长度为m的字符串s，也只由大写字母A到Z组成
# 考虑点对(u, v)的简单路径，把沿途节点的字母拼接起来
# 如果拼接字符串恰好是s重复正数次，那么该点对合法
# 打印合法点对的数量，注意(u, v)和(v, u)是不同的点对
# 1 <= m <= n <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4075
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_ModeString1:
    __java_fields__ = {'MAXN': 'MAXN', 'BASE': 'BASE', 't': 't', 'n': 'n', 'm': 'm', 'val': 'val', 'str': 'str', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'pre': 'pre', 'suf': 'suf', 'vis': 'vis', 'siz': 'siz', 'deep': 'deep', 'curp': 'curp', 'curs': 'curs', 'allp': 'allp', 'alls': 'alls', 'ans': 'ans', 'stack': 'stack', 'hashst': 'hashst', 'u': 'u', 'f': 'f', 'dep': 'dep', 'e': 'e', 'hash': 'hash', 'stacksize': 'stacksize'}
    MAXN = 0
    BASE = 0
    t = 0
    n = 0
    m = 0
    val = None
    str = None
    a = None
    b = None
    head = None
    nxt = None
    to = None
    cntg = 0
    pre = None
    suf = None
    vis = None
    siz = None
    deep = None
    curp = None
    curs = None
    allp = None
    alls = None
    ans = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    hashst = None
    u = 0
    f = 0
    dep = 0
    e = 0
    hash = 0
    stacksize = 0
    @staticmethod
    def push(u, f, dep, hash, e):
        u = jcast('int', u)
        f = jcast('int', f)
        dep = jcast('int', dep)
        hash = jcast('long', hash)
        e = jcast('int', e)
        jset(Code07_ModeString1.stack[Code07_ModeString1.stacksize], 0, u)
        jset(Code07_ModeString1.stack[Code07_ModeString1.stacksize], 1, f)
        jset(Code07_ModeString1.stack[Code07_ModeString1.stacksize], 2, dep)
        jset(Code07_ModeString1.stack[Code07_ModeString1.stacksize], 3, e)
        Code07_ModeString1.hashst[Code07_ModeString1.stacksize] = jcast('long', hash)
        Code07_ModeString1.stacksize = jcast('int', (Code07_ModeString1.stacksize + 1))

    @staticmethod
    def pop():
        Code07_ModeString1.stacksize = jcast('int', (Code07_ModeString1.stacksize - 1))
        Code07_ModeString1.u = jcast('int', Code07_ModeString1.stack[Code07_ModeString1.stacksize][0])
        Code07_ModeString1.f = jcast('int', Code07_ModeString1.stack[Code07_ModeString1.stacksize][1])
        Code07_ModeString1.dep = jcast('int', Code07_ModeString1.stack[Code07_ModeString1.stacksize][2])
        Code07_ModeString1.e = jcast('int', Code07_ModeString1.stack[Code07_ModeString1.stacksize][3])
        Code07_ModeString1.hash = jcast('long', Code07_ModeString1.hashst[Code07_ModeString1.stacksize])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_ModeString1.nxt, ((_java_obj_1 := Code07_ModeString1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_ModeString1.head[u])
        Code07_ModeString1.to[Code07_ModeString1.cntg] = jcast('int', v)
        Code07_ModeString1.head[u] = jcast('int', Code07_ModeString1.cntg)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_ModeString1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_ModeString1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ModeString1.to[e])
            if ((v != fa) and (not Code07_ModeString1.vis[v])):
                Code07_ModeString1.getSize1(v, u)
                Code07_ModeString1.siz[u] = jcast('int', jcast('int', jadd(Code07_ModeString1.siz[u], Code07_ModeString1.siz[v])))
            e = jcast('int', Code07_ModeString1.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code07_ModeString1.stacksize = jcast('int', 0)
        Code07_ModeString1.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code07_ModeString1.stacksize > 0):
            Code07_ModeString1.pop()
            if (Code07_ModeString1.e == jcast('int', (-1))):
                Code07_ModeString1.siz[Code07_ModeString1.u] = jcast('int', 1)
                Code07_ModeString1.e = jcast('int', Code07_ModeString1.head[Code07_ModeString1.u])
            else:
                Code07_ModeString1.e = jcast('int', Code07_ModeString1.nxt[Code07_ModeString1.e])
            if (Code07_ModeString1.e != 0):
                Code07_ModeString1.push(Code07_ModeString1.u, Code07_ModeString1.f, 0, 0, Code07_ModeString1.e)
                v = jcast('int', Code07_ModeString1.to[Code07_ModeString1.e])
                if ((v != Code07_ModeString1.f) and (not Code07_ModeString1.vis[v])):
                    Code07_ModeString1.push(v, Code07_ModeString1.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_ModeString1.head[Code07_ModeString1.u])
                while (ei > 0):
                    v = jcast('int', Code07_ModeString1.to[ei])
                    if ((v != Code07_ModeString1.f) and (not Code07_ModeString1.vis[v])):
                        Code07_ModeString1.siz[Code07_ModeString1.u] = jcast('int', jcast('int', jadd(Code07_ModeString1.siz[Code07_ModeString1.u], Code07_ModeString1.siz[v])))
                    ei = jcast('int', Code07_ModeString1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code07_ModeString1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code07_ModeString1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code07_ModeString1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code07_ModeString1.to[e])
                        if (((v != fa) and (not Code07_ModeString1.vis[v])) and (Code07_ModeString1.siz[v] > half)):
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
                    e = jcast('int', Code07_ModeString1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    # 收集信息 + 结算答案递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, dep, hash):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dep = jcast('int', dep)
        hash = jcast('long', hash)
        Code07_ModeString1.deep[u] = jcast('int', dep)
        hash = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (hash * Code07_ModeString1.BASE)), Code07_ModeString1.val[u])) - jchar('A'))), 1)))
        if (hash == Code07_ModeString1.pre[dep]):
            ((_java_obj_6 := Code07_ModeString1.curp), (_java_key_7 := jcast('int', jadd(jcast('int', jmod(jcast('int', (dep - 1)), Code07_ModeString1.m)), 1))), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('long', (_java_old_8 + (1)))), _java_old_8)[4]
            Code07_ModeString1.ans = jcast('long', jcast('long', jadd(Code07_ModeString1.ans, Code07_ModeString1.alls[jcast('int', (Code07_ModeString1.m - jcast('int', jmod(jcast('int', (dep - 1)), Code07_ModeString1.m))))])))
        if (hash == Code07_ModeString1.suf[dep]):
            ((_java_obj_9 := Code07_ModeString1.curs), (_java_key_10 := jcast('int', jadd(jcast('int', jmod(jcast('int', (dep - 1)), Code07_ModeString1.m)), 1))), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('long', (_java_old_11 + (1)))), _java_old_11)[4]
            Code07_ModeString1.ans = jcast('long', jcast('long', jadd(Code07_ModeString1.ans, Code07_ModeString1.allp[jcast('int', (Code07_ModeString1.m - jcast('int', jmod(jcast('int', (dep - 1)), Code07_ModeString1.m))))])))
        e = jcast('int', Code07_ModeString1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ModeString1.to[e])
            if ((v != fa) and (not Code07_ModeString1.vis[v])):
                Code07_ModeString1.dfs1(v, u, jcast('int', jadd(dep, 1)), hash)
                jset(Code07_ModeString1.deep, u, jstatic('Math', 'max', Code07_ModeString1.deep[u], Code07_ModeString1.deep[v]))
            e = jcast('int', Code07_ModeString1.nxt[e])

    # 收集信息 + 结算答案迭代版
    @staticmethod
    def dfs2(cur, fa, pdep, phash):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        pdep = jcast('int', pdep)
        phash = jcast('long', phash)
        Code07_ModeString1.stacksize = jcast('int', 0)
        Code07_ModeString1.push(cur, fa, pdep, phash, jcast('int', (-1)))
        while (Code07_ModeString1.stacksize > 0):
            Code07_ModeString1.pop()
            if (Code07_ModeString1.e == jcast('int', (-1))):
                Code07_ModeString1.deep[Code07_ModeString1.u] = jcast('int', Code07_ModeString1.dep)
                Code07_ModeString1.hash = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code07_ModeString1.hash * Code07_ModeString1.BASE)), Code07_ModeString1.val[Code07_ModeString1.u])) - jchar('A'))), 1)))
                if (Code07_ModeString1.hash == Code07_ModeString1.pre[Code07_ModeString1.dep]):
                    ((_java_obj_12 := Code07_ModeString1.curp), (_java_key_13 := jcast('int', jadd(jcast('int', jmod(jcast('int', (Code07_ModeString1.dep - 1)), Code07_ModeString1.m)), 1))), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('long', (_java_old_14 + (1)))), _java_old_14)[4]
                    Code07_ModeString1.ans = jcast('long', jcast('long', jadd(Code07_ModeString1.ans, Code07_ModeString1.alls[jcast('int', (Code07_ModeString1.m - jcast('int', jmod(jcast('int', (Code07_ModeString1.dep - 1)), Code07_ModeString1.m))))])))
                if (Code07_ModeString1.hash == Code07_ModeString1.suf[Code07_ModeString1.dep]):
                    ((_java_obj_15 := Code07_ModeString1.curs), (_java_key_16 := jcast('int', jadd(jcast('int', jmod(jcast('int', (Code07_ModeString1.dep - 1)), Code07_ModeString1.m)), 1))), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('long', (_java_old_17 + (1)))), _java_old_17)[4]
                    Code07_ModeString1.ans = jcast('long', jcast('long', jadd(Code07_ModeString1.ans, Code07_ModeString1.allp[jcast('int', (Code07_ModeString1.m - jcast('int', jmod(jcast('int', (Code07_ModeString1.dep - 1)), Code07_ModeString1.m))))])))
                Code07_ModeString1.e = jcast('int', Code07_ModeString1.head[Code07_ModeString1.u])
            else:
                Code07_ModeString1.e = jcast('int', Code07_ModeString1.nxt[Code07_ModeString1.e])
            if (Code07_ModeString1.e != 0):
                Code07_ModeString1.push(Code07_ModeString1.u, Code07_ModeString1.f, Code07_ModeString1.dep, Code07_ModeString1.hash, Code07_ModeString1.e)
                v = jcast('int', Code07_ModeString1.to[Code07_ModeString1.e])
                if ((v != Code07_ModeString1.f) and (not Code07_ModeString1.vis[v])):
                    Code07_ModeString1.push(v, Code07_ModeString1.u, jcast('int', jadd(Code07_ModeString1.dep, 1)), Code07_ModeString1.hash, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_ModeString1.head[Code07_ModeString1.u])
                while (ei > 0):
                    v = jcast('int', Code07_ModeString1.to[ei])
                    if ((v != Code07_ModeString1.f) and (not Code07_ModeString1.vis[v])):
                        jset(Code07_ModeString1.deep, Code07_ModeString1.u, jstatic('Math', 'max', Code07_ModeString1.deep[Code07_ModeString1.u], Code07_ModeString1.deep[v]))
                    ei = jcast('int', Code07_ModeString1.nxt[ei])

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        maxDep = jcast('int', 0)
        jset(Code07_ModeString1.allp, 1, jset(Code07_ModeString1.alls, 1, 1))
        e = jcast('int', Code07_ModeString1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ModeString1.to[e])
            if (not Code07_ModeString1.vis[v]):
                # dfs1(v, u, 2, arr[u] - 'A' + 1);
                Code07_ModeString1.dfs2(v, u, 2, jcast('int', jadd(jcast('int', (Code07_ModeString1.val[u] - jchar('A'))), 1)))
                curDep = jcast('int', jstatic('Math', 'min', Code07_ModeString1.deep[v], Code07_ModeString1.m))
                i = jcast('int', 1)
                while (i <= curDep):
                    Code07_ModeString1.allp[i] = jcast('long', jcast('long', jadd(Code07_ModeString1.allp[i], Code07_ModeString1.curp[i])))
                    Code07_ModeString1.alls[i] = jcast('long', jcast('long', jadd(Code07_ModeString1.alls[i], Code07_ModeString1.curs[i])))
                    jset(Code07_ModeString1.curp, i, jset(Code07_ModeString1.curs, i, 0))
                    i = jcast('int', (i + 1))
                maxDep = jcast('int', jstatic('Math', 'max', maxDep, curDep))
            e = jcast('int', Code07_ModeString1.nxt[e])
        i = jcast('int', 1)
        while (i <= maxDep):
            jset(Code07_ModeString1.allp, i, jset(Code07_ModeString1.alls, i, 0))
            i = jcast('int', (i + 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code07_ModeString1.vis[u] = jcast('boolean', True)
        Code07_ModeString1.calc(u)
        e = jcast('int', Code07_ModeString1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ModeString1.to[e])
            if (not Code07_ModeString1.vis[v]):
                Code07_ModeString1.solve(Code07_ModeString1.getCentroid(v, u))
            e = jcast('int', Code07_ModeString1.nxt[e])

    @staticmethod
    def prepare():
        Code07_ModeString1.cntg = jcast('int', 0)
        Code07_ModeString1.ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code07_ModeString1.n):
            Code07_ModeString1.head[i] = jcast('int', 0)
            Code07_ModeString1.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code07_ModeString1.n):
            Code07_ModeString1.addEdge(Code07_ModeString1.a[i], Code07_ModeString1.b[i])
            Code07_ModeString1.addEdge(Code07_ModeString1.b[i], Code07_ModeString1.a[i])
            i = jcast('int', (i + 1))
        tmp = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code07_ModeString1.n):
            Code07_ModeString1.pre[i] = jcast('long', jcast('long', jadd(Code07_ModeString1.pre[jcast('int', (i - 1))], jcast('long', (tmp * jcast('int', jadd(jcast('int', (Code07_ModeString1.str[jcast('int', jadd(jcast('int', jmod(jcast('int', (i - 1)), Code07_ModeString1.m)), 1))] - jchar('A'))), 1)))))))
            Code07_ModeString1.suf[i] = jcast('long', jcast('long', jadd(Code07_ModeString1.suf[jcast('int', (i - 1))], jcast('long', (tmp * jcast('int', jadd(jcast('int', (Code07_ModeString1.str[jcast('int', (Code07_ModeString1.m - jcast('int', jmod(jcast('int', (i - 1)), Code07_ModeString1.m))))] - jchar('A'))), 1)))))))
            tmp = jcast('long', jcast('long', (tmp * Code07_ModeString1.BASE)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_ModeString1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_ModeString1.t = jcast('int', jcall(in_, 'nextInt'))
        k = jcast('int', 1)
        while (k <= Code07_ModeString1.t):
            Code07_ModeString1.n = jcast('int', jcall(in_, 'nextInt'))
            Code07_ModeString1.m = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code07_ModeString1.n):
                jset(Code07_ModeString1.val, i, jcall(in_, 'nextUpperCase'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i < Code07_ModeString1.n):
                jset(Code07_ModeString1.a, i, jcall(in_, 'nextInt'))
                jset(Code07_ModeString1.b, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code07_ModeString1.m):
                jset(Code07_ModeString1.str, i, jcall(in_, 'nextUpperCase'))
                i = jcast('int', (i + 1))
            Code07_ModeString1.prepare()
            Code07_ModeString1.solve(Code07_ModeString1.getCentroid(1, 0))
            jcall(out, 'println', Code07_ModeString1.ans)
            k = jcast('int', (k + 1))
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

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

        def nextUpperCase(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if ((c >= jchar('A')) and (c <= jchar('Z'))):
                    return jcast('char', jcast('char', c))

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
            raise TypeError("No matching overload for Code07_ModeString1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_ModeString1.MAXN = jcast('int', 100001)
Code07_ModeString1.BASE = jcast('int', 499)
Code07_ModeString1.t = jcast('int', 0)
Code07_ModeString1.n = jcast('int', 0)
Code07_ModeString1.m = jcast('int', 0)
Code07_ModeString1.val = jarray('char', [Code07_ModeString1.MAXN])
Code07_ModeString1.str = jarray('char', [Code07_ModeString1.MAXN])
Code07_ModeString1.a = jarray('int', [Code07_ModeString1.MAXN])
Code07_ModeString1.b = jarray('int', [Code07_ModeString1.MAXN])
Code07_ModeString1.head = jarray('int', [Code07_ModeString1.MAXN])
Code07_ModeString1.nxt = jarray('int', [jcast('int', (Code07_ModeString1.MAXN << (1 & 31)))])
Code07_ModeString1.to = jarray('int', [jcast('int', (Code07_ModeString1.MAXN << (1 & 31)))])
Code07_ModeString1.cntg = jcast('int', 0)
Code07_ModeString1.pre = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.suf = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.vis = jarray('boolean', [Code07_ModeString1.MAXN])
Code07_ModeString1.siz = jarray('int', [Code07_ModeString1.MAXN])
Code07_ModeString1.deep = jarray('int', [Code07_ModeString1.MAXN])
Code07_ModeString1.curp = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.curs = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.allp = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.alls = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.ans = jcast('long', 0)
Code07_ModeString1.stack = jarray('int', [Code07_ModeString1.MAXN, 4])
Code07_ModeString1.hashst = jarray('long', [Code07_ModeString1.MAXN])
Code07_ModeString1.u = jcast('int', 0)
Code07_ModeString1.f = jcast('int', 0)
Code07_ModeString1.dep = jcast('int', 0)
Code07_ModeString1.e = jcast('int', 0)
Code07_ModeString1.hash = jcast('long', 0)
Code07_ModeString1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_ModeString1.main([])

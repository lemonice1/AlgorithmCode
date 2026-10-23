# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 软件包管理器，Python版
# 一共有n个软件，编号0~n-1，0号软件不依赖任何软件，其他每个软件都仅依赖一个软件
# 依赖关系由数组形式给出，题目保证不会出现循环依赖
# 一开始所有软件都是没有安装的，如果a依赖b，那么安装a需要安装b，同时卸载b需要卸载a
# 一共有m条操作，每种操作是如下2种类型中的一种
# 操作 install x    : 安装x，如果x已经安装打印0，否则打印有多少个软件的状态需要改变
# 操作 uninstall x  : 卸载x，如果x没有安装打印0，否则打印有多少个软件的状态需要改变
# 1 <= n、m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P2146
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_PackageManager2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'cntd': 'cntd', 'sum': 'sum', 'update': 'update_data', 'change': 'change', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
    head = None
    next = None
    to = None
    cntg = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    cntd = 0
    sum = None
    update_data = None
    change = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_PackageManager2.next, ((_java_obj_1 := Code04_PackageManager2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_PackageManager2.head[u])
        Code04_PackageManager2.to[Code04_PackageManager2.cntg] = jcast('int', v)
        Code04_PackageManager2.head[u] = jcast('int', Code04_PackageManager2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_PackageManager2.fa[u] = jcast('int', f)
        Code04_PackageManager2.dep[u] = jcast('int', jcast('int', jadd(Code04_PackageManager2.dep[f], 1)))
        Code04_PackageManager2.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_PackageManager2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_PackageManager2.to[e])
            if (v != f):
                Code04_PackageManager2.dfs1(v, u)
            e = jcast('int', Code04_PackageManager2.next[e])
        e = jcast('int', Code04_PackageManager2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_PackageManager2.to[e])
            if (v != f):
                Code04_PackageManager2.siz[u] = jcast('int', jcast('int', jadd(Code04_PackageManager2.siz[u], Code04_PackageManager2.siz[v])))
                if ((Code04_PackageManager2.son[u] == 0) or (Code04_PackageManager2.siz[Code04_PackageManager2.son[u]] < Code04_PackageManager2.siz[v])):
                    Code04_PackageManager2.son[u] = jcast('int', v)
            e = jcast('int', Code04_PackageManager2.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code04_PackageManager2.top[u] = jcast('int', t)
        jset(Code04_PackageManager2.dfn, u, ((_java_obj_4 := Code04_PackageManager2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (Code04_PackageManager2.son[u] == 0):
            return
        Code04_PackageManager2.dfs2(Code04_PackageManager2.son[u], t)
        e = jcast('int', Code04_PackageManager2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_PackageManager2.to[e])
            if ((v != Code04_PackageManager2.fa[u]) and (v != Code04_PackageManager2.son[u])):
                Code04_PackageManager2.dfs2(v, v)
            e = jcast('int', Code04_PackageManager2.next[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    fse = None
    stacksize = 0
    first = 0
    second = 0
    edge = 0
    @staticmethod
    def push(fir, sec, edg):
        fir = jcast('int', fir)
        sec = jcast('int', sec)
        edg = jcast('int', edg)
        jset(Code04_PackageManager2.fse[Code04_PackageManager2.stacksize], 0, fir)
        jset(Code04_PackageManager2.fse[Code04_PackageManager2.stacksize], 1, sec)
        jset(Code04_PackageManager2.fse[Code04_PackageManager2.stacksize], 2, edg)
        Code04_PackageManager2.stacksize = jcast('int', (Code04_PackageManager2.stacksize + 1))

    @staticmethod
    def pop():
        Code04_PackageManager2.stacksize = jcast('int', (Code04_PackageManager2.stacksize - 1))
        Code04_PackageManager2.first = jcast('int', Code04_PackageManager2.fse[Code04_PackageManager2.stacksize][0])
        Code04_PackageManager2.second = jcast('int', Code04_PackageManager2.fse[Code04_PackageManager2.stacksize][1])
        Code04_PackageManager2.edge = jcast('int', Code04_PackageManager2.fse[Code04_PackageManager2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code04_PackageManager2.stacksize = jcast('int', 0)
        Code04_PackageManager2.push(1, 0, jcast('int', (-1)))
        while (Code04_PackageManager2.stacksize > 0):
            Code04_PackageManager2.pop()
            if (Code04_PackageManager2.edge == jcast('int', (-1))):
                Code04_PackageManager2.fa[Code04_PackageManager2.first] = jcast('int', Code04_PackageManager2.second)
                Code04_PackageManager2.dep[Code04_PackageManager2.first] = jcast('int', jcast('int', jadd(Code04_PackageManager2.dep[Code04_PackageManager2.second], 1)))
                Code04_PackageManager2.siz[Code04_PackageManager2.first] = jcast('int', 1)
                Code04_PackageManager2.edge = jcast('int', Code04_PackageManager2.head[Code04_PackageManager2.first])
            else:
                Code04_PackageManager2.edge = jcast('int', Code04_PackageManager2.next[Code04_PackageManager2.edge])
            if (Code04_PackageManager2.edge != 0):
                Code04_PackageManager2.push(Code04_PackageManager2.first, Code04_PackageManager2.second, Code04_PackageManager2.edge)
                if (Code04_PackageManager2.to[Code04_PackageManager2.edge] != Code04_PackageManager2.second):
                    Code04_PackageManager2.push(Code04_PackageManager2.to[Code04_PackageManager2.edge], Code04_PackageManager2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code04_PackageManager2.head[Code04_PackageManager2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code04_PackageManager2.to[e])
                    if (v != Code04_PackageManager2.second):
                        Code04_PackageManager2.siz[Code04_PackageManager2.first] = jcast('int', jcast('int', jadd(Code04_PackageManager2.siz[Code04_PackageManager2.first], Code04_PackageManager2.siz[v])))
                        if ((Code04_PackageManager2.son[Code04_PackageManager2.first] == 0) or (Code04_PackageManager2.siz[Code04_PackageManager2.son[Code04_PackageManager2.first]] < Code04_PackageManager2.siz[v])):
                            Code04_PackageManager2.son[Code04_PackageManager2.first] = jcast('int', v)
                    e = jcast('int', Code04_PackageManager2.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code04_PackageManager2.stacksize = jcast('int', 0)
        Code04_PackageManager2.push(1, 1, jcast('int', (-1)))
        while (Code04_PackageManager2.stacksize > 0):
            try:
                Code04_PackageManager2.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code04_PackageManager2.edge == jcast('int', (-1))):
                    Code04_PackageManager2.top[Code04_PackageManager2.first] = jcast('int', Code04_PackageManager2.second)
                    jset(Code04_PackageManager2.dfn, Code04_PackageManager2.first, ((_java_obj_8 := Code04_PackageManager2), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    if (Code04_PackageManager2.son[Code04_PackageManager2.first] == 0):
                        raise JContinue(None)
                    Code04_PackageManager2.push(Code04_PackageManager2.first, Code04_PackageManager2.second, jcast('int', (-2)))
                    Code04_PackageManager2.push(Code04_PackageManager2.son[Code04_PackageManager2.first], Code04_PackageManager2.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code04_PackageManager2.edge == jcast('int', (-2))):
                        Code04_PackageManager2.edge = jcast('int', Code04_PackageManager2.head[Code04_PackageManager2.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code04_PackageManager2.edge = jcast('int', Code04_PackageManager2.next[Code04_PackageManager2.edge])
                if (Code04_PackageManager2.edge != 0):
                    Code04_PackageManager2.push(Code04_PackageManager2.first, Code04_PackageManager2.second, Code04_PackageManager2.edge)
                    if ((Code04_PackageManager2.to[Code04_PackageManager2.edge] != Code04_PackageManager2.fa[Code04_PackageManager2.first]) and (Code04_PackageManager2.to[Code04_PackageManager2.edge] != Code04_PackageManager2.son[Code04_PackageManager2.first])):
                        Code04_PackageManager2.push(Code04_PackageManager2.to[Code04_PackageManager2.edge], Code04_PackageManager2.to[Code04_PackageManager2.edge], jcast('int', (-1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_PackageManager2.sum[i] = jcast('int', jcast('int', jadd(Code04_PackageManager2.sum[jcast('int', (i << (1 & 31)))], Code04_PackageManager2.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 线段树重置操作的懒更新
    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('int', v)
        n = jcast('int', n)
        Code04_PackageManager2.sum[i] = jcast('int', jcast('int', (v * n)))
        Code04_PackageManager2.update_data[i] = jcast('boolean', True)
        Code04_PackageManager2.change[i] = jcast('int', v)

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code04_PackageManager2.update_data[i]:
            Code04_PackageManager2.lazy(jcast('int', (i << (1 & 31))), Code04_PackageManager2.change[i], ln)
            Code04_PackageManager2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code04_PackageManager2.change[i], rn)
            Code04_PackageManager2.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_PackageManager2.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code04_PackageManager2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code04_PackageManager2.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_PackageManager2.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_PackageManager2.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code04_PackageManager2.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code04_PackageManager2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_PackageManager2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_PackageManager2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    # 从1到x的路径上，所有节点值改成v
    @staticmethod
    def pathUpdate(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        y = jcast('int', 1)
        while (Code04_PackageManager2.top[x] != Code04_PackageManager2.top[y]):
            if (Code04_PackageManager2.dep[Code04_PackageManager2.top[x]] <= Code04_PackageManager2.dep[Code04_PackageManager2.top[y]]):
                Code04_PackageManager2.update(Code04_PackageManager2.dfn[Code04_PackageManager2.top[y]], Code04_PackageManager2.dfn[y], v, 1, Code04_PackageManager2.n, 1)
                y = jcast('int', Code04_PackageManager2.fa[Code04_PackageManager2.top[y]])
            else:
                Code04_PackageManager2.update(Code04_PackageManager2.dfn[Code04_PackageManager2.top[x]], Code04_PackageManager2.dfn[x], v, 1, Code04_PackageManager2.n, 1)
                x = jcast('int', Code04_PackageManager2.fa[Code04_PackageManager2.top[x]])
        Code04_PackageManager2.update(jstatic('Math', 'min', Code04_PackageManager2.dfn[x], Code04_PackageManager2.dfn[y]), jstatic('Math', 'max', Code04_PackageManager2.dfn[x], Code04_PackageManager2.dfn[y]), v, 1, Code04_PackageManager2.n, 1)

    @staticmethod
    def install(x):
        x = jcast('int', x)
        pre = jcast('int', Code04_PackageManager2.sum[1])
        Code04_PackageManager2.pathUpdate(x, 1)
        post = jcast('int', Code04_PackageManager2.sum[1])
        return jcast('int', jstatic('Math', 'abs', jcast('int', (post - pre))))

    @staticmethod
    def uninstall(x):
        x = jcast('int', x)
        pre = jcast('int', Code04_PackageManager2.sum[1])
        Code04_PackageManager2.update(Code04_PackageManager2.dfn[x], jcast('int', (jcast('int', jadd(Code04_PackageManager2.dfn[x], Code04_PackageManager2.siz[x])) - 1)), 0, 1, Code04_PackageManager2.n, 1)
        post = jcast('int', Code04_PackageManager2.sum[1])
        return jcast('int', jstatic('Math', 'abs', jcast('int', (post - pre))))

    @staticmethod
    def main(args):
        io = Code04_PackageManager2.Kattio(_java_ctor=0)
        Code04_PackageManager2.n = jcast('int', jcall(io, 'nextInt'))
        u = jcast('int', 2)
        v = 0
        while (u <= Code04_PackageManager2.n):
            v = jcast('int', jcast('int', jadd(jcall(io, 'nextInt'), 1)))
            Code04_PackageManager2.addEdge(v, u)
            u = jcast('int', (u + 1))
        # dfs3() 等同于 dfs1(1, 0)，调用迭代版防止爆栈
        Code04_PackageManager2.dfs3()
        # dfs4() 等同于 dfs2(1, 1)，调用迭代版防止爆栈
        Code04_PackageManager2.dfs4()
        Code04_PackageManager2.m = jcast('int', jcall(io, 'nextInt'))
        op = None
        x = 0
        i = jcast('int', 1)
        while (i <= Code04_PackageManager2.m):
            op = jcall(io, 'next')
            x = jcast('int', jcast('int', jadd(jcall(io, 'nextInt'), 1)))
            if jcall(op, 'equals', 'install'):
                jcall(io, 'println', Code04_PackageManager2.install(x))
            else:
                jcall(io, 'println', Code04_PackageManager2.uninstall(x))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'Exception'):
                    e = _java_exception_11
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code04_PackageManager2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PackageManager2.MAXN = jcast('int', 100001)
Code04_PackageManager2.n = jcast('int', 0)
Code04_PackageManager2.m = jcast('int', 0)
Code04_PackageManager2.head = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.next = jarray('int', [jcast('int', (Code04_PackageManager2.MAXN << (1 & 31)))])
Code04_PackageManager2.to = jarray('int', [jcast('int', (Code04_PackageManager2.MAXN << (1 & 31)))])
Code04_PackageManager2.cntg = jcast('int', 0)
Code04_PackageManager2.fa = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.dep = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.siz = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.son = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.top = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.dfn = jarray('int', [Code04_PackageManager2.MAXN])
Code04_PackageManager2.cntd = jcast('int', 0)
Code04_PackageManager2.sum = jarray('int', [jcast('int', (Code04_PackageManager2.MAXN << (2 & 31)))])
Code04_PackageManager2.update_data = jarray('boolean', [jcast('int', (Code04_PackageManager2.MAXN << (2 & 31)))])
Code04_PackageManager2.change = jarray('int', [jcast('int', (Code04_PackageManager2.MAXN << (2 & 31)))])
Code04_PackageManager2.fse = jarray('int', [Code04_PackageManager2.MAXN, 3])
Code04_PackageManager2.stacksize = jcast('int', 0)
Code04_PackageManager2.first = jcast('int', 0)
Code04_PackageManager2.second = jcast('int', 0)
Code04_PackageManager2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code04_PackageManager2.main([])

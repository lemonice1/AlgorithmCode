# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不同名字数量，Python版
# 一共有n个节点，编号1~n，给定每个节点的名字和父亲节点编号
# 名字是string类型，如果父亲节点编号为0，说明当前节点是某棵树的头节点
# 注意，n个节点组成的是森林结构，可能有若干棵树
# 一共有m条查询，每条查询 x k，含义如下
# 以x为头的子树上，到x距离为k的所有节点中，打印不同名字的数量
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF246E
# 测试链接 : https://codeforces.com/problemset/problem/246/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_DifferntName2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'nameId': 'nameId', 'root': 'root', 'id': 'id', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headq': 'headq', 'nextq': 'nextq', 'ansiq': 'ansiq', 'kq': 'kq', 'cntq': 'cntq', 'fa': 'fa', 'siz': 'siz', 'dep': 'dep', 'son': 'son', 'depSet': 'depSet', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    nameId = None
    root = None
    id = None
    # 链式前向星
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 问题列表
    headq = None
    nextq = None
    ansiq = None
    kq = None
    cntq = 0
    # 树链剖分
    fa = None
    siz = None
    dep = None
    son = None
    # 树上启发式合并
    depSet = None
    ans = None
    @staticmethod
    def getNameId(name):
        if jcall(Code04_DifferntName2.nameId, 'containsKey', name):
            return jcast('int', jcall(Code04_DifferntName2.nameId, 'get', name))
        jcall(Code04_DifferntName2.nameId, 'put', name, jcast('int', jadd(jcall(Code04_DifferntName2.nameId, 'size'), 1)))
        return jcast('int', jcall(Code04_DifferntName2.nameId, 'size'))

    @staticmethod
    def addId(deep, id):
        deep = jcast('int', deep)
        id = jcast('int', id)
        jcall(jcall(Code04_DifferntName2.depSet, 'get', deep), 'add', id)

    @staticmethod
    def removeId(deep, id):
        deep = jcast('int', deep)
        id = jcast('int', id)
        jcall(jcall(Code04_DifferntName2.depSet, 'get', deep), 'remove', id)

    @staticmethod
    def sizeOfDeep(deep):
        deep = jcast('int', deep)
        if (deep > Code04_DifferntName2.n):
            return jcast('int', 0)
        return jcast('int', jcall(jcall(Code04_DifferntName2.depSet, 'get', deep), 'size'))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_DifferntName2.nextg, ((_java_obj_1 := Code04_DifferntName2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_DifferntName2.headg[u])
        Code04_DifferntName2.tog[Code04_DifferntName2.cntg] = jcast('int', v)
        Code04_DifferntName2.headg[u] = jcast('int', Code04_DifferntName2.cntg)

    @staticmethod
    def addQuestion(u, ansi, k):
        u = jcast('int', u)
        ansi = jcast('int', ansi)
        k = jcast('int', k)
        jset(Code04_DifferntName2.nextq, ((_java_obj_4 := Code04_DifferntName2), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_DifferntName2.headq[u])
        Code04_DifferntName2.ansiq[Code04_DifferntName2.cntq] = jcast('int', ansi)
        Code04_DifferntName2.kq[Code04_DifferntName2.cntq] = jcast('int', k)
        Code04_DifferntName2.headq[u] = jcast('int', Code04_DifferntName2.cntq)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_DifferntName2.fa[u] = jcast('int', f)
        Code04_DifferntName2.siz[u] = jcast('int', 1)
        Code04_DifferntName2.dep[u] = jcast('int', jcast('int', jadd(Code04_DifferntName2.dep[f], 1)))
        e = jcast('int', Code04_DifferntName2.headg[u])
        while (e > 0):
            Code04_DifferntName2.dfs1(Code04_DifferntName2.tog[e], u)
            e = jcast('int', Code04_DifferntName2.nextg[e])
        e = jcast('int', Code04_DifferntName2.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_DifferntName2.tog[e])
            Code04_DifferntName2.siz[u] = jcast('int', jcast('int', jadd(Code04_DifferntName2.siz[u], Code04_DifferntName2.siz[v])))
            if ((Code04_DifferntName2.son[u] == 0) or (Code04_DifferntName2.siz[Code04_DifferntName2.son[u]] < Code04_DifferntName2.siz[v])):
                Code04_DifferntName2.son[u] = jcast('int', v)
            e = jcast('int', Code04_DifferntName2.nextg[e])

    @staticmethod
    def effect(u):
        u = jcast('int', u)
        Code04_DifferntName2.addId(Code04_DifferntName2.dep[u], Code04_DifferntName2.id[u])
        e = jcast('int', Code04_DifferntName2.headg[u])
        while (e > 0):
            Code04_DifferntName2.effect(Code04_DifferntName2.tog[e])
            e = jcast('int', Code04_DifferntName2.nextg[e])

    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        Code04_DifferntName2.removeId(Code04_DifferntName2.dep[u], Code04_DifferntName2.id[u])
        e = jcast('int', Code04_DifferntName2.headg[u])
        while (e > 0):
            Code04_DifferntName2.cancel(Code04_DifferntName2.tog[e])
            e = jcast('int', Code04_DifferntName2.nextg[e])

    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        e = jcast('int', Code04_DifferntName2.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_DifferntName2.tog[e])
            if (v != Code04_DifferntName2.son[u]):
                Code04_DifferntName2.dfs2(v, 0)
            e = jcast('int', Code04_DifferntName2.nextg[e])
        if (Code04_DifferntName2.son[u] != 0):
            Code04_DifferntName2.dfs2(Code04_DifferntName2.son[u], 1)
        Code04_DifferntName2.addId(Code04_DifferntName2.dep[u], Code04_DifferntName2.id[u])
        e = jcast('int', Code04_DifferntName2.headg[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code04_DifferntName2.tog[e])
            if (v != Code04_DifferntName2.son[u]):
                Code04_DifferntName2.effect(v)
            e = jcast('int', Code04_DifferntName2.nextg[e])
        i = jcast('int', Code04_DifferntName2.headq[u])
        while (i > 0):
            jset(Code04_DifferntName2.ans, Code04_DifferntName2.ansiq[i], Code04_DifferntName2.sizeOfDeep(jcast('int', jadd(Code04_DifferntName2.dep[u], Code04_DifferntName2.kq[i]))))
            i = jcast('int', Code04_DifferntName2.nextq[i])
        if (keep == 0):
            Code04_DifferntName2.cancel(u)

    @staticmethod
    def main(args):
        io = Code04_DifferntName2.Kattio(_java_ctor=0)
        Code04_DifferntName2.n = jcast('int', jcall(io, 'nextInt'))
        name = None
        father = 0
        i = jcast('int', 1)
        while (i <= Code04_DifferntName2.n):
            name = jcall(io, 'next')
            father = jcast('int', jcall(io, 'nextInt'))
            jset(Code04_DifferntName2.id, i, Code04_DifferntName2.getNameId(name))
            if (father == 0):
                Code04_DifferntName2.root[i] = jcast('boolean', True)
            else:
                Code04_DifferntName2.addEdge(father, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_DifferntName2.n):
            if Code04_DifferntName2.root[i]:
                Code04_DifferntName2.dfs1(i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code04_DifferntName2.n):
            jcall(Code04_DifferntName2.depSet, 'add', jnew('HashSet'))
            i = jcast('int', (i + 1))
        Code04_DifferntName2.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        node = 0
        k = 0
        while (i <= Code04_DifferntName2.m):
            node = jcast('int', jcall(io, 'nextInt'))
            k = jcast('int', jcall(io, 'nextInt'))
            Code04_DifferntName2.addQuestion(node, i, k)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_DifferntName2.n):
            if Code04_DifferntName2.root[i]:
                Code04_DifferntName2.dfs2(i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_DifferntName2.m):
            jcall(io, 'println', Code04_DifferntName2.ans[i])
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
            except Exception as _java_exception_7:
                if jinstanceof(_java_exception_7, 'Exception'):
                    e = _java_exception_7
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
            raise TypeError("No matching overload for Code04_DifferntName2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_DifferntName2.MAXN = jcast('int', 100001)
Code04_DifferntName2.n = jcast('int', 0)
Code04_DifferntName2.m = jcast('int', 0)
Code04_DifferntName2.nameId = jnew('HashMap')
Code04_DifferntName2.root = jarray('boolean', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.id = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.headg = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.nextg = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.tog = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.cntg = jcast('int', 0)
Code04_DifferntName2.headq = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.nextq = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.ansiq = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.kq = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.cntq = jcast('int', 0)
Code04_DifferntName2.fa = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.siz = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.dep = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.son = jarray('int', [Code04_DifferntName2.MAXN])
Code04_DifferntName2.depSet = jnew('ArrayList')
Code04_DifferntName2.ans = jarray('int', [Code04_DifferntName2.MAXN])

if __name__ == '__main__':
    Code04_DifferntName2.main([])

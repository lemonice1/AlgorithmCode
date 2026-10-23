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

# QTREE7，Python版
# 给定一棵n个节点的树，每个节点有黑白两种颜色，给定初始颜色和点权
# 接下来有q条操作，操作类型如下
# 操作 0 x   : 打印节点x所在的同色连通块中的最大点权
# 操作 1 x   : 翻转节点x的颜色
# 操作 2 x w : 节点x的点权修改为w
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP16580
# 测试链接 : https://www.spoj.com/problems/QTREE7/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_QTREE7_1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'q': 'q', 'color': 'color', 'weight': 'weight', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'parent': 'parent', 'val': 'val', 'vir': 'vir', 'maxv': 'maxv'}
    MAXN = 0
    INF = 0
    n = 0
    q = 0
    # 节点的初始颜色、初始点权
    color = None
    weight = None
    head = None
    nxt = None
    to = None
    cntg = 0
    fa = None
    ls = None
    rs = None
    parent = None
    # 节点x有两个状态
    # val[x] != -INF，说明节点x为黑，此时黑色状态的权值就是点权
    # val[x + n] != -INF，说明节点x为白，此时白色状态的权值就是点权
    # 一定有一个状态是节点点权，另一个状态是-INF
    val = None
    # 保存状态x每个直接虚儿子的完整子树最大值，以及出现次数
    vir = None
    # maxv[x]表示以状态节点x为根的辅助splay汇总的最大点权
    # 包括x自身、x的虚子树、splay中的左右儿子
    maxv = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_QTREE7_1.nxt, ((_java_obj_1 := Code03_QTREE7_1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_QTREE7_1.head[u])
        Code03_QTREE7_1.to[Code03_QTREE7_1.cntg] = jcast('int', v)
        Code03_QTREE7_1.head[u] = jcast('int', Code03_QTREE7_1.cntg)

    @staticmethod
    def insert(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        if (not jcall(Code03_QTREE7_1.vir, 'containsKey', x)):
            jcall(Code03_QTREE7_1.vir, 'put', x, jnew('TreeMap'))
        map = jcall(Code03_QTREE7_1.vir, 'get', x)
        jcall(map, 'put', v, jadd(jcall(map, 'getOrDefault', v, 0), 1))

    @staticmethod
    def remove(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        map = jcall(Code03_QTREE7_1.vir, 'get', x)
        cnt = jcast('int', jcall(map, 'get', v))
        if (cnt == 1):
            jcall(map, 'remove', v)
        else:
            jcall(map, 'put', v, jcast('int', (cnt - 1)))

    @staticmethod
    def getmax(x):
        x = jcast('int', x)
        if ((not jcall(Code03_QTREE7_1.vir, 'containsKey', x)) or jcall(jcall(Code03_QTREE7_1.vir, 'get', x), 'isEmpty')):
            return jcast('int', jcast('int', (-Code03_QTREE7_1.INF)))
        return jcast('int', jcall(jcall(Code03_QTREE7_1.vir, 'get', x), 'lastKey'))

    @staticmethod
    def up(x):
        x = jcast('int', x)
        jset(Code03_QTREE7_1.maxv, x, jstatic('Math', 'max', Code03_QTREE7_1.val[x], jstatic('Math', 'max', Code03_QTREE7_1.getmax(x), jstatic('Math', 'max', Code03_QTREE7_1.maxv[Code03_QTREE7_1.ls[x]], Code03_QTREE7_1.maxv[Code03_QTREE7_1.rs[x]]))))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code03_QTREE7_1.ls[Code03_QTREE7_1.fa[x]] != x) and (Code03_QTREE7_1.rs[Code03_QTREE7_1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code03_QTREE7_1.ls[Code03_QTREE7_1.fa[x]] == x) else 1))

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code03_QTREE7_1.fa[x])
        g = jcast('int', Code03_QTREE7_1.fa[f])
        if (Code03_QTREE7_1.lr(x) == 0):
            Code03_QTREE7_1.ls[f] = jcast('int', Code03_QTREE7_1.rs[x])
            if (Code03_QTREE7_1.ls[f] != 0):
                jset(Code03_QTREE7_1.fa, Code03_QTREE7_1.ls[f], f)
            Code03_QTREE7_1.rs[x] = jcast('int', f)
        else:
            Code03_QTREE7_1.rs[f] = jcast('int', Code03_QTREE7_1.ls[x])
            if (Code03_QTREE7_1.rs[f] != 0):
                jset(Code03_QTREE7_1.fa, Code03_QTREE7_1.rs[f], f)
            Code03_QTREE7_1.ls[x] = jcast('int', f)
        if (not Code03_QTREE7_1.isroot(f)):
            if (Code03_QTREE7_1.lr(f) == 0):
                Code03_QTREE7_1.ls[g] = jcast('int', x)
            else:
                Code03_QTREE7_1.rs[g] = jcast('int', x)
        Code03_QTREE7_1.fa[f] = jcast('int', x)
        Code03_QTREE7_1.fa[x] = jcast('int', g)
        Code03_QTREE7_1.up(f)
        Code03_QTREE7_1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        while (not Code03_QTREE7_1.isroot(x)):
            f = jcast('int', Code03_QTREE7_1.fa[x])
            if (not Code03_QTREE7_1.isroot(f)):
                if (Code03_QTREE7_1.lr(x) == Code03_QTREE7_1.lr(f)):
                    Code03_QTREE7_1.rotate(f)
                else:
                    Code03_QTREE7_1.rotate(x)
            Code03_QTREE7_1.rotate(x)
        Code03_QTREE7_1.up(x)

    # 注意修正虚子树贡献
    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code03_QTREE7_1.splay(x)
            if (Code03_QTREE7_1.rs[x] != 0):
                Code03_QTREE7_1.insert(x, Code03_QTREE7_1.maxv[Code03_QTREE7_1.rs[x]])
            if (y != 0):
                Code03_QTREE7_1.remove(x, Code03_QTREE7_1.maxv[y])
            Code03_QTREE7_1.rs[x] = jcast('int', y)
            Code03_QTREE7_1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code03_QTREE7_1.fa[x])

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code03_QTREE7_1.access(x)
        Code03_QTREE7_1.splay(x)
        while (Code03_QTREE7_1.ls[x] != 0):
            x = jcast('int', Code03_QTREE7_1.ls[x])
        Code03_QTREE7_1.splay(x)
        return jcast('int', x)

    # 连接固定父边(x, f)，x是子，f是父，连接后x作为f的虚儿子
    @staticmethod
    def link(x, f):
        x = jcast('int', x)
        f = jcast('int', f)
        if (f == 0):
            return
        Code03_QTREE7_1.access(f)
        Code03_QTREE7_1.splay(f)
        Code03_QTREE7_1.splay(x)
        Code03_QTREE7_1.fa[x] = jcast('int', f)
        Code03_QTREE7_1.insert(f, Code03_QTREE7_1.maxv[x])
        Code03_QTREE7_1.up(f)

    # 删除固定父边(x, f)，x是子，f是父
    @staticmethod
    def cut(x, f):
        x = jcast('int', x)
        f = jcast('int', f)
        Code03_QTREE7_1.access(x)
        Code03_QTREE7_1.splay(x)
        if (f != 0):
            left = jcast('int', Code03_QTREE7_1.ls[x])
            Code03_QTREE7_1.fa[left] = jcast('int', 0)
            Code03_QTREE7_1.ls[x] = jcast('int', 0)
            Code03_QTREE7_1.up(x)

    @staticmethod
    def query(x):
        x = jcast('int', x)
        xs = jcast('int', (x if (Code03_QTREE7_1.val[x] != jcast('int', (-Code03_QTREE7_1.INF))) else jcast('int', jadd(x, Code03_QTREE7_1.n))))
        ys = jcast('int', Code03_QTREE7_1.findroot(xs))
        return jcast('int', (Code03_QTREE7_1.maxv[ys] if (Code03_QTREE7_1.val[ys] != jcast('int', (-Code03_QTREE7_1.INF))) else Code03_QTREE7_1.maxv[Code03_QTREE7_1.rs[ys]]))

    @staticmethod
    def reverseColor(x):
        x = jcast('int', x)
        pre = jcast('int', (x if (Code03_QTREE7_1.val[x] != jcast('int', (-Code03_QTREE7_1.INF))) else jcast('int', jadd(x, Code03_QTREE7_1.n))))
        cur = jcast('int', (jcast('int', jadd(pre, Code03_QTREE7_1.n)) if (pre <= Code03_QTREE7_1.n) else jcast('int', (pre - Code03_QTREE7_1.n))))
        Code03_QTREE7_1.cut(pre, Code03_QTREE7_1.parent[pre])
        Code03_QTREE7_1.val[cur] = jcast('int', Code03_QTREE7_1.val[pre])
        Code03_QTREE7_1.val[pre] = jcast('int', jcast('int', (-Code03_QTREE7_1.INF)))
        Code03_QTREE7_1.link(cur, Code03_QTREE7_1.parent[cur])

    @staticmethod
    def updateValue(x, w):
        x = jcast('int', x)
        w = jcast('int', w)
        cur = jcast('int', (x if (Code03_QTREE7_1.val[x] != jcast('int', (-Code03_QTREE7_1.INF))) else jcast('int', jadd(x, Code03_QTREE7_1.n))))
        Code03_QTREE7_1.access(cur)
        Code03_QTREE7_1.splay(cur)
        Code03_QTREE7_1.val[cur] = jcast('int', w)
        Code03_QTREE7_1.up(cur)

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        if (f != 0):
            Code03_QTREE7_1.parent[u] = jcast('int', f)
            Code03_QTREE7_1.parent[jcast('int', jadd(u, Code03_QTREE7_1.n))] = jcast('int', jcast('int', jadd(f, Code03_QTREE7_1.n)))
        e = jcast('int', Code03_QTREE7_1.head[u])
        while (e != 0):
            v = jcast('int', Code03_QTREE7_1.to[e])
            if (v != f):
                Code03_QTREE7_1.dfs(v, u)
                cur = jcast('int', (v if (Code03_QTREE7_1.color[v] == 0) else jcast('int', jadd(v, Code03_QTREE7_1.n))))
                Code03_QTREE7_1.link(cur, Code03_QTREE7_1.parent[cur])
            e = jcast('int', Code03_QTREE7_1.nxt[e])

    @staticmethod
    def prepare():
        Code03_QTREE7_1.maxv[0] = jcast('int', jcast('int', (-Code03_QTREE7_1.INF)))
        # 根据初始颜色，设置黑白状态的贡献和最大值
        i = jcast('int', 1)
        while (i <= Code03_QTREE7_1.n):
            if (Code03_QTREE7_1.color[i] == 0):
                jset(Code03_QTREE7_1.val, i, jset(Code03_QTREE7_1.maxv, i, Code03_QTREE7_1.weight[i]))
                jset(Code03_QTREE7_1.val, jcast('int', jadd(i, Code03_QTREE7_1.n)), jset(Code03_QTREE7_1.maxv, jcast('int', jadd(i, Code03_QTREE7_1.n)), jcast('int', (-Code03_QTREE7_1.INF))))
            else:
                jset(Code03_QTREE7_1.val, i, jset(Code03_QTREE7_1.maxv, i, jcast('int', (-Code03_QTREE7_1.INF))))
                jset(Code03_QTREE7_1.val, jcast('int', jadd(i, Code03_QTREE7_1.n)), jset(Code03_QTREE7_1.maxv, jcast('int', jadd(i, Code03_QTREE7_1.n)), Code03_QTREE7_1.weight[i]))
            i = jcast('int', (i + 1))
        Code03_QTREE7_1.dfs(1, 0)

    @staticmethod
    def main(args):
        in_ = Code03_QTREE7_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_QTREE7_1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_QTREE7_1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_QTREE7_1.addEdge(u, v)
            Code03_QTREE7_1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_QTREE7_1.n):
            jset(Code03_QTREE7_1.color, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_QTREE7_1.n):
            jset(Code03_QTREE7_1.weight, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_QTREE7_1.prepare()
        Code03_QTREE7_1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        x = 0
        w = 0
        while (i <= Code03_QTREE7_1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                jcall(out, 'println', Code03_QTREE7_1.query(x))
            else:
                if (op == 1):
                    Code03_QTREE7_1.reverseColor(x)
                else:
                    w = jcast('int', jcall(in_, 'nextInt'))
                    Code03_QTREE7_1.updateValue(x, w)
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
                val = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (val * 10)), c)) - jchar('0'))))
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
            raise TypeError("No matching overload for Code03_QTREE7_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_QTREE7_1.MAXN = jcast('int', 200001)
Code03_QTREE7_1.INF = jcast('int', 1000000001)
Code03_QTREE7_1.n = jcast('int', 0)
Code03_QTREE7_1.q = jcast('int', 0)
Code03_QTREE7_1.color = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.weight = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.head = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.nxt = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.to = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.cntg = jcast('int', 0)
Code03_QTREE7_1.fa = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.ls = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.rs = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.parent = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.val = jarray('int', [Code03_QTREE7_1.MAXN])
Code03_QTREE7_1.vir = jnew('HashMap')
Code03_QTREE7_1.maxv = jarray('int', [Code03_QTREE7_1.MAXN])

if __name__ == '__main__':
    Code03_QTREE7_1.main([])

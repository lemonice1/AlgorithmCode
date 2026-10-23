# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 首都，Python版
# 初始时有n个互不连通的点，然后有m条操作，操作类型如下
# 操作 A x y : 点x和点y之间连一条边，保证之前x和y是不连通的
# 操作 Q x   : 打印点x所在连通区的重心编号
# 操作 Xor   : 打印当前所有连通区，重心编号的异或和
# 本题的一个连通区就是一棵树，重心是到其他点的距离总和最小的点
# 为了保证重心唯一，本题规定，如果有多个重心，选择编号最小的点作为重心
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4299
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Capital1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'father': 'father', 'vir': 'vir', 'sum': 'sum', 'xorsum': 'xorsum'}
    MAXN = 0
    n = 0
    m = 0
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # 并查集维护连通性，连通块的代表节点就是连通块的重心
    father = None
    vir = None
    sum = None
    xorsum = 0
    # 查询x所在连通块当前的重心
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code05_Capital1.father[x]):
            jset(Code05_Capital1.father, x, Code05_Capital1.find(Code05_Capital1.father[x]))
        return jcast('int', Code05_Capital1.father[x])

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code05_Capital1.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(Code05_Capital1.sum[Code05_Capital1.ls[x]], Code05_Capital1.sum[Code05_Capital1.rs[x]])), Code05_Capital1.vir[x])), 1)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code05_Capital1.ls[Code05_Capital1.fa[x]] != x) and (Code05_Capital1.rs[Code05_Capital1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code05_Capital1.ls[Code05_Capital1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code05_Capital1.ls[x])
            Code05_Capital1.ls[x] = jcast('int', Code05_Capital1.rs[x])
            Code05_Capital1.rs[x] = jcast('int', tmp)
            Code05_Capital1.rev[x] = jcast('boolean', (not Code05_Capital1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code05_Capital1.rev[x]:
            Code05_Capital1.reverse(Code05_Capital1.ls[x])
            Code05_Capital1.reverse(Code05_Capital1.rs[x])
            Code05_Capital1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code05_Capital1.fa[x])
        g = jcast('int', Code05_Capital1.fa[f])
        if (Code05_Capital1.lr(x) == 0):
            Code05_Capital1.ls[f] = jcast('int', Code05_Capital1.rs[x])
            if (Code05_Capital1.ls[f] != 0):
                jset(Code05_Capital1.fa, Code05_Capital1.ls[f], f)
            Code05_Capital1.rs[x] = jcast('int', f)
        else:
            Code05_Capital1.rs[f] = jcast('int', Code05_Capital1.ls[x])
            if (Code05_Capital1.rs[f] != 0):
                jset(Code05_Capital1.fa, Code05_Capital1.rs[f], f)
            Code05_Capital1.ls[x] = jcast('int', f)
        if (not Code05_Capital1.isroot(f)):
            if (Code05_Capital1.lr(f) == 0):
                Code05_Capital1.ls[g] = jcast('int', x)
            else:
                Code05_Capital1.rs[g] = jcast('int', x)
        Code05_Capital1.fa[f] = jcast('int', x)
        Code05_Capital1.fa[x] = jcast('int', g)
        Code05_Capital1.up(f)
        Code05_Capital1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code05_Capital1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code05_Capital1.isroot(y)):
            jset(Code05_Capital1.sta, (siz := jcast('int', (siz + (1)))), Code05_Capital1.fa[y])
            y = jcast('int', Code05_Capital1.fa[y])
        while (siz != 0):
            Code05_Capital1.down(Code05_Capital1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code05_Capital1.isroot(x)):
            f = jcast('int', Code05_Capital1.fa[x])
            if (not Code05_Capital1.isroot(f)):
                if (Code05_Capital1.lr(x) == Code05_Capital1.lr(f)):
                    Code05_Capital1.rotate(f)
                else:
                    Code05_Capital1.rotate(x)
            Code05_Capital1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code05_Capital1.splay(x)
            Code05_Capital1.vir[x] = jcast('int', jcast('int', jadd(Code05_Capital1.vir[x], Code05_Capital1.sum[Code05_Capital1.rs[x]])))
            Code05_Capital1.vir[x] = jcast('int', jcast('int', (Code05_Capital1.vir[x] - Code05_Capital1.sum[y])))
            Code05_Capital1.rs[x] = jcast('int', y)
            Code05_Capital1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code05_Capital1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code05_Capital1.access(x)
        Code05_Capital1.splay(x)
        Code05_Capital1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code05_Capital1.access(x)
        Code05_Capital1.splay(x)
        Code05_Capital1.down(x)
        while (Code05_Capital1.ls[x] != 0):
            x = jcast('int', Code05_Capital1.ls[x])
            Code05_Capital1.down(x)
        Code05_Capital1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_Capital1.makeroot(x)
        Code05_Capital1.access(y)
        Code05_Capital1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_Capital1.makeroot(x)
        if (Code05_Capital1.findroot(y) != x):
            Code05_Capital1.access(y)
            Code05_Capital1.splay(y)
            Code05_Capital1.fa[x] = jcast('int', y)
            Code05_Capital1.vir[y] = jcast('int', jcast('int', jadd(Code05_Capital1.vir[y], Code05_Capital1.sum[x])))
            Code05_Capital1.up(y)

    # 根据两个旧重心a和b，寻找并返回新重心
    @staticmethod
    def newCenter(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        # 打通两个旧重心的路径，新重心一定在这条路径上
        Code05_Capital1.split(a, b)
        half = jcast('int', jcast('int', (Code05_Capital1.sum[b] >> (1 & 31))))
        lpass = jcast('int', 0)
        rpass = jcast('int', 0)
        ans = jcast('int', jcast('int', jadd(Code05_Capital1.n, 1)))
        cur = jcast('int', b)
        while (cur != 0):
            # 先要处理翻转标记，才能正确的向左或者向右移动
            Code05_Capital1.down(cur)
            lsiz = jcast('int', jcast('int', jadd(Code05_Capital1.sum[Code05_Capital1.ls[cur]], lpass)))
            rsiz = jcast('int', jcast('int', jadd(Code05_Capital1.sum[Code05_Capital1.rs[cur]], rpass)))
            # 课上重点讲解了，只需要检查路径的两个方向的子树即可
            if ((lsiz <= half) and (rsiz <= half)):
                ans = jcast('int', jstatic('Math', 'min', ans, cur))
            # 向节点数量较多的一侧移动
            if (lsiz < rsiz):
                lpass = jcast('int', jcast('int', jadd(lpass, jcast('int', jadd(jcast('int', jadd(Code05_Capital1.sum[Code05_Capital1.ls[cur]], Code05_Capital1.vir[cur])), 1)))))
                cur = jcast('int', Code05_Capital1.rs[cur])
            else:
                rpass = jcast('int', jcast('int', jadd(rpass, jcast('int', jadd(jcast('int', jadd(Code05_Capital1.sum[Code05_Capital1.rs[cur]], Code05_Capital1.vir[cur])), 1)))))
                cur = jcast('int', Code05_Capital1.ls[cur])
        # 新重心旋转上去，保证平衡性
        Code05_Capital1.splay(ans)
        return jcast('int', ans)

    @staticmethod
    def road(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', Code05_Capital1.find(x))
        b = jcast('int', Code05_Capital1.find(y))
        Code05_Capital1.link(x, y)
        cur = jcast('int', Code05_Capital1.newCenter(a, b))
        jset(Code05_Capital1.father, cur, jset(Code05_Capital1.father, a, jset(Code05_Capital1.father, b, cur)))
        Code05_Capital1.xorsum = jcast('int', jcast('int', (Code05_Capital1.xorsum ^ jcast('int', (jcast('int', (a ^ b)) ^ cur)))))

    @staticmethod
    def main(args):
        in_ = Code05_Capital1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Capital1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Capital1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Capital1.n):
            Code05_Capital1.sum[i] = jcast('int', 1)
            Code05_Capital1.father[i] = jcast('int', i)
            Code05_Capital1.xorsum = jcast('int', jcast('int', (Code05_Capital1.xorsum ^ i)))
            i = jcast('int', (i + 1))
        op = None
        x = 0
        y = 0
        i = jcast('int', 1)
        while (i <= Code05_Capital1.m):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'A'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code05_Capital1.road(x, y)
            else:
                if jcall(op, 'equals', 'Q'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', Code05_Capital1.find(x))
                else:
                    jcall(out, 'println', Code05_Capital1.xorsum)
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
            return jcast('int', self.buffer[((_java_obj_2 := self), (_java_key_3 := 'ptr'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

        def nextString(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            if (c == jcast('int', (-1))):
                return None
            sb = jnew('StringBuilder')
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('int', self.readByte())
            return jcall(sb, 'toString')

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
            raise TypeError("No matching overload for Code05_Capital1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Capital1.MAXN = jcast('int', 100001)
Code05_Capital1.n = jcast('int', 0)
Code05_Capital1.m = jcast('int', 0)
Code05_Capital1.fa = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.ls = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.rs = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.rev = jarray('boolean', [Code05_Capital1.MAXN])
Code05_Capital1.sta = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.father = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.vir = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.sum = jarray('int', [Code05_Capital1.MAXN])
Code05_Capital1.xorsum = jcast('int', 0)

if __name__ == '__main__':
    Code05_Capital1.main([])

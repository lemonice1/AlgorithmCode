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

# 洞穴勘测，Python版
# 一共n个点，初始时没有任何边，任意时刻图都是森林，一共m条操作，类型如下
# 操作 Connect x y : 点x和点y之间增加直接边，保证原来不存在这条直接边
# 操作 Destroy x y : 删除点x和点y之间的直接边，保证原来存在这条直接边
# 操作 Query x y   : 查询点x和点y之间是否连通，打印 Yes 或 No
# 1 <= n <= 10^4
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2147
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_CaveSurvey2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev'}
    MAXN = 0
    n = 0
    m = 0
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code03_CaveSurvey2.ls[Code03_CaveSurvey2.fa[x]] != x) and (Code03_CaveSurvey2.rs[Code03_CaveSurvey2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code03_CaveSurvey2.ls[Code03_CaveSurvey2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code03_CaveSurvey2.ls[x])
            Code03_CaveSurvey2.ls[x] = jcast('int', Code03_CaveSurvey2.rs[x])
            Code03_CaveSurvey2.rs[x] = jcast('int', tmp)
            Code03_CaveSurvey2.rev[x] = jcast('boolean', (not Code03_CaveSurvey2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code03_CaveSurvey2.rev[x]:
            Code03_CaveSurvey2.reverse(Code03_CaveSurvey2.ls[x])
            Code03_CaveSurvey2.reverse(Code03_CaveSurvey2.rs[x])
            Code03_CaveSurvey2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code03_CaveSurvey2.fa[x])
        g = jcast('int', Code03_CaveSurvey2.fa[f])
        if (Code03_CaveSurvey2.lr(x) == 0):
            Code03_CaveSurvey2.ls[f] = jcast('int', Code03_CaveSurvey2.rs[x])
            if (Code03_CaveSurvey2.ls[f] != 0):
                jset(Code03_CaveSurvey2.fa, Code03_CaveSurvey2.ls[f], f)
            Code03_CaveSurvey2.rs[x] = jcast('int', f)
        else:
            Code03_CaveSurvey2.rs[f] = jcast('int', Code03_CaveSurvey2.ls[x])
            if (Code03_CaveSurvey2.rs[f] != 0):
                jset(Code03_CaveSurvey2.fa, Code03_CaveSurvey2.rs[f], f)
            Code03_CaveSurvey2.ls[x] = jcast('int', f)
        if (not Code03_CaveSurvey2.isroot(f)):
            if (Code03_CaveSurvey2.lr(f) == 0):
                Code03_CaveSurvey2.ls[g] = jcast('int', x)
            else:
                Code03_CaveSurvey2.rs[g] = jcast('int', x)
        Code03_CaveSurvey2.fa[f] = jcast('int', x)
        Code03_CaveSurvey2.fa[x] = jcast('int', g)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code03_CaveSurvey2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code03_CaveSurvey2.isroot(y)):
            jset(Code03_CaveSurvey2.sta, (siz := jcast('int', (siz + (1)))), Code03_CaveSurvey2.fa[y])
            y = jcast('int', Code03_CaveSurvey2.fa[y])
        while (siz != 0):
            Code03_CaveSurvey2.down(Code03_CaveSurvey2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code03_CaveSurvey2.isroot(x)):
            f = jcast('int', Code03_CaveSurvey2.fa[x])
            if (not Code03_CaveSurvey2.isroot(f)):
                if (Code03_CaveSurvey2.lr(x) == Code03_CaveSurvey2.lr(f)):
                    Code03_CaveSurvey2.rotate(f)
                else:
                    Code03_CaveSurvey2.rotate(x)
            Code03_CaveSurvey2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code03_CaveSurvey2.splay(x)
            Code03_CaveSurvey2.rs[x] = jcast('int', y)
            y = jcast('int', x)
            x = jcast('int', Code03_CaveSurvey2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code03_CaveSurvey2.access(x)
        Code03_CaveSurvey2.splay(x)
        Code03_CaveSurvey2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code03_CaveSurvey2.access(x)
        Code03_CaveSurvey2.splay(x)
        Code03_CaveSurvey2.down(x)
        while (Code03_CaveSurvey2.ls[x] != 0):
            x = jcast('int', Code03_CaveSurvey2.ls[x])
            Code03_CaveSurvey2.down(x)
        Code03_CaveSurvey2.splay(x)
        return jcast('int', x)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_CaveSurvey2.makeroot(x)
        if (Code03_CaveSurvey2.findroot(y) != x):
            Code03_CaveSurvey2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_CaveSurvey2.makeroot(x)
        if ((((Code03_CaveSurvey2.findroot(y) == x) and (Code03_CaveSurvey2.fa[y] == x)) and (Code03_CaveSurvey2.ls[y] == 0)) and (Code03_CaveSurvey2.rs[x] == y)):
            jset(Code03_CaveSurvey2.fa, y, jset(Code03_CaveSurvey2.rs, x, 0))

    @staticmethod
    def main(args):
        in_ = Code03_CaveSurvey2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_CaveSurvey2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_CaveSurvey2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code03_CaveSurvey2.m):
            op = jcall(in_, 'nextString')
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if jcall(op, 'equals', 'Connect'):
                Code03_CaveSurvey2.link(x, y)
            else:
                if jcall(op, 'equals', 'Destroy'):
                    Code03_CaveSurvey2.cut(x, y)
                else:
                    if (Code03_CaveSurvey2.findroot(x) == Code03_CaveSurvey2.findroot(y)):
                        jcall(out, 'println', 'Yes')
                    else:
                        jcall(out, 'println', 'No')
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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_CaveSurvey2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CaveSurvey2.MAXN = jcast('int', 10001)
Code03_CaveSurvey2.n = jcast('int', 0)
Code03_CaveSurvey2.m = jcast('int', 0)
Code03_CaveSurvey2.fa = jarray('int', [Code03_CaveSurvey2.MAXN])
Code03_CaveSurvey2.ls = jarray('int', [Code03_CaveSurvey2.MAXN])
Code03_CaveSurvey2.rs = jarray('int', [Code03_CaveSurvey2.MAXN])
Code03_CaveSurvey2.sta = jarray('int', [Code03_CaveSurvey2.MAXN])
Code03_CaveSurvey2.rev = jarray('boolean', [Code03_CaveSurvey2.MAXN])

if __name__ == '__main__':
    Code03_CaveSurvey2.main([])

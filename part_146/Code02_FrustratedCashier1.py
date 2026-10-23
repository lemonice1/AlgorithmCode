# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 郁闷的出纳员(Python版)
# 最低薪水为limit，一旦员工薪水低于limit，员工会离职，实现如下四种操作
# I x : 新来员工初始薪水是x，如果x低于limit，该员工不会入职当然也不算离职
# A x : 所有员工的薪水都加上x
# S x : 所有员工的薪水都减去x，一旦有员工低于limit那么就会离职
# F x : 查询第x多的工资，如果x大于当前员工数量，打印-1
# 所有操作完成后，打印有多少员工在操作期间离开了公司
# 测试链接 : https://www.luogu.com.cn/problem/P1486
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_FrustratedCashier1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size', 'limit': 'limit', 'change': 'change', 'enter': 'enter'}
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    father = None
    left = None
    right = None
    size = None
    limit = 0
    change = 0
    enter = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_FrustratedCashier1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.left[i]], Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (Code02_FrustratedCashier1.right[Code02_FrustratedCashier1.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', Code02_FrustratedCashier1.father[i])
        g = jcast('int', Code02_FrustratedCashier1.father[f])
        soni = jcast('int', Code02_FrustratedCashier1.lr(i))
        sonf = jcast('int', Code02_FrustratedCashier1.lr(f))
        if (soni == 1):
            Code02_FrustratedCashier1.right[f] = jcast('int', Code02_FrustratedCashier1.left[i])
            if (Code02_FrustratedCashier1.right[f] != 0):
                jset(Code02_FrustratedCashier1.father, Code02_FrustratedCashier1.right[f], f)
            Code02_FrustratedCashier1.left[i] = jcast('int', f)
        else:
            Code02_FrustratedCashier1.left[f] = jcast('int', Code02_FrustratedCashier1.right[i])
            if (Code02_FrustratedCashier1.left[f] != 0):
                jset(Code02_FrustratedCashier1.father, Code02_FrustratedCashier1.left[f], f)
            Code02_FrustratedCashier1.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                Code02_FrustratedCashier1.right[g] = jcast('int', i)
            else:
                Code02_FrustratedCashier1.left[g] = jcast('int', i)
        Code02_FrustratedCashier1.father[f] = jcast('int', i)
        Code02_FrustratedCashier1.father[i] = jcast('int', g)
        Code02_FrustratedCashier1.up(f)
        Code02_FrustratedCashier1.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', Code02_FrustratedCashier1.father[i])
        g = jcast('int', Code02_FrustratedCashier1.father[f])
        while (f != goal):
            if (g != goal):
                if (Code02_FrustratedCashier1.lr(i) == Code02_FrustratedCashier1.lr(f)):
                    Code02_FrustratedCashier1.rotate(f)
                else:
                    Code02_FrustratedCashier1.rotate(i)
            Code02_FrustratedCashier1.rotate(i)
            f = jcast('int', Code02_FrustratedCashier1.father[i])
            g = jcast('int', Code02_FrustratedCashier1.father[f])
        if (goal == 0):
            Code02_FrustratedCashier1.head = jcast('int', i)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        jset(Code02_FrustratedCashier1.key, ((_java_obj_1 := Code02_FrustratedCashier1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.cnt] = jcast('int', 1)
        if (Code02_FrustratedCashier1.head == 0):
            Code02_FrustratedCashier1.head = jcast('int', Code02_FrustratedCashier1.cnt)
        else:
            f = jcast('int', 0)
            i = jcast('int', Code02_FrustratedCashier1.head)
            son = jcast('int', 0)
            while (i != 0):
                f = jcast('int', i)
                if (Code02_FrustratedCashier1.key[i] <= num):
                    son = jcast('int', 1)
                    i = jcast('int', Code02_FrustratedCashier1.right[i])
                else:
                    son = jcast('int', 0)
                    i = jcast('int', Code02_FrustratedCashier1.left[i])
            if (son == 1):
                Code02_FrustratedCashier1.right[f] = jcast('int', Code02_FrustratedCashier1.cnt)
            else:
                Code02_FrustratedCashier1.left[f] = jcast('int', Code02_FrustratedCashier1.cnt)
            Code02_FrustratedCashier1.father[Code02_FrustratedCashier1.cnt] = jcast('int', f)
            Code02_FrustratedCashier1.splay(Code02_FrustratedCashier1.cnt, 0)

    @staticmethod
    def index(x):
        x = jcast('int', x)
        i = jcast('int', Code02_FrustratedCashier1.head)
        last = jcast('int', Code02_FrustratedCashier1.head)
        while (i != 0):
            last = jcast('int', i)
            if (Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.left[i]] >= x):
                i = jcast('int', Code02_FrustratedCashier1.left[i])
            else:
                if (jcast('int', jadd(Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.left[i]], 1)) < x):
                    x = jcast('int', jcast('int', (x - jcast('int', jadd(Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.left[i]], 1)))))
                    i = jcast('int', Code02_FrustratedCashier1.right[i])
                else:
                    i = jcast('int', 0)
        Code02_FrustratedCashier1.splay(last, 0)
        return jcast('int', Code02_FrustratedCashier1.key[last])

    @staticmethod
    def departure():
        num = jcast('int', jcast('int', (jcast('int', (Code02_FrustratedCashier1.limit - Code02_FrustratedCashier1.change)) - 1)))
        i = jcast('int', Code02_FrustratedCashier1.head)
        ans = jcast('int', 0)
        while (i != 0):
            if (Code02_FrustratedCashier1.key[i] > num):
                ans = jcast('int', i)
                i = jcast('int', Code02_FrustratedCashier1.left[i])
            else:
                i = jcast('int', Code02_FrustratedCashier1.right[i])
        if (ans == 0):
            Code02_FrustratedCashier1.head = jcast('int', 0)
        else:
            Code02_FrustratedCashier1.splay(ans, 0)
            Code02_FrustratedCashier1.left[Code02_FrustratedCashier1.head] = jcast('int', 0)
            Code02_FrustratedCashier1.up(Code02_FrustratedCashier1.head)

    @staticmethod
    def main(args):
        io = Code02_FrustratedCashier1.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        Code02_FrustratedCashier1.limit = jcast('int', jcall(io, 'nextInt'))
        op = None
        x = 0
        i = jcast('int', 1)
        while (i <= n):
            op = jcall(io, 'next')
            x = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'I'):
                if (x >= Code02_FrustratedCashier1.limit):
                    Code02_FrustratedCashier1.enter = jcast('int', (Code02_FrustratedCashier1.enter + 1))
                    Code02_FrustratedCashier1.add(jcast('int', (x - Code02_FrustratedCashier1.change)))
            else:
                if jcall(op, 'equals', 'A'):
                    Code02_FrustratedCashier1.change = jcast('int', jcast('int', jadd(Code02_FrustratedCashier1.change, x)))
                else:
                    if jcall(op, 'equals', 'S'):
                        Code02_FrustratedCashier1.change = jcast('int', jcast('int', (Code02_FrustratedCashier1.change - x)))
                        Code02_FrustratedCashier1.departure()
                    else:
                        if (x > Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.head]):
                            jcall(io, 'println', jcast('int', (-1)))
                        else:
                            jcall(io, 'println', jcast('int', jadd(Code02_FrustratedCashier1.index(jcast('int', jadd(jcast('int', (Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.head] - x)), 1))), Code02_FrustratedCashier1.change)))
            i = jcast('int', (i + 1))
        jcall(io, 'println', jcast('int', (Code02_FrustratedCashier1.enter - Code02_FrustratedCashier1.size[Code02_FrustratedCashier1.head])))
        jcall(io, 'flush')
        jcall(io, 'close')

    # Kattio 与 StreamTokenizer 接口均由 Python 实现，按输入格式选择，不沿用原语言的速度比较
    # 输入包含特殊格式时，可使用本类先读取字符串，再选择 int 或 float 解析
    # Python 输入输出参考：https://docs.python.org/3/library/io.html
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
            except Exception as _java_exception_4:
                if jinstanceof(_java_exception_4, 'Exception'):
                    e = _java_exception_4
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
            raise TypeError("No matching overload for Code02_FrustratedCashier1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_FrustratedCashier1.MAXN = jcast('int', 300001)
Code02_FrustratedCashier1.head = jcast('int', 0)
Code02_FrustratedCashier1.cnt = jcast('int', 0)
Code02_FrustratedCashier1.key = jarray('int', [Code02_FrustratedCashier1.MAXN])
Code02_FrustratedCashier1.father = jarray('int', [Code02_FrustratedCashier1.MAXN])
Code02_FrustratedCashier1.left = jarray('int', [Code02_FrustratedCashier1.MAXN])
Code02_FrustratedCashier1.right = jarray('int', [Code02_FrustratedCashier1.MAXN])
Code02_FrustratedCashier1.size = jarray('int', [Code02_FrustratedCashier1.MAXN])
Code02_FrustratedCashier1.limit = jcast('int', 0)
Code02_FrustratedCashier1.change = jcast('int', 0)
Code02_FrustratedCashier1.enter = jcast('int', 0)

if __name__ == '__main__':
    Code02_FrustratedCashier1.main([])

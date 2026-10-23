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

# 书架(Python版)
# 给定一个长度为n的排列，由数字1、2、3...n组成，实现如下五种操作
# Top s      : 数字s移动到最左边
# Bottom s   : 数字s移动到最右边
# Insert s t : 数字s位置假设为rank，现在移动到rank+t位置
# Ask s      : 查询数字s左边有多少数字
# Query s    : 查询从左往右第s位的数字
# 所有操作保证都是合法的
# 测试链接 : https://www.luogu.com.cn/problem/P2596
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Bookcase1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'num': 'num', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size', 'pos': 'pos', 'n': 'n', 'm': 'm'}
    MAXN = 0
    head = 0
    cnt = 0
    num = None
    father = None
    left = None
    right = None
    size = None
    # pos[num] : 数字num所在节点的编号
    pos = None
    n = 0
    m = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_Bookcase1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_Bookcase1.size[Code04_Bookcase1.left[i]], Code04_Bookcase1.size[Code04_Bookcase1.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (Code04_Bookcase1.right[Code04_Bookcase1.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', Code04_Bookcase1.father[i])
        g = jcast('int', Code04_Bookcase1.father[f])
        soni = jcast('int', Code04_Bookcase1.lr(i))
        sonf = jcast('int', Code04_Bookcase1.lr(f))
        if (soni == 1):
            Code04_Bookcase1.right[f] = jcast('int', Code04_Bookcase1.left[i])
            if (Code04_Bookcase1.right[f] != 0):
                jset(Code04_Bookcase1.father, Code04_Bookcase1.right[f], f)
            Code04_Bookcase1.left[i] = jcast('int', f)
        else:
            Code04_Bookcase1.left[f] = jcast('int', Code04_Bookcase1.right[i])
            if (Code04_Bookcase1.left[f] != 0):
                jset(Code04_Bookcase1.father, Code04_Bookcase1.left[f], f)
            Code04_Bookcase1.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                Code04_Bookcase1.right[g] = jcast('int', i)
            else:
                Code04_Bookcase1.left[g] = jcast('int', i)
        Code04_Bookcase1.father[f] = jcast('int', i)
        Code04_Bookcase1.father[i] = jcast('int', g)
        Code04_Bookcase1.up(f)
        Code04_Bookcase1.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', Code04_Bookcase1.father[i])
        g = jcast('int', Code04_Bookcase1.father[f])
        while (f != goal):
            if (g != goal):
                if (Code04_Bookcase1.lr(i) == Code04_Bookcase1.lr(f)):
                    Code04_Bookcase1.rotate(f)
                else:
                    Code04_Bookcase1.rotate(i)
            Code04_Bookcase1.rotate(i)
            f = jcast('int', Code04_Bookcase1.father[i])
            g = jcast('int', Code04_Bookcase1.father[f])
        if (goal == 0):
            Code04_Bookcase1.head = jcast('int', i)

    # 返回中序排名为rank的节点编号
    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', Code04_Bookcase1.head)
        while (i != 0):
            if (jcast('int', jadd(Code04_Bookcase1.size[Code04_Bookcase1.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (Code04_Bookcase1.size[Code04_Bookcase1.left[i]] >= rank):
                    i = jcast('int', Code04_Bookcase1.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(Code04_Bookcase1.size[Code04_Bookcase1.left[i]], 1)))))
                    i = jcast('int', Code04_Bookcase1.right[i])
        return jcast('int', 0)

    @staticmethod
    def add(s):
        s = jcast('int', s)
        jset(Code04_Bookcase1.num, ((_java_obj_1 := Code04_Bookcase1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], s)
        Code04_Bookcase1.pos[s] = jcast('int', Code04_Bookcase1.cnt)
        Code04_Bookcase1.size[Code04_Bookcase1.cnt] = jcast('int', 1)
        Code04_Bookcase1.father[Code04_Bookcase1.cnt] = jcast('int', Code04_Bookcase1.head)
        Code04_Bookcase1.right[Code04_Bookcase1.head] = jcast('int', Code04_Bookcase1.cnt)
        Code04_Bookcase1.splay(Code04_Bookcase1.cnt, 0)

    @staticmethod
    def ask(s):
        s = jcast('int', s)
        i = jcast('int', Code04_Bookcase1.pos[s])
        Code04_Bookcase1.splay(i, 0)
        return jcast('int', Code04_Bookcase1.size[Code04_Bookcase1.left[i]])

    @staticmethod
    def query(s):
        s = jcast('int', s)
        i = jcast('int', Code04_Bookcase1.find(s))
        Code04_Bookcase1.splay(i, 0)
        return jcast('int', Code04_Bookcase1.num[i])

    # 中序排名为a的节点，移动到中序排名为b的位置
    # 注意a不会是1和n位置，b也如此
    # 因为1位置和n位置提前加入了预备值，永远不会修改
    @staticmethod
    def move(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        l = jcast('int', Code04_Bookcase1.find(jcast('int', (a - 1))))
        r = jcast('int', Code04_Bookcase1.find(jcast('int', jadd(a, 1))))
        Code04_Bookcase1.splay(l, 0)
        Code04_Bookcase1.splay(r, l)
        i = jcast('int', Code04_Bookcase1.left[r])
        Code04_Bookcase1.left[r] = jcast('int', 0)
        Code04_Bookcase1.up(r)
        Code04_Bookcase1.up(l)
        l = jcast('int', Code04_Bookcase1.find(jcast('int', (b - 1))))
        r = jcast('int', Code04_Bookcase1.find(b))
        Code04_Bookcase1.splay(l, 0)
        Code04_Bookcase1.splay(r, l)
        Code04_Bookcase1.left[r] = jcast('int', i)
        Code04_Bookcase1.father[i] = jcast('int', r)
        Code04_Bookcase1.up(r)
        Code04_Bookcase1.up(l)

    @staticmethod
    def main(args):
        io = Code04_Bookcase1.Kattio(_java_ctor=0)
        Code04_Bookcase1.n = jcast('int', jcall(io, 'nextInt'))
        Code04_Bookcase1.m = jcast('int', jcall(io, 'nextInt'))
        Code04_Bookcase1.add(0)
        i = jcast('int', 1)
        while (i <= Code04_Bookcase1.n):
            Code04_Bookcase1.add(jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_Bookcase1.add(jcast('int', jadd(Code04_Bookcase1.n, 1)))
        # 注意在最左插入了0，最右插入了n+1，作为准备值，所以一共n+2个数
        # 下面操作时，不要忘了最左是0，最右是n+1，并且永远不修改
        Code04_Bookcase1.n = jcast('int', jcast('int', jadd(Code04_Bookcase1.n, 2)))
        op = None
        i = jcast('int', 1)
        s = 0
        t = 0
        rank = 0
        while (i <= Code04_Bookcase1.m):
            op = jcall(io, 'next')
            s = jcast('int', jcall(io, 'nextInt'))
            rank = jcast('int', jcast('int', jadd(Code04_Bookcase1.ask(s), 1)))
            if jcall(op, 'equals', 'Top'):
                # 因为有最左侧的准备值，所以开头是中序排名2的位置
                Code04_Bookcase1.move(rank, 2)
            else:
                if jcall(op, 'equals', 'Bottom'):
                    # 因为有最右侧的准备值，所以结尾是中序排名n-1的位置
                    Code04_Bookcase1.move(rank, jcast('int', (Code04_Bookcase1.n - 1)))
                else:
                    if jcall(op, 'equals', 'Insert'):
                        t = jcast('int', jcall(io, 'nextInt'))
                        Code04_Bookcase1.move(rank, jcast('int', jadd(rank, t)))
                    else:
                        if jcall(op, 'equals', 'Ask'):
                            # rank代表当前数字的排名，因为有最左侧的准备值
                            # 所以排名其实是rank-1，题目要返回小于的数量，所以是rank - 2
                            jcall(io, 'println', jcast('int', (rank - 2)))
                        else:
                            # 因为有最左侧的准备值，所以查s+1名的数字
                            jcall(io, 'println', Code04_Bookcase1.query(jcast('int', jadd(s, 1))))
            i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code04_Bookcase1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Bookcase1.MAXN = jcast('int', 80005)
Code04_Bookcase1.head = jcast('int', 0)
Code04_Bookcase1.cnt = jcast('int', 0)
Code04_Bookcase1.num = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.father = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.left = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.right = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.size = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.pos = jarray('int', [Code04_Bookcase1.MAXN])
Code04_Bookcase1.n = jcast('int', 0)
Code04_Bookcase1.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_Bookcase1.main([])

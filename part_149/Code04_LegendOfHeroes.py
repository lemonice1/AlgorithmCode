# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 银河英雄传说
# 一共有30000搜战舰，编号1~30000，一开始每艘战舰各自成一队
# 如果若干战舰变成一队，那么队伍里的所有战舰竖直地排成一列
# 实现如下两种操作，操作一共调用t次
# M l r : 合并l号战舰所在队伍和r号战舰所在队伍
# l号战舰的队伍，整体移动到，r号战舰所在队伍的最末尾战舰的后面
# 如果l号战舰和r号战舰已经是一队，不进行任何操作
# C l r : 如果l号战舰和r号战舰不在一个队伍，打印-1
# 如果l号战舰和r号战舰在一个队伍，打印它俩中间隔着几艘战舰
# 1 <= t <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1196
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LegendOfHeroes:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'father': 'father', 'dist': 'dist', 'size': 'size', 'stack': 'stack'}
    MAXN = 0
    n = 0
    father = None
    dist = None
    size = None
    # 递归会爆栈，所以用迭代来寻找并查集代表节点
    stack = None
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code04_LegendOfHeroes.n):
            Code04_LegendOfHeroes.father[i] = jcast('int', i)
            Code04_LegendOfHeroes.dist[i] = jcast('int', 0)
            Code04_LegendOfHeroes.size[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    # 迭代的方式实现find，递归方式实现会爆栈
    @staticmethod
    def find(i):
        i = jcast('int', i)
        si = jcast('int', 0)
        while (i != Code04_LegendOfHeroes.father[i]):
            jset(Code04_LegendOfHeroes.stack, (si := jcast('int', (si + (1)))), i)
            i = jcast('int', Code04_LegendOfHeroes.father[i])
        Code04_LegendOfHeroes.stack[jcast('int', jadd(si, 1))] = jcast('int', i)
        j = jcast('int', si)
        while (j >= 1):
            jset(Code04_LegendOfHeroes.father, Code04_LegendOfHeroes.stack[j], i)
            ((_java_obj_1 := Code04_LegendOfHeroes.dist), (_java_key_2 := Code04_LegendOfHeroes.stack[j]), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), Code04_LegendOfHeroes.dist[Code04_LegendOfHeroes.stack[jcast('int', jadd(j, 1))]]))))[2]
            j = jcast('int', (j - 1))
        return jcast('int', i)

    @staticmethod
    def union(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        lf = jcast('int', Code04_LegendOfHeroes.find(l))
        rf = jcast('int', Code04_LegendOfHeroes.find(r))
        if (lf != rf):
            Code04_LegendOfHeroes.father[lf] = jcast('int', rf)
            Code04_LegendOfHeroes.dist[lf] = jcast('int', jcast('int', jadd(Code04_LegendOfHeroes.dist[lf], Code04_LegendOfHeroes.size[rf])))
            Code04_LegendOfHeroes.size[rf] = jcast('int', jcast('int', jadd(Code04_LegendOfHeroes.size[rf], Code04_LegendOfHeroes.size[lf])))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (Code04_LegendOfHeroes.find(l) != Code04_LegendOfHeroes.find(r)):
            return jcast('int', jcast('int', (-1)))
        return jcast('int', jcast('int', (jstatic('Math', 'abs', jcast('int', (Code04_LegendOfHeroes.dist[l] - Code04_LegendOfHeroes.dist[r]))) - 1)))

    @staticmethod
    def main(args):
        Code04_LegendOfHeroes.prepare()
        io = Code04_LegendOfHeroes.Kattio(_java_ctor=0)
        t = jcast('int', jcall(io, 'nextInt'))
        op = None
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= t):
            op = jcall(io, 'next')
            l = jcast('int', jcall(io, 'nextInt'))
            r = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'M'):
                Code04_LegendOfHeroes.union(l, r)
            else:
                jcall(io, 'println', Code04_LegendOfHeroes.query(l, r))
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
            except Exception as _java_exception_3:
                if jinstanceof(_java_exception_3, 'Exception'):
                    e = _java_exception_3
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
            raise TypeError("No matching overload for Code04_LegendOfHeroes.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LegendOfHeroes.MAXN = jcast('int', 30001)
Code04_LegendOfHeroes.n = jcast('int', 30000)
Code04_LegendOfHeroes.father = jarray('int', [Code04_LegendOfHeroes.MAXN])
Code04_LegendOfHeroes.dist = jarray('int', [Code04_LegendOfHeroes.MAXN])
Code04_LegendOfHeroes.size = jarray('int', [Code04_LegendOfHeroes.MAXN])
Code04_LegendOfHeroes.stack = jarray('int', [Code04_LegendOfHeroes.MAXN])

if __name__ == '__main__':
    Code04_LegendOfHeroes.main([])

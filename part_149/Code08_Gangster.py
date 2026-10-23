# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 团伙
# 注意洛谷关于本题的描述有问题，请按照如下的描述来理解题意
# 一共有n个黑帮成员，编号1 ~ n，发现了m条事实，每条事实一定属于如下两种类型中的一种
# F l r : l号成员和r号成员是朋友
# E l r : l号成员和r号成员是敌人
# 黑帮遵守如下的约定，敌人的敌人一定是朋友，朋友都来自同一个黑帮，敌人一定不是同一个黑帮
# 如果根据事实无法推断出一个成员有哪些朋友，那么该成员自己是一个黑帮
# 输入数据不存在矛盾，也就是任何两人不会推出既是朋友又是敌人的结论
# 遵守上面的约定，根据m条事实，计算黑帮有多少个
# 1 <= n <= 1000    1 <= m <= 5000
# 测试链接 : https://www.luogu.com.cn/problem/P1892
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Gangster:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'father': 'father', 'enemy': 'enemy'}
    MAXN = 0
    n = 0
    m = 0
    father = None
    enemy = None
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code08_Gangster.n):
            Code08_Gangster.father[i] = jcast('int', i)
            Code08_Gangster.enemy[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code08_Gangster.father, i, (i if (Code08_Gangster.father[i] == i) else Code08_Gangster.find(Code08_Gangster.father[i])))
        return jcast('int', Code08_Gangster.father[i])

    @staticmethod
    def union(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        jset(Code08_Gangster.father, Code08_Gangster.find(l), Code08_Gangster.find(r))

    @staticmethod
    def main(args):
        io = Code08_Gangster.Kattio(_java_ctor=0)
        Code08_Gangster.n = jcast('int', jcall(io, 'nextInt'))
        Code08_Gangster.m = jcast('int', jcall(io, 'nextInt'))
        Code08_Gangster.prepare()
        op = None
        l = 0
        r = 0
        i = jcast('int', 1)
        while (i <= Code08_Gangster.m):
            op = jcall(io, 'next')
            l = jcast('int', jcall(io, 'nextInt'))
            r = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'F'):
                Code08_Gangster.union(l, r)
            else:
                if (Code08_Gangster.enemy[l] == 0):
                    Code08_Gangster.enemy[l] = jcast('int', r)
                else:
                    Code08_Gangster.union(Code08_Gangster.enemy[l], r)
                if (Code08_Gangster.enemy[r] == 0):
                    Code08_Gangster.enemy[r] = jcast('int', l)
                else:
                    Code08_Gangster.union(l, Code08_Gangster.enemy[r])
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_Gangster.n):
            if (i == Code08_Gangster.father[i]):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        jcall(io, 'println', ans)
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
            except Exception as _java_exception_1:
                if jinstanceof(_java_exception_1, 'Exception'):
                    e = _java_exception_1
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
            raise TypeError("No matching overload for Code08_Gangster.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Gangster.MAXN = jcast('int', 1001)
Code08_Gangster.n = jcast('int', 0)
Code08_Gangster.m = jcast('int', 0)
Code08_Gangster.father = jarray('int', [Code08_Gangster.MAXN])
Code08_Gangster.enemy = jarray('int', [Code08_Gangster.MAXN])

if __name__ == '__main__':
    Code08_Gangster.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 动态排名，Python版
# 给定一个长度为n的数组arr，下标1~n，每条操作都是如下2种类型中的一种，一共进行m次操作
# 操作 Q x y z : 查询arr[x..y]中排第z名的数字
# 操作 C x y   : arr中x位置的数字改成y
# 1 <= n、m <= 10^5
# 数组中的值永远在[0, 10^9]范围内
# 测试链接 : https://www.luogu.com.cn/problem/P2617
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_DynamicRankings1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'ques': 'ques', 'sorted': 'sorted', 'root': 'root', 'sum': 'sum', 'left': 'left', 'right': 'right', 'cntt': 'cntt', 'addTree': 'addTree', 'minusTree': 'minusTree', 'cntadd': 'cntadd', 'cntminus': 'cntminus'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    s = 0
    arr = None
    ques = None
    sorted = None
    root = None
    sum = None
    left = None
    right = None
    cntt = 0
    addTree = None
    minusTree = None
    cntadd = 0
    cntminus = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code05_DynamicRankings1.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code05_DynamicRankings1.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code05_DynamicRankings1.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def innerAdd(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_1 := Code05_DynamicRankings1), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code05_DynamicRankings1.sum[i] = jcast('int', jcast('int', jadd(Code05_DynamicRankings1.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code05_DynamicRankings1.left, i, Code05_DynamicRankings1.innerAdd(jobi, jobv, l, mid, Code05_DynamicRankings1.left[i]))
            else:
                jset(Code05_DynamicRankings1.right, i, Code05_DynamicRankings1.innerAdd(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code05_DynamicRankings1.right[i]))
            Code05_DynamicRankings1.sum[i] = jcast('int', jcast('int', jadd(Code05_DynamicRankings1.sum[Code05_DynamicRankings1.left[i]], Code05_DynamicRankings1.sum[Code05_DynamicRankings1.right[i]])))
        return jcast('int', i)

    @staticmethod
    def innerQuery(jobk, l, r):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        leftsum = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.cntadd):
            leftsum = jcast('int', jcast('int', jadd(leftsum, Code05_DynamicRankings1.sum[Code05_DynamicRankings1.left[Code05_DynamicRankings1.addTree[i]]])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.cntminus):
            leftsum = jcast('int', jcast('int', (leftsum - Code05_DynamicRankings1.sum[Code05_DynamicRankings1.left[Code05_DynamicRankings1.minusTree[i]]])))
            i = jcast('int', (i + 1))
        if (jobk <= leftsum):
            i = jcast('int', 1)
            while (i <= Code05_DynamicRankings1.cntadd):
                Code05_DynamicRankings1.addTree[i] = jcast('int', Code05_DynamicRankings1.left[Code05_DynamicRankings1.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code05_DynamicRankings1.cntminus):
                Code05_DynamicRankings1.minusTree[i] = jcast('int', Code05_DynamicRankings1.left[Code05_DynamicRankings1.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code05_DynamicRankings1.innerQuery(jobk, l, mid))
        else:
            i = jcast('int', 1)
            while (i <= Code05_DynamicRankings1.cntadd):
                Code05_DynamicRankings1.addTree[i] = jcast('int', Code05_DynamicRankings1.right[Code05_DynamicRankings1.addTree[i]])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code05_DynamicRankings1.cntminus):
                Code05_DynamicRankings1.minusTree[i] = jcast('int', Code05_DynamicRankings1.right[Code05_DynamicRankings1.minusTree[i]])
                i = jcast('int', (i + 1))
            return jcast('int', Code05_DynamicRankings1.innerQuery(jcast('int', (jobk - leftsum)), jcast('int', jadd(mid, 1)), r))

    @staticmethod
    def add(i, cnt):
        i = jcast('int', i)
        cnt = jcast('int', cnt)
        j = jcast('int', i)
        while (j <= Code05_DynamicRankings1.n):
            jset(Code05_DynamicRankings1.root, j, Code05_DynamicRankings1.innerAdd(Code05_DynamicRankings1.arr[i], cnt, 1, Code05_DynamicRankings1.s, Code05_DynamicRankings1.root[j]))
            j = jcast('int', jcast('int', jadd(j, Code05_DynamicRankings1.lowbit(j))))

    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code05_DynamicRankings1.add(i, jcast('int', (-1)))
        jset(Code05_DynamicRankings1.arr, i, Code05_DynamicRankings1.kth(v))
        Code05_DynamicRankings1.add(i, 1)

    @staticmethod
    def number(l, r, k):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        Code05_DynamicRankings1.cntadd = jcast('int', jset(Code05_DynamicRankings1, 'cntminus', 0))
        i = jcast('int', r)
        while (i > 0):
            jset(Code05_DynamicRankings1.addTree, ((_java_obj_4 := Code05_DynamicRankings1), (_java_key_5 := 'cntadd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_DynamicRankings1.root[i])
            i = jcast('int', jcast('int', (i - Code05_DynamicRankings1.lowbit(i))))
        i = jcast('int', jcast('int', (l - 1)))
        while (i > 0):
            jset(Code05_DynamicRankings1.minusTree, ((_java_obj_7 := Code05_DynamicRankings1), (_java_key_8 := 'cntminus'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code05_DynamicRankings1.root[i])
            i = jcast('int', jcast('int', (i - Code05_DynamicRankings1.lowbit(i))))
        return jcast('int', Code05_DynamicRankings1.sorted[Code05_DynamicRankings1.innerQuery(k, 1, Code05_DynamicRankings1.s)])

    @staticmethod
    def prepare():
        Code05_DynamicRankings1.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.n):
            jset(Code05_DynamicRankings1.sorted, ((_java_obj_10 := Code05_DynamicRankings1), (_java_key_11 := 's'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code05_DynamicRankings1.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.m):
            if (Code05_DynamicRankings1.ques[i][0] == 2):
                jset(Code05_DynamicRankings1.sorted, ((_java_obj_13 := Code05_DynamicRankings1), (_java_key_14 := 's'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code05_DynamicRankings1.ques[i][2])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_DynamicRankings1.sorted, 1, jcast('int', jadd(Code05_DynamicRankings1.s, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_DynamicRankings1.s):
            if (Code05_DynamicRankings1.sorted[len] != Code05_DynamicRankings1.sorted[i]):
                jset(Code05_DynamicRankings1.sorted, (len := jcast('int', (len + (1)))), Code05_DynamicRankings1.sorted[i])
            i = jcast('int', (i + 1))
        Code05_DynamicRankings1.s = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.n):
            jset(Code05_DynamicRankings1.arr, i, Code05_DynamicRankings1.kth(Code05_DynamicRankings1.arr[i]))
            Code05_DynamicRankings1.add(i, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        io = Code05_DynamicRankings1.Kattio(_java_ctor=0)
        Code05_DynamicRankings1.n = jcast('int', jcall(io, 'nextInt'))
        Code05_DynamicRankings1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.n):
            jset(Code05_DynamicRankings1.arr, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_DynamicRankings1.m):
            jset(Code05_DynamicRankings1.ques[i], 0, (1 if jcall(jcall(io, 'next'), 'equals', 'Q') else 2))
            jset(Code05_DynamicRankings1.ques[i], 1, jcall(io, 'nextInt'))
            jset(Code05_DynamicRankings1.ques[i], 2, jcall(io, 'nextInt'))
            if (Code05_DynamicRankings1.ques[i][0] == 1):
                jset(Code05_DynamicRankings1.ques[i], 3, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code05_DynamicRankings1.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code05_DynamicRankings1.m):
            op = jcast('int', Code05_DynamicRankings1.ques[i][0])
            x = jcast('int', Code05_DynamicRankings1.ques[i][1])
            y = jcast('int', Code05_DynamicRankings1.ques[i][2])
            if (op == 1):
                z = jcast('int', Code05_DynamicRankings1.ques[i][3])
                jcall(io, 'println', Code05_DynamicRankings1.number(x, y, z))
            else:
                Code05_DynamicRankings1.update(x, y)
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
            except Exception as _java_exception_16:
                if jinstanceof(_java_exception_16, 'Exception'):
                    e = _java_exception_16
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
            raise TypeError("No matching overload for Code05_DynamicRankings1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_DynamicRankings1.MAXN = jcast('int', 100001)
Code05_DynamicRankings1.MAXT = jcast('int', jcast('int', (Code05_DynamicRankings1.MAXN * 130)))
Code05_DynamicRankings1.n = jcast('int', 0)
Code05_DynamicRankings1.m = jcast('int', 0)
Code05_DynamicRankings1.s = jcast('int', 0)
Code05_DynamicRankings1.arr = jarray('int', [Code05_DynamicRankings1.MAXN])
Code05_DynamicRankings1.ques = jarray('int', [Code05_DynamicRankings1.MAXN, 4])
Code05_DynamicRankings1.sorted = jarray('int', [jcast('int', (Code05_DynamicRankings1.MAXN * 2))])
Code05_DynamicRankings1.root = jarray('int', [Code05_DynamicRankings1.MAXN])
Code05_DynamicRankings1.sum = jarray('int', [Code05_DynamicRankings1.MAXT])
Code05_DynamicRankings1.left = jarray('int', [Code05_DynamicRankings1.MAXT])
Code05_DynamicRankings1.right = jarray('int', [Code05_DynamicRankings1.MAXT])
Code05_DynamicRankings1.cntt = jcast('int', 0)
Code05_DynamicRankings1.addTree = jarray('int', [Code05_DynamicRankings1.MAXN])
Code05_DynamicRankings1.minusTree = jarray('int', [Code05_DynamicRankings1.MAXN])
Code05_DynamicRankings1.cntadd = jcast('int', 0)
Code05_DynamicRankings1.cntminus = jcast('int', 0)

if __name__ == '__main__':
    Code05_DynamicRankings1.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 烹调方案
# 课上没有讲这个题，本节课的题目5，砍树问题，现在验证已经很困难了
# 所以找到这个题作为平替，因为贪心的思路是非常类似的
#
# 一共有n个食材，一共有m秒可以加工食材，你只能串行加工食材
# 每个食材的初始美味度为a[i]，美味衰减速度b[i]，加工花费c[i]秒
# 第i个食材美味度 = a[i] - t * b[i]，t是加工食材的时刻
# 计算m秒内，你能获得的最大美味度总和
# 1 <= n <= 50
# 其他数据 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1417
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
#
# 本题的分析过程
# 假设当前来到s时刻，食材x和食材y，必须选择一个先加工
# 选择1，先加工x，后加工y，获得食材x的美味时刻是s，y的时刻是s + c[x]
# 选择1的美味度 = a[x] - s * b[x] + a[y] - (s + c[x]) * b[y]
# = a[x] - s * b[x] + a[y] - s * b[y] - c[x] * b[y]
#
# 选择2，先加工y，后加工x，获得食材y的美味时刻是s，x的时刻是s + c[y]
# 选择2的美味度 = a[y] - s * b[y] + a[x] - (s + c[y]) * b[x]
# = a[y] - s * b[y] + a[x] - s * b[x] - c[y] * b[x]
#
# 选择1和选择2的公共部分 = a[x] + a[y] - s * b[x] - s * b[y]，记为common
# 选择1 = common - c[x] * b[y]
# 选择2 = common - c[y] * b[x]
# 也就是说，如果c[x] * b[y] <= c[y] * b[x]，先选食材x，否则先选食材y
# 于是排序策略搞定了，剩下就和题目5一样了，01背包的解法，并且可以空间压缩
# 代码如下
class Code06_CookingPlan:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'food': 'food', 'dp': 'dp'}
    class Food:
        __java_fields__ = {'a': 'a', 'b': 'b', 'c': 'c'}
        # a：实例字段，在构造函数中初始化。
        # b：实例字段，在构造函数中初始化。
        # c：实例字段，在构造函数中初始化。
        def _java_init_0(self, x, y, z):
            x = jcast('int', x)
            y = jcast('int', y)
            z = jcast('int', z)
            self.a = jcast('int', x)
            self.b = jcast('int', y)
            self.c = jcast('int', z)

        def __init__(self, *args, _java_ctor=None):
            self.a = jcast('int', 0)
            self.b = jcast('int', 0)
            self.c = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_CookingPlan.Food.Food")


    class FoodCmp:
        __java_fields__ = {}
        def compare(self, x, y):
            if (jcast('long', (jcast('long', jget(x, 'c')) * jcast('long', jget(y, 'b')))) <= jcast('long', (jcast('long', jget(y, 'c')) * jcast('long', jget(x, 'b'))))):
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', 1)

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    food = None
    dp = None
    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code06_CookingPlan.food, 1, jcast('int', jadd(Code06_CookingPlan.n, 1)), Code06_CookingPlan.FoodCmp())
        Code06_CookingPlan.dp[0] = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.m):
            Code06_CookingPlan.dp[i] = jcast('long', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.n):
            j = jcast('int', Code06_CookingPlan.m)
            p = jcast('int', jcast('int', (j - jget(Code06_CookingPlan.food[i], 'c'))))
            while (p >= 0):
                if (Code06_CookingPlan.dp[p] != jcast('int', (-1))):
                    jset(Code06_CookingPlan.dp, j, jstatic('Math', 'max', Code06_CookingPlan.dp[j], jcast('long', (jcast('long', jadd(Code06_CookingPlan.dp[p], jget(Code06_CookingPlan.food[i], 'a'))) - jcast('long', (jcast('long', j) * jget(Code06_CookingPlan.food[i], 'b')))))))
                j = jcast('int', (j - 1))
                p = jcast('int', (p - 1))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.m):
            ans = jcast('long', jstatic('Math', 'max', ans, Code06_CookingPlan.dp[i]))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code06_CookingPlan.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_CookingPlan.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_CookingPlan.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.n):
            jset(Code06_CookingPlan.food, i, Code06_CookingPlan.Food(0, 0, 0, _java_ctor=0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.n):
            jset(Code06_CookingPlan.food[i], 'a', jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.n):
            jset(Code06_CookingPlan.food[i], 'b', jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_CookingPlan.n):
            jset(Code06_CookingPlan.food[i], 'c', jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('long', Code06_CookingPlan.compute())
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_CookingPlan.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_CookingPlan.MAXN = jcast('int', 51)
Code06_CookingPlan.MAXM = jcast('int', 100001)
Code06_CookingPlan.n = jcast('int', 0)
Code06_CookingPlan.m = jcast('int', 0)
Code06_CookingPlan.food = jarray('Food', [Code06_CookingPlan.MAXN])
Code06_CookingPlan.dp = jarray('long', [Code06_CookingPlan.MAXM])

if __name__ == '__main__':
    Code06_CookingPlan.main([])

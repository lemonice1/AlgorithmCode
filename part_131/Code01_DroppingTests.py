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

# 01分数规划模版题
# 给定n个数据，每个数据有(a, b)两个值，都为整数，并且都是非负的
# 请舍弃掉k个数据，希望让剩下数据做到，所有a的和 / 所有b的和，这个比值尽量大
# 如果剩下数据所有b的和为0，认为无意义
# 最后，将该比值 * 100，小数部分四舍五入的整数结果返回
# 1 <= n <= 100
# 0 <= a、b <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P10505
# 测试链接 : http://poj.org/problem?id=2976
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DroppingTests:
    __java_fields__ = {'MAXN': 'MAXN', 'sml': 'sml', 'arr': 'arr', 'n': 'n', 'k': 'k'}
    MAXN = 0
    sml = 0.0
    # arr[i][0] = i号数据的a
    # arr[i][1] = i号数据的b
    # arr[i][2] = i号数据的结余，a - x * b
    arr = None
    n = 0
    k = 0
    @staticmethod
    def check(x):
        x = jcast('double', x)
        # x固定的情况下，得到所有数据的结余
        i = jcast('int', 1)
        while (i <= Code01_DroppingTests.n):
            jset(Code01_DroppingTests.arr[i], 2, (Code01_DroppingTests.arr[i][0] - (x * Code01_DroppingTests.arr[i][1])))
            i = jcast('int', (i + 1))
        # 结余从大到小排序
        jstatic('Arrays', 'sort', Code01_DroppingTests.arr, 1, jcast('int', jadd(Code01_DroppingTests.n, 1)), Code01_DroppingTests.MyComparator())
        # 最大k个结余的累加和
        sum = jcast('double', 0)
        i = jcast('int', 1)
        while (i <= Code01_DroppingTests.k):
            sum = jcast('double', jadd(sum, Code01_DroppingTests.arr[i][2]))
            i = jcast('int', (i + 1))
        return jcast('boolean', (sum >= 0))

    # 比较器接口保留在兼容层中，Python 可使用函数或 lambda 表达式定义比较规则
    class MyComparator:
        __java_fields__ = {}
        def compare(self, o1, o2):
            return jcast('int', (jcast('int', (-1)) if (o1[2] >= o2[2]) else 1))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_DroppingTests.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_DroppingTests.k = jcast('int', jcast('int', jget(in_, 'nval')))
        while ((Code01_DroppingTests.n != 0) or (Code01_DroppingTests.k != 0)):
            # 题目要求舍弃掉k个，其实就是挑选n-k个
            Code01_DroppingTests.k = jcast('int', jcast('int', (Code01_DroppingTests.n - Code01_DroppingTests.k)))
            i = jcast('int', 1)
            while (i <= Code01_DroppingTests.n):
                jcall(in_, 'nextToken')
                jset(Code01_DroppingTests.arr[i], 0, jget(in_, 'nval'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code01_DroppingTests.n):
                jcall(in_, 'nextToken')
                jset(Code01_DroppingTests.arr[i], 1, jget(in_, 'nval'))
                i = jcast('int', (i + 1))
            l = jcast('double', 0)
            r = jcast('double', 0)
            x = 0.0
            i = jcast('int', 1)
            while (i <= Code01_DroppingTests.n):
                r = jcast('double', jadd(r, Code01_DroppingTests.arr[i][0]))
                i = jcast('int', (i + 1))
            ans = jcast('double', 0)
            while ((l < r) and ((r - l) >= Code01_DroppingTests.sml)):
                x = jcast('double', jdiv(jadd(l, r), 2))
                if Code01_DroppingTests.check(x):
                    ans = jcast('double', x)
                    l = jcast('double', jadd(x, Code01_DroppingTests.sml))
                else:
                    r = jcast('double', (x - Code01_DroppingTests.sml))
            jcall(out, 'println', jcast('int', (100 * jadd(ans, 0.005))))
            jcall(in_, 'nextToken')
            Code01_DroppingTests.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_DroppingTests.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DroppingTests.MAXN = jcast('int', 1001)
Code01_DroppingTests.sml = jcast('double', 1e-06)
Code01_DroppingTests.arr = jarray('double', [Code01_DroppingTests.MAXN, 3])
Code01_DroppingTests.n = jcast('int', 0)
Code01_DroppingTests.k = jcast('int', 0)

if __name__ == '__main__':
    Code01_DroppingTests.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# windy数
# 不含前导零且相邻两个数字之差至少为2的正整数被称为windy数
# windy想知道[a,b]范围上总共有多少个windy数
# 测试链接 : https://www.luogu.com.cn/problem/P2657
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_WindyNumber:
    __java_fields__ = {'MAXLEN': 'MAXLEN', 'dp': 'dp'}
    MAXLEN = 0
    dp = None
    @staticmethod
    def build(len):
        len = jcast('int', len)
        i = jcast('int', 0)
        while (i <= len):
            j = jcast('int', 0)
            while (j <= 10):
                jset(Code01_WindyNumber.dp[i][j], 0, jcast('int', (-1)))
                jset(Code01_WindyNumber.dp[i][j], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code01_WindyNumber.compute(a, b))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', jcast('int', (Code01_WindyNumber.cnt(b) - Code01_WindyNumber.cnt(jcast('int', (a - 1))))))

    # 求0~num范围上，windy数的个数
    @staticmethod
    def cnt(num):
        num = jcast('int', num)
        if (num == 0):
            return jcast('int', 1)
        len = jcast('int', 1)
        offset = jcast('int', 1)
        tmp = jcast('int', jcast('int', jdiv(num, 10)))
        while (tmp > 0):
            len = jcast('int', (len + 1))
            offset = jcast('int', jcast('int', (offset * 10)))
            tmp = jcast('int', jcast('int', jdiv(tmp, 10)))
        Code01_WindyNumber.build(len)
        return jcast('int', Code01_WindyNumber.f(num, offset, len, 10, 0))

    # offset完全由len决定，为了方便提取num中某一位数字（上节课内容）
    # 从num的高位开始，还剩下len位没有决定
    # 前一位的数字是pre，如果pre == 10，表示从来没有选择过数字
    # 如果之前的位已经确定比num小，那么free == 1，表示接下的数字可以自由选择
    # 如果之前的位和num一样，那么free == 0，表示接下的数字不能大于num当前位的数字
    # 返回<=num的windy数有多少个
    @staticmethod
    def f(num, offset, len, pre, free):
        num = jcast('int', num)
        offset = jcast('int', offset)
        len = jcast('int', len)
        pre = jcast('int', pre)
        free = jcast('int', free)
        if (len == 0):
            return jcast('int', 1)
        if (Code01_WindyNumber.dp[len][pre][free] != jcast('int', (-1))):
            return jcast('int', Code01_WindyNumber.dp[len][pre][free])
        cur = jcast('int', jcast('int', jmod(jcast('int', jdiv(num, offset)), 10)))
        ans = jcast('int', 0)
        if (free == 0):
            if (pre == 10):
                # 之前的位和num一样，此时不能随意选择数字
                # 也从来没有选择过数字
                # 就表示：来到的是num的最高位
                # 一个数字也不要
                ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), 10, 1))))
                i = jcast('int', 1)
                while (i < cur):
                    ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
                ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), cur, 0))))
            else:
                # 之前的位和num一样，此时不能随意选择数字，
                # 之前选择过数字pre
                i = jcast('int', 0)
                while (i <= 9):
                    if ((i <= jcast('int', (pre - 2))) or (i >= jcast('int', jadd(pre, 2)))):
                        if (i < cur):
                            ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                        else:
                            if (i == cur):
                                ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), cur, 0))))
                    i = jcast('int', (i + 1))
        else:
            if (pre == 10):
                # free == 1，可以自由选择数字，前面的状况 < num
                # 从来没有选择过数字
                # 还是可以不选择数字
                ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), 10, 1))))
                i = jcast('int', 1)
                while (i <= 9):
                    ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
            else:
                # free == 1，可以自由选择数字，前面的状况 < num
                # 选择过数字pre
                i = jcast('int', 0)
                while (i <= 9):
                    if ((i <= jcast('int', (pre - 2))) or (i >= jcast('int', jadd(pre, 2)))):
                        ans = jcast('int', jcast('int', jadd(ans, Code01_WindyNumber.f(num, jcast('int', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
        jset(Code01_WindyNumber.dp[len][pre], free, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_WindyNumber.MAXLEN = jcast('int', 11)
Code01_WindyNumber.dp = jarray('int', [Code01_WindyNumber.MAXLEN, 11, 2])

if __name__ == '__main__':
    Code01_WindyNumber.main([])
